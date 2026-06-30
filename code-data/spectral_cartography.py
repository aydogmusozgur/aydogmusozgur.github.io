# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 17:58:19 2025

@author: Lenovo
"""

# -*- coding: utf-8 -*-
"""
Full Analysis Suite for Spatial 2x2 Games: Derrida Slopes, Frequencies, and Phase Boundaries
--------------------------------------------------------------------------------------------
Features:
1. "Dual Calculator": Simulates two replicas to measure both evolutionary outcome (f_infty)
   and dynamical chaos (d_infty / Hamming distance).
2. Optimized Core: Uses Numba JIT with fastmath and manual loop unrolling for maximum speed.
3. Smart Stopping: Auto-detects frozen states to skip unnecessary computation in stable regions.
4. Theory Overlay: Plots the 8 analytical phase boundaries derived in the paper.

Author: Assistant
"""

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import multiprocessing as mp
from numba import njit
import os

# =============================================================================
# 1. OPTIMIZED CORE CA MODEL (Numba JIT)
# =============================================================================

@njit(fastmath=True)
def calculate_payoffs(grid, pm, pay):
    """
    Calculates payoffs for the Von Neumann neighborhood with periodic boundaries.
    """
    rows, cols = grid.shape
    for i in range(rows):
        # Fast torus wrapping (avoiding modulo % for speed)
        up = (i - 1) if i > 0 else rows - 1
        down = (i + 1) if i < rows - 1 else 0
        for j in range(cols):
            left = (j - 1) if j > 0 else cols - 1
            right = (j + 1) if j < cols - 1 else 0
            
            me = grid[i, j]
            score = 0.0
            # Manual unroll for vectorization hints
            score += pm[me, grid[up, j]]
            score += pm[me, grid[down, j]]
            score += pm[me, grid[i, left]]
            score += pm[me, grid[i, right]]
            pay[i, j] = score

@njit(fastmath=True)
def update_grid(grid, pay, new_grid):
    """
    Deterministic 'Imitate-the-Best' rule.
    Returns True if the grid changed, False if frozen.
    """
    rows, cols = grid.shape
    changed = False
    for i in range(rows):
        up = (i - 1) if i > 0 else rows - 1
        down = (i + 1) if i < rows - 1 else 0
        for j in range(cols):
            left = (j - 1) if j > 0 else cols - 1
            right = (j + 1) if j < cols - 1 else 0
            
            best_s = grid[i, j]
            best_p = pay[i, j]
            
            # Strict inequality check (>): Keep current if tie
            if pay[up, j] > best_p:
                best_p = pay[up, j]
                best_s = grid[up, j]
            if pay[down, j] > best_p:
                best_p = pay[down, j]
                best_s = grid[down, j]
            if pay[i, left] > best_p:
                best_p = pay[i, left]
                best_s = grid[i, left]
            if pay[i, right] > best_p:
                best_p = pay[i, right]
                best_s = grid[i, right]
            
            if best_s != grid[i, j]:
                changed = True
            new_grid[i, j] = best_s
            
    return changed

@njit(fastmath=True)
def evolve_and_measure(grid1, grid2, pm, max_steps=2000, sample_steps=100):
    """
    Evolves two replicas simultaneously.
    - grid1: Main simulation for Frequency.
    - grid2: Perturbed copy for Hamming Distance.
    Returns: (Average Cooperator Frequency, Average Hamming Distance)
    """
    rows, cols = grid1.shape
    N = float(rows * cols)
    
    # Allocations
    pay1 = np.zeros(grid1.shape, dtype=np.float64)
    pay2 = np.zeros(grid2.shape, dtype=np.float64)
    new1 = np.zeros(grid1.shape, dtype=np.int8)
    new2 = np.zeros(grid2.shape, dtype=np.int8)
    
    avg_freq = 0.0
    avg_ham = 0.0
    
    burn_in = max_steps - sample_steps
    
    for t in range(max_steps):
        # 1. Calculate Payoffs
        calculate_payoffs(grid1, pm, pay1)
        calculate_payoffs(grid2, pm, pay2)
        
        # 2. Update Strategies
        c1 = update_grid(grid1, pay1, new1)
        c2 = update_grid(grid2, pay2, new2)
        
        # 3. Swap buffers (copy new to old)
        grid1[:] = new1[:]
        grid2[:] = new2[:]
        
        # 4. Measurements
        # Current Freq of Cooperators (0). grid sum is count of Defectors (1).
        current_f = 1.0 - (np.sum(grid1) / N)
        current_d = np.sum(grid1 != grid2) / N
        
        if t >= burn_in:
            avg_freq += current_f
            avg_ham += current_d
        
        # 5. Early Stopping Optimization
        # If both grids are frozen (no changes), we can stop early.
        if (not c1) and (not c2):
            # If we are in the sampling phase or haven't reached it,
            # the values will remain constant for all future steps.
            # We add the weighted remaining average to the result.
            remaining_steps = max_steps - 1 - t
            
            # How many of these remaining steps are inside the sampling window?
            # We are currently at step 't'.
            # The window is [burn_in, max_steps).
            
            # Steps effectively computed so far in the window:
            steps_in_window_so_far = max(0, t - burn_in + 1)
            
            # Total steps that WOULD be in the window if we ran to completion:
            total_window_steps = sample_steps
            
            # Steps remaining to be added to the average:
            steps_remaining_in_window = total_window_steps - steps_in_window_so_far
            
            if steps_remaining_in_window > 0:
                avg_freq += current_f * steps_remaining_in_window
                avg_ham += current_d * steps_remaining_in_window
            
            break # Stop the loop
            
    return avg_freq / sample_steps, avg_ham / sample_steps

def create_payoff_matrix(u, v):
    """R=1, P=0, T=1+u, S=v. Index 0=Coop, 1=Defect."""
    return np.array([[1.0, v], [1.0+u, 0.0]], dtype=np.float64)

# =============================================================================
# 2. PARALLEL PARAMETER SCANNING
# =============================================================================

def one_point(args):
    """Worker function for a single (u,v) point."""
    i, j, u, v, seed, grid_size, fC0 = args
    rng = np.random.default_rng(seed)
    
    # 1. Init Grid 1 (0=C, 1=D)
    # rng >= fC0 ensures prob(0) = fC0.
    grid1 = (rng.random((grid_size, grid_size)) >= fC0).astype(np.int8)
    
    # 2. Init Grid 2 (Perturbed copy)
    grid2 = grid1.copy()
    # Flip one random site
    rx, ry = rng.integers(0, grid_size, 2)
    grid2[rx, ry] = 1 - grid2[rx, ry]
    
    pm = create_payoff_matrix(u, v)
    
    # Run
    f_final, d_final = evolve_and_measure(grid1, grid2, pm)
    
    return i, j, f_final, d_final

def scan_plane(u_vals, v_vals, fC0, grid_size=50, replicates=5, master_seed=42):
    num_cores = mp.cpu_count()
    map_freq = np.zeros((len(v_vals), len(u_vals)))
    map_ham = np.zeros((len(v_vals), len(u_vals)))
    
    tasks = []
    for i, u in enumerate(u_vals):
        for j, v in enumerate(v_vals):
            for rep in range(replicates):
                # Robust unique seeding
                seed = (master_seed + i*7919 + j*104729 + rep*9973) % (2**32)
                tasks.append((i, j, u, v, seed, grid_size, fC0))
                
    print(f"Scanning fC0={fC0} on {num_cores} cores...")
    
    with mp.Pool(num_cores) as pool:
        # chunksize=5 helps load balancing
        for i, j, f, d in tqdm(pool.imap_unordered(one_point, tasks, chunksize=5), total=len(tasks)):
            map_freq[j, i] += f / replicates
            map_ham[j, i]  += d / replicates
            
    return map_freq, map_ham

# =============================================================================
# 3. PLOTTING & THEORY OVERLAY
# =============================================================================

def add_theoretical_lines(ax, u_vals):
    """Overlay analytical phase boundaries and characteristic stability lines."""
    # === 1. Global Mode Limits (k = 0) ===
    ax.plot(u_vals, 4*u_vals + 1, "k-", lw=1.0, alpha=0.8, label=r"Global Inv. (D): $v=4u+1$")
    ax.plot(u_vals, 0.25*u_vals + 0.25, "k--", lw=1.0, alpha=0.8, label=r"Global Inv. (C): $v=0.25u+0.25$")

    # === 2. Stripe Phase (k ≈ (π,0) or (0,π)) ===
    ax.plot(u_vals, 2*u_vals - 1, "r-", lw=1.2, label=r"Stripe Unzipping: $v=2u-1$")

    # === 3. Checkerboard Mode (k = (π,π)) ===
    ax.plot(u_vals, u_vals, "b--", lw=1.0, alpha=0.7, label=r"Checkerboard Eq.: $v=u$")

    # === 4. Oblique / Block Phases (k ≈ (π, π/2)) ===
    ax.plot(u_vals, 0.5*u_vals - 0.5, "m:", lw=1.2, label=r"Block Stability: $v=0.5u-0.5$")
    ax.plot(u_vals, u_vals + 2/3, "c:", lw=1.2, label=r"Domino/Kink: $v=u+2/3$")

    # === 5. Localized Superpositions ===
    ax.plot(u_vals, u_vals/3, "g-.", lw=1.2, label=r"Filament Nucleation: $v=u/3$")
    ax.axvline(x=1/3, color='purple', linestyle='-.', lw=1.2, alpha=0.8, label=r"Core Erosion: $u=1/3$")

    # === 6. Formatting ===
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.legend(fontsize=6, loc='upper left', frameon=True, framealpha=0.9, ncol=2)

# =============================================================================
# 4. MAIN EXECUTION
# =============================================================================

if __name__ == '__main__':
    # --- Simulation Parameters ---
    RES = 400       # Resolution (200x200 pixels)
    GRID = 50       # Lattice size (60x60 sites)
    REPS = 30        # Replicates per pixel
    
    # Parameter Range
    U = np.linspace(-1.0, 1.0, RES)
    V = np.linspace(-1.0, 1.0, RES)
    
    # Directory setup
    os.makedirs("results", exist_ok=True)
    
    # Scan for three standard initial conditions
    for fC0 in [0.01]:
        print(f"\n--- Processing Initial Cooperator Freq: {fC0} ---")
        
        # 1. Run Simulation
        freq_map, ham_map = scan_plane(U, V, fC0, grid_size=GRID, replicates=REPS)

        # 2. Save Raw Data
        #np.save(f"results/freq_map100_fc{fC0}.npy", freq_map)
        np.save(f"results/ham_map001.npy", freq_map)

        # 3. Generate Frequency Plot
        fig1, ax1 = plt.subplots(figsize=(10, 8))
        pcm1 = ax1.pcolormesh(U, V, freq_map, shading='auto', cmap='viridis', vmin=0, vmax=1)
        fig1.colorbar(pcm1, label='Final Cooperator Frequency $f_\\infty$')
        ax1.set_title(f"Final Frequency Map (Initial $f_C={fC0}$)")
        ax1.set_xlabel('Temptation $u$')
        ax1.set_ylabel('Sucker\'s Payoff $v$')
        
        # Overlay Theory
        add_theoretical_lines(ax1, U)
        
        plt.tight_layout()
        plt.savefig(f"results/freq_map_fc{fC0}.png", dpi=300)
        plt.close(fig1)

        # 4. Generate Hamming Distance (Chaos) Plot
        fig2, ax2 = plt.subplots(figsize=(10, 8))
        pcm2 = ax2.pcolormesh(U, V, ham_map, shading='auto', cmap='inferno', vmin=0, vmax=0.5)
        fig2.colorbar(pcm2, label='Asymptotic Hamming Distance $d_\\infty$')
        ax2.set_title(f"Chaos Map / Asymptotic Distance (Initial $f_C={fC0}$)")
        ax2.set_xlabel('Temptation $u$')
        ax2.set_ylabel('Sucker\'s Payoff $v$')
        
        # Overlay Theory
        add_theoretical_lines(ax2, U)
        
        plt.tight_layout()
        plt.savefig(f"results/ham_map_fc{fC0}.png", dpi=300)
        plt.close(fig2)
        
    print("\nDone! All results saved to /results folder.")