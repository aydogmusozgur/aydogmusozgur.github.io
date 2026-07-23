<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Code & Data | Spectral Cartography</title>
    <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --navy: #1a2744;
            --navy-mid: #2c3e6b;
            --accent: #c0392b;
            --bg: #f8f7f4;
            --bg-card: #ffffff;
            --border: #ddd8cf;
            --text: #2a2a2a;
            --text-mid: #4a4a4a;
            --text-soft: #777;
            --badge-code: #1d4e2e;
            --badge-code-bg: #d4edda;
            --badge-data: #1a3a5c;
            --badge-data-bg: #d1e4f5;
            --badge-pdf: #5a1a0a;
            --badge-pdf-bg: #f5ddd9;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'DM Sans', sans-serif; background: var(--bg); color: var(--text); line-height: 1.7; }

        header { background: var(--navy); color: #fff; padding: 36px 24px 28px; }
        .back-link {
            display: inline-flex; align-items: center; gap: 6px;
            color: #a8c4f0; text-decoration: none; font-size: 0.85rem; margin-bottom: 18px;
        }
        .back-link:hover { color: #fff; }
        header h1 {
            font-family: 'EB Garamond', serif; font-size: 1.6rem;
            font-weight: 600; line-height: 1.3; max-width: 700px;
        }
        .meta { margin-top: 8px; font-size: 0.88rem; color: #8a9ab8; }

        .content { max-width: 860px; margin: 40px auto; padding: 0 24px 60px; }

        h2 {
            font-family: 'EB Garamond', serif; font-size: 1.3rem; color: var(--navy);
            border-left: 4px solid var(--accent); padding-left: 12px; margin: 32px 0 14px;
        }

        .abstract-box {
            background: var(--bg-card); border: 1px solid var(--border);
            border-left: 4px solid var(--navy-mid); border-radius: 6px;
            padding: 16px 20px; font-size: 0.9rem; color: var(--text-mid); line-height: 1.75;
        }

        /* ── Code block ── */
        .code-wrap {
            background: #0d1117; border-radius: 8px; overflow: hidden;
            border: 1px solid #30363d;
        }
        .code-toolbar {
            background: #161b22; padding: 10px 16px;
            display: flex; align-items: center; justify-content: space-between;
            border-bottom: 1px solid #30363d;
        }
        .code-filename { font-size: 0.82rem; color: #8b949e; font-family: 'Courier New', monospace; }
        .copy-btn {
            background: #21262d; border: 1px solid #30363d; color: #c9d1d9;
            font-size: 0.78rem; padding: 4px 12px; border-radius: 5px;
            cursor: pointer; font-family: 'DM Sans', sans-serif; transition: background 0.15s;
        }
        .copy-btn:hover { background: #30363d; }
        .copy-btn.copied { color: #3fb950; border-color: #3fb950; }

        .code-scroll { overflow-x: auto; max-height: 520px; overflow-y: auto; }
        pre {
            margin: 0; padding: 18px 20px;
            font-family: 'Courier New', monospace; font-size: 0.78rem;
            line-height: 1.6; color: #e6edf3; tab-size: 4;
        }

        /* Syntax highlighting */
        .kw  { color: #ff7b72; }   /* keywords */
        .cm  { color: #8b949e; font-style: italic; } /* comments */
        .st  { color: #a5d6ff; }   /* strings */
        .fn  { color: #d2a8ff; }   /* function names */
        .dc  { color: #ffa657; }   /* decorators */
        .nm  { color: #79c0ff; }   /* numbers */

        /* ── Download / PDF cards ── */
        .card {
            background: var(--bg-card); border: 1px solid var(--border);
            border-radius: 8px; padding: 18px 20px; margin-bottom: 12px;
            display: flex; align-items: flex-start; gap: 16px;
        }
        .card-icon {
            width: 38px; height: 38px; border-radius: 8px;
            display: flex; align-items: center; justify-content: center; flex-shrink: 0;
        }
        .icon-code { background: var(--badge-code-bg); color: var(--badge-code); }
        .icon-data { background: var(--badge-data-bg); color: var(--badge-data); }
        .icon-pdf  { background: var(--badge-pdf-bg);  color: var(--badge-pdf);  }
        .card-icon svg { width: 18px; height: 18px; }
        .card-body { flex: 1; }
        .card-title { font-weight: 600; font-size: 0.93rem; color: var(--navy); margin-bottom: 3px; }
        .card-desc  { font-size: 0.83rem; color: var(--text-soft); margin-bottom: 10px; }
        .dl-btn {
            display: inline-flex; align-items: center; gap: 6px;
            font-size: 0.8rem; font-weight: 600; padding: 5px 14px;
            border-radius: 5px; text-decoration: none; transition: opacity 0.15s; border: 1px solid;
        }
        .dl-btn:hover { opacity: 0.8; }
        .dl-btn svg { width: 12px; height: 12px; }
        .btn-code { background: var(--badge-code-bg); color: var(--badge-code); border-color: #a8d5b5; }
        .btn-data { background: var(--badge-data-bg); color: var(--badge-data); border-color: #90bce0; }
        .btn-pdf  { background: var(--badge-pdf-bg);  color: var(--badge-pdf);  border-color: #e5b8b0; }

        .cite-box {
            background: #f0f4f8; border: 1px solid #c8d8e8; border-radius: 6px;
            padding: 14px 18px; font-family: 'Courier New', monospace;
            font-size: 0.8rem; color: #2a3a4a; white-space: pre-wrap; word-break: break-word;
        }

        /* ── Dependencies pill list ── */
        .dep-list { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 6px; }
        .dep { background: #0d1117; color: #79c0ff; border: 1px solid #30363d;
               font-family: monospace; font-size: 0.78rem; padding: 2px 10px; border-radius: 20px; }
    </style>
</head>
<body>

<header>
    <a class="back-link" href="../index.html">
        <svg viewBox="0 0 16 16" fill="currentColor" width="14" height="14">
            <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
        </svg>
        Back to profile
    </a>
    <h1>From Local Payoffs to Global Instabilities: A Spectral Cartography of Spatiotemporal Chaos in Canonical 2×2 Evolutionary Games</h1>
    <div class="meta">Ozgur H. Aydogmus &nbsp;·&nbsp; Under Review</div>
</header>

<div class="content">

    <h2>Abstract</h2>
    <div class="abstract-box">
        We investigate the emergence of spatiotemporal chaos in canonical 2×2 evolutionary games defined on spatial lattices, characterizing transitions from stable equilibria to complex dynamics via spectral methods. By scanning the payoff parameter space (temptation <em>u</em>, sucker's payoff <em>v</em>), we construct a spectral cartography that identifies regions of stability, pattern formation, and chaos. The Derrida slope (asymptotic Hamming distance between perturbed replicas) serves as the chaos indicator. Eight analytical phase boundaries derived from linear stability analysis are shown to accurately predict the observed dynamical regimes.
    </div>

    <h2>Code</h2>

    <div class="code-wrap">
        <div class="code-toolbar">
            <span class="code-filename">spectral_cartography.py</span>
            <button class="copy-btn" onclick="copyCode(this)">Copy</button>
        </div>
        <div class="code-scroll">
<pre id="code-block"
><span class="cm"># -*- coding: utf-8 -*-
"""
Full Analysis Suite for Spatial 2x2 Games: Derrida Slopes, Frequencies, and Phase Boundaries
--------------------------------------------------------------------------------------------
Features:
1. "Dual Calculator": Simulates two replicas to measure both evolutionary outcome (f_infty)
   and dynamical chaos (d_infty / Hamming distance).
2. Optimized Core: Uses Numba JIT with fastmath and manual loop unrolling for maximum speed.
3. Smart Stopping: Auto-detects frozen states to skip unnecessary computation in stable regions.
4. Theory Overlay: Plots the 8 analytical phase boundaries derived in the paper.
"""</span>

<span class="kw">import</span> numpy <span class="kw">as</span> np
<span class="kw">import</span> matplotlib.pyplot <span class="kw">as</span> plt
<span class="kw">from</span> tqdm <span class="kw">import</span> tqdm
<span class="kw">import</span> multiprocessing <span class="kw">as</span> mp
<span class="kw">from</span> numba <span class="kw">import</span> njit
<span class="kw">import</span> os

<span class="cm"># =============================================================================
# 1. OPTIMIZED CORE CA MODEL (Numba JIT)
# =============================================================================</span>

<span class="dc">@njit</span>(fastmath=<span class="kw">True</span>)
<span class="kw">def</span> <span class="fn">calculate_payoffs</span>(grid, pm, pay):
    <span class="st">"""
    Calculates payoffs for the Von Neumann neighborhood with periodic boundaries.
    """</span>
    rows, cols = grid.shape
    <span class="kw">for</span> i <span class="kw">in</span> range(rows):
        up   = (i - <span class="nm">1</span>) <span class="kw">if</span> i > <span class="nm">0</span> <span class="kw">else</span> rows - <span class="nm">1</span>
        down = (i + <span class="nm">1</span>) <span class="kw">if</span> i < rows - <span class="nm">1</span> <span class="kw">else</span> <span class="nm">0</span>
        <span class="kw">for</span> j <span class="kw">in</span> range(cols):
            left  = (j - <span class="nm">1</span>) <span class="kw">if</span> j > <span class="nm">0</span> <span class="kw">else</span> cols - <span class="nm">1</span>
            right = (j + <span class="nm">1</span>) <span class="kw">if</span> j < cols - <span class="nm">1</span> <span class="kw">else</span> <span class="nm">0</span>
            me = grid[i, j]
            score = <span class="nm">0.0</span>
            score += pm[me, grid[up,   j]]
            score += pm[me, grid[down, j]]
            score += pm[me, grid[i, left]]
            score += pm[me, grid[i, right]]
            pay[i, j] = score

<span class="dc">@njit</span>(fastmath=<span class="kw">True</span>)
<span class="kw">def</span> <span class="fn">update_grid</span>(grid, pay, new_grid):
    <span class="st">"""
    Deterministic 'Imitate-the-Best' rule.
    Returns True if the grid changed, False if frozen.
    """</span>
    rows, cols = grid.shape
    changed = <span class="kw">False</span>
    <span class="kw">for</span> i <span class="kw">in</span> range(rows):
        up   = (i - <span class="nm">1</span>) <span class="kw">if</span> i > <span class="nm">0</span> <span class="kw">else</span> rows - <span class="nm">1</span>
        down = (i + <span class="nm">1</span>) <span class="kw">if</span> i < rows - <span class="nm">1</span> <span class="kw">else</span> <span class="nm">0</span>
        <span class="kw">for</span> j <span class="kw">in</span> range(cols):
            left  = (j - <span class="nm">1</span>) <span class="kw">if</span> j > <span class="nm">0</span> <span class="kw">else</span> cols - <span class="nm">1</span>
            right = (j + <span class="nm">1</span>) <span class="kw">if</span> j < cols - <span class="nm">1</span> <span class="kw">else</span> <span class="nm">0</span>
            best_s = grid[i, j]
            best_p = pay[i, j]
            <span class="kw">if</span> pay[up,   j] > best_p: best_p = pay[up,   j]; best_s = grid[up,   j]
            <span class="kw">if</span> pay[down, j] > best_p: best_p = pay[down, j]; best_s = grid[down, j]
            <span class="kw">if</span> pay[i, left]  > best_p: best_p = pay[i, left];  best_s = grid[i, left]
            <span class="kw">if</span> pay[i, right] > best_p: best_p = pay[i, right]; best_s = grid[i, right]
            <span class="kw">if</span> best_s != grid[i, j]: changed = <span class="kw">True</span>
            new_grid[i, j] = best_s
    <span class="kw">return</span> changed

<span class="dc">@njit</span>(fastmath=<span class="kw">True</span>)
<span class="kw">def</span> <span class="fn">evolve_and_measure</span>(grid1, grid2, pm, max_steps=<span class="nm">2000</span>, sample_steps=<span class="nm">100</span>):
    <span class="st">"""
    Evolves two replicas simultaneously.
    - grid1: Main simulation for Frequency.
    - grid2: Perturbed copy for Hamming Distance.
    Returns: (Average Cooperator Frequency, Average Hamming Distance)
    """</span>
    rows, cols = grid1.shape
    N = <span class="fn">float</span>(rows * cols)
    pay1 = np.zeros(grid1.shape, dtype=np.float64)
    pay2 = np.zeros(grid2.shape, dtype=np.float64)
    new1 = np.zeros(grid1.shape, dtype=np.int8)
    new2 = np.zeros(grid2.shape, dtype=np.int8)
    avg_freq = <span class="nm">0.0</span>
    avg_ham  = <span class="nm">0.0</span>
    burn_in  = max_steps - sample_steps

    <span class="kw">for</span> t <span class="kw">in</span> range(max_steps):
        <span class="fn">calculate_payoffs</span>(grid1, pm, pay1)
        <span class="fn">calculate_payoffs</span>(grid2, pm, pay2)
        c1 = <span class="fn">update_grid</span>(grid1, pay1, new1)
        c2 = <span class="fn">update_grid</span>(grid2, pay2, new2)
        grid1[:] = new1[:]
        grid2[:] = new2[:]
        current_f = <span class="nm">1.0</span> - (np.sum(grid1) / N)
        current_d = np.sum(grid1 != grid2) / N
        <span class="kw">if</span> t >= burn_in:
            avg_freq += current_f
            avg_ham  += current_d
        <span class="kw">if</span> (<span class="kw">not</span> c1) <span class="kw">and</span> (<span class="kw">not</span> c2):
            steps_in_window_so_far    = <span class="fn">max</span>(<span class="nm">0</span>, t - burn_in + <span class="nm">1</span>)
            steps_remaining_in_window = sample_steps - steps_in_window_so_far
            <span class="kw">if</span> steps_remaining_in_window > <span class="nm">0</span>:
                avg_freq += current_f * steps_remaining_in_window
                avg_ham  += current_d * steps_remaining_in_window
            <span class="kw">break</span>

    <span class="kw">return</span> avg_freq / sample_steps, avg_ham / sample_steps

<span class="kw">def</span> <span class="fn">create_payoff_matrix</span>(u, v):
    <span class="st">"""R=1, P=0, T=1+u, S=v. Index 0=Coop, 1=Defect."""</span>
    <span class="kw">return</span> np.array([[<span class="nm">1.0</span>, v], [<span class="nm">1.0</span>+u, <span class="nm">0.0</span>]], dtype=np.float64)

<span class="cm"># =============================================================================
# 2. PARALLEL PARAMETER SCANNING
# =============================================================================</span>

<span class="kw">def</span> <span class="fn">one_point</span>(args):
    <span class="st">"""Worker function for a single (u,v) point."""</span>
    i, j, u, v, seed, grid_size, fC0 = args
    rng   = np.random.default_rng(seed)
    grid1 = (rng.random((grid_size, grid_size)) >= fC0).astype(np.int8)
    grid2 = grid1.copy()
    rx, ry = rng.integers(<span class="nm">0</span>, grid_size, <span class="nm">2</span>)
    grid2[rx, ry] = <span class="nm">1</span> - grid2[rx, ry]
    pm = <span class="fn">create_payoff_matrix</span>(u, v)
    f_final, d_final = <span class="fn">evolve_and_measure</span>(grid1, grid2, pm)
    <span class="kw">return</span> i, j, f_final, d_final

<span class="kw">def</span> <span class="fn">scan_plane</span>(u_vals, v_vals, fC0, grid_size=<span class="nm">50</span>, replicates=<span class="nm">5</span>, master_seed=<span class="nm">42</span>):
    num_cores = mp.cpu_count()
    map_freq  = np.zeros((<span class="fn">len</span>(v_vals), <span class="fn">len</span>(u_vals)))
    map_ham   = np.zeros((<span class="fn">len</span>(v_vals), <span class="fn">len</span>(u_vals)))
    tasks = []
    <span class="kw">for</span> i, u <span class="kw">in</span> <span class="fn">enumerate</span>(u_vals):
        <span class="kw">for</span> j, v <span class="kw">in</span> <span class="fn">enumerate</span>(v_vals):
            <span class="kw">for</span> rep <span class="kw">in</span> range(replicates):
                seed = (master_seed + i*<span class="nm">7919</span> + j*<span class="nm">104729</span> + rep*<span class="nm">9973</span>) % (<span class="nm">2</span>**<span class="nm">32</span>)
                tasks.append((i, j, u, v, seed, grid_size, fC0))
    <span class="fn">print</span>(<span class="st">f"Scanning fC0=</span>{fC0}<span class="st"> on </span>{num_cores}<span class="st"> cores..."</span>)
    <span class="kw">with</span> mp.Pool(num_cores) <span class="kw">as</span> pool:
        <span class="kw">for</span> i, j, f, d <span class="kw">in</span> <span class="fn">tqdm</span>(pool.imap_unordered(<span class="fn">one_point</span>, tasks, chunksize=<span class="nm">5</span>), total=<span class="fn">len</span>(tasks)):
            map_freq[j, i] += f / replicates
            map_ham[j,  i] += d / replicates
    <span class="kw">return</span> map_freq, map_ham

<span class="cm"># =============================================================================
# 3. PLOTTING & THEORY OVERLAY
# =============================================================================</span>

<span class="kw">def</span> <span class="fn">add_theoretical_lines</span>(ax, u_vals):
    <span class="st">"""Overlay analytical phase boundaries."""</span>
    ax.plot(u_vals,  <span class="nm">4</span>*u_vals + <span class="nm">1</span>,     <span class="st">"k-"</span>,  lw=<span class="nm">1.0</span>, alpha=<span class="nm">0.8</span>, label=<span class="st">r"Global Inv. (D): $v=4u+1$"</span>)
    ax.plot(u_vals,  <span class="nm">0.25</span>*u_vals + <span class="nm">0.25</span>, <span class="st">"k--"</span>, lw=<span class="nm">1.0</span>, alpha=<span class="nm">0.8</span>, label=<span class="st">r"Global Inv. (C): $v=0.25u+0.25$"</span>)
    ax.plot(u_vals,  <span class="nm">2</span>*u_vals - <span class="nm">1</span>,      <span class="st">"r-"</span>,  lw=<span class="nm">1.2</span>,              label=<span class="st">r"Stripe Unzipping: $v=2u-1$"</span>)
    ax.plot(u_vals,  u_vals,              <span class="st">"b--"</span>, lw=<span class="nm">1.0</span>, alpha=<span class="nm">0.7</span>, label=<span class="st">r"Checkerboard Eq.: $v=u$"</span>)
    ax.plot(u_vals,  <span class="nm">0.5</span>*u_vals - <span class="nm">0.5</span>,  <span class="st">"m:"</span>,  lw=<span class="nm">1.2</span>,              label=<span class="st">r"Block Stability: $v=0.5u-0.5$"</span>)
    ax.plot(u_vals,  u_vals + <span class="nm">2</span>/<span class="nm">3</span>,       <span class="st">"c:"</span>,  lw=<span class="nm">1.2</span>,              label=<span class="st">r"Domino/Kink: $v=u+2/3$"</span>)
    ax.plot(u_vals,  u_vals/<span class="nm">3</span>,           <span class="st">"g-."</span>, lw=<span class="nm">1.2</span>,              label=<span class="st">r"Filament Nucleation: $v=u/3$"</span>)
    ax.axvline(x=<span class="nm">1</span>/<span class="nm">3</span>, color=<span class="st">'purple'</span>, linestyle=<span class="st">'-.'</span>, lw=<span class="nm">1.2</span>, alpha=<span class="nm">0.8</span>, label=<span class="st">r"Core Erosion: $u=1/3$"</span>)
    ax.set_xlim(-<span class="nm">1</span>, <span class="nm">1</span>); ax.set_ylim(-<span class="nm">1</span>, <span class="nm">1</span>)
    ax.legend(fontsize=<span class="nm">6</span>, loc=<span class="st">'upper left'</span>, frameon=<span class="kw">True</span>, framealpha=<span class="nm">0.9</span>, ncol=<span class="nm">2</span>)

<span class="cm"># =============================================================================
# 4. MAIN EXECUTION
# =============================================================================</span>

<span class="kw">if</span> __name__ == <span class="st">'__main__'</span>:
    RES  = <span class="nm">400</span>   <span class="cm"># Resolution (400x400 pixels)</span>
    GRID = <span class="nm">50</span>    <span class="cm"># Lattice size (50x50 sites)</span>
    REPS = <span class="nm">30</span>    <span class="cm"># Replicates per pixel</span>
    U = np.linspace(-<span class="nm">1.0</span>, <span class="nm">1.0</span>, RES)
    V = np.linspace(-<span class="nm">1.0</span>, <span class="nm">1.0</span>, RES)
    os.makedirs(<span class="st">"results"</span>, exist_ok=<span class="kw">True</span>)

    <span class="kw">for</span> fC0 <span class="kw">in</span> [<span class="nm">0.01</span>]:
        <span class="fn">print</span>(<span class="st">f"\n--- Processing Initial Cooperator Freq: </span>{fC0}<span class="st"> ---"</span>)
        freq_map, ham_map = <span class="fn">scan_plane</span>(U, V, fC0, grid_size=GRID, replicates=REPS)
        np.save(<span class="st">f"results/ham_map001.npy"</span>, freq_map)

        <span class="cm"># Frequency plot</span>
        fig1, ax1 = plt.subplots(figsize=(<span class="nm">10</span>, <span class="nm">8</span>))
        pcm1 = ax1.pcolormesh(U, V, freq_map, shading=<span class="st">'auto'</span>, cmap=<span class="st">'viridis'</span>, vmin=<span class="nm">0</span>, vmax=<span class="nm">1</span>)
        fig1.colorbar(pcm1, label=<span class="st">r'Final Cooperator Frequency $f_\infty$'</span>)
        ax1.set_title(<span class="st">f"Final Frequency Map (Initial $f_C=</span>{fC0}<span class="st">$)"</span>)
        ax1.set_xlabel(<span class="st">r'Temptation $u$'</span>); ax1.set_ylabel(<span class="st">r"Sucker's Payoff $v$"</span>)
        <span class="fn">add_theoretical_lines</span>(ax1, U)
        plt.tight_layout()
        plt.savefig(<span class="st">f"results/freq_map_fc</span>{fC0}<span class="st">.png"</span>, dpi=<span class="nm">300</span>)
        plt.close(fig1)

        <span class="cm"># Hamming distance (chaos) plot</span>
        fig2, ax2 = plt.subplots(figsize=(<span class="nm">10</span>, <span class="nm">8</span>))
        pcm2 = ax2.pcolormesh(U, V, ham_map, shading=<span class="st">'auto'</span>, cmap=<span class="st">'inferno'</span>, vmin=<span class="nm">0</span>, vmax=<span class="nm">0.5</span>)
        fig2.colorbar(pcm2, label=<span class="st">r'Asymptotic Hamming Distance $d_\infty$'</span>)
        ax2.set_title(<span class="st">f"Chaos Map / Asymptotic Distance (Initial $f_C=</span>{fC0}<span class="st">$)"</span>)
        ax2.set_xlabel(<span class="st">r'Temptation $u$'</span>); ax2.set_ylabel(<span class="st">r"Sucker's Payoff $v$"</span>)
        <span class="fn">add_theoretical_lines</span>(ax2, U)
        plt.tight_layout()
        plt.savefig(<span class="st">f"results/ham_map_fc</span>{fC0}<span class="st">.png"</span>, dpi=<span class="nm">300</span>)
        plt.close(fig2)

    <span class="fn">print</span>(<span class="st">"\nDone! All results saved to /results folder."</span>)</pre>
        </div>
    </div>

    <div style="margin-top:12px;">
        <strong style="font-size:0.85rem;color:var(--text-mid);">Dependencies</strong>
        <div class="dep-list">
            <span class="dep">numpy</span>
            <span class="dep">numba</span>
            <span class="dep">matplotlib</span>
            <span class="dep">tqdm</span>
            <span class="dep">python ≥ 3.8</span>
        </div>
    </div>

    <h2>Data</h2>
    <div class="card">
        <div class="card-icon icon-data">
            <svg viewBox="0 0 16 16" fill="currentColor"><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2zm2 0v12h8V2H4zm1 2h6v1H5V4zm0 2h6v1H5V6zm0 2h4v1H5V8z"/></svg>
        </div>
        <div class="card-body">
            <div class="card-title">spectral_cartography_data.zip</div>
            <div class="card-desc">Parameter sweep results (.npy arrays), frequency maps, and chaos maps for all initial conditions reported in the paper.</div>
            <a class="dl-btn btn-data" href="spectral_cartography_data.zip" download>
                <svg viewBox="0 0 16 16" fill="currentColor"><path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"/><path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"/></svg>
                Download .zip
            </a>
        </div>
    </div>

    <h2>Paper</h2>
    <div class="card">
        <div class="card-icon icon-pdf">
            <svg viewBox="0 0 16 16" fill="currentColor"><path d="M14 14V4.5L9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2zM9.5 3A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5v2z"/></svg>
        </div>
        <div class="card-body">
            <div class="card-title">Preprint PDF</div>
            <div class="card-desc">Under review. Please cite the preprint version until the journal version is available.</div>
            <a class="dl-btn btn-pdf" href="../papers/spectral_cartography.pdf" target="_blank">
                <svg viewBox="0 0 16 16" fill="currentColor"><path d="M14 14V4.5L9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2zM9.5 3A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5v2z"/></svg>
                View PDF
            </a>
        </div>
    </div>

    <h2>Citation</h2>
    <div class="cite-box">Aydogmus, O. H. (2025). From Local Payoffs to Global Instabilities: A Spectral Cartography of Spatiotemporal Chaos in Canonical 2×2 Evolutionary Games. <em>Manuscript under review.</em></div>

</div>

<script>
function copyCode(btn) {
    const pre = document.getElementById('code-block');
    navigator.clipboard.writeText(pre.innerText).then(() => {
        btn.textContent = 'Copied!';
        btn.classList.add('copied');
        setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 2000);
    });
}
</script>

</body>
</html>
