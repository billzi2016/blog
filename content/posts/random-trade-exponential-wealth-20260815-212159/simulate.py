import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), dpi=300)

N = 2000          # 人口规模
M = 2000          # 总财富
m_avg = M / N      # 平均财富
rounds = 1500     # 轮数，每轮随机配对 N/2 组，共 N/2 * 1500 = 150 万次交易

np.random.seed(42)

# 1. 标准无偏随机交易模型 (Vectorized)
wealth1 = np.ones(N) * m_avg
for _ in range(rounds):
    perm = np.random.permutation(N)
    i_idx, j_idx = perm[:N//2], perm[N//2:]
    totals = wealth1[i_idx] + wealth1[j_idx]
    r = np.random.random(N//2)
    wealth1[i_idx] = r * totals
    wealth1[j_idx] = (1 - r) * totals

# 2. 储蓄率交易模型 (lambda = 0.3)
lambda_save = 0.3
wealth2 = np.ones(N) * m_avg
for _ in range(rounds):
    perm = np.random.permutation(N)
    i_idx, j_idx = perm[:N//2], perm[N//2:]
    pools = (1 - lambda_save) * (wealth2[i_idx] + wealth2[j_idx])
    r = np.random.random(N//2)
    wealth2[i_idx] = lambda_save * wealth2[i_idx] + r * pools
    wealth2[j_idx] = lambda_save * wealth2[j_idx] + (1 - r) * pools

# 3. Yard-Sale 财富凝聚模型 (按较贫者 10% 资产比率下注)
wealth3 = np.ones(N) * m_avg
f = 0.1
for _ in range(rounds):
    perm = np.random.permutation(N)
    i_idx, j_idx = perm[:N//2], perm[N//2:]
    min_w = np.minimum(wealth3[i_idx], wealth3[j_idx])
    dw = f * min_w
    wins = np.random.random(N//2) < 0.5
    wealth3[i_idx] += np.where(wins, dw, -dw)
    wealth3[j_idx] += np.where(wins, -dw, dw)

# --- 子图 1: 标准模型 vs 玻尔兹曼-吉布斯理论曲线 ---
ax1 = axes[0]
ax1.hist(wealth1, bins=40, density=True, alpha=0.6, color='#1f77b4', edgecolor='white', label='Monte Carlo Sim')
x = np.linspace(0, max(wealth1), 200)
y_theory = (1.0 / m_avg) * np.exp(-x / m_avg)
ax1.plot(x, y_theory, 'r--', linewidth=2, label=r'Theory: $P(m)=\frac{1}{\bar{m}}e^{-m/\bar{m}}$')
ax1.set_title('Standard Model (Boltzmann-Gibbs)', fontsize=12, fontweight='bold', pad=10)
ax1.set_xlabel('Wealth (m)', fontsize=10)
ax1.set_ylabel('Probability Density', fontsize=10)
ax1.legend(frameon=True, facecolor='white', edgecolor='none')
ax1.grid(True, linestyle=':', alpha=0.5)

# --- 子图 2: 储蓄保护机制 vs 纯指数分布 ---
ax2 = axes[1]
ax2.hist(wealth2, bins=40, density=True, alpha=0.6, color='#2ca02c', edgecolor='white', label=r'Saving $\lambda=0.3$')
ax2.plot(x, y_theory, color='gray', linestyle=':', linewidth=1.5, label=r'Exponential ($\lambda=0$)')
ax2.set_title('Saving Model (Middle Class Emergence)', fontsize=12, fontweight='bold', pad=10)
ax2.set_xlabel('Wealth (m)', fontsize=10)
ax2.set_ylabel('Probability Density', fontsize=10)
ax2.legend(frameon=True, facecolor='white', edgecolor='none')
ax2.grid(True, linestyle=':', alpha=0.5)

# --- 子图 3: 洛伦兹曲线对比 ---
ax3 = axes[2]
sorted_w3 = np.sort(wealth3)
cum_w3 = np.cumsum(sorted_w3) / np.sum(sorted_w3)
pop_frac = np.linspace(0, 1, N)
L_theory = pop_frac + (1 - pop_frac) * np.log(np.maximum(1 - pop_frac, 1e-10))

ax3.plot(pop_frac, pop_frac, 'k--', alpha=0.4, label='Perfect Equality (G=0)')
ax3.plot(pop_frac, L_theory, color='#1f77b4', linestyle='-.', linewidth=1.8, label='Standard Model (G=0.5)')
ax3.plot(pop_frac, cum_w3, color='#d62728', linewidth=2, label='Yard-Sale (G → 1.0)')
ax3.set_title('Lorenz Curve Comparison', fontsize=12, fontweight='bold', pad=10)
ax3.set_xlabel('Cumulative Population Share', fontsize=10)
ax3.set_ylabel('Cumulative Wealth Share', fontsize=10)
ax3.legend(frameon=True, facecolor='white', edgecolor='none')
ax3.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'random_trade_simulation.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Successfully generated {output_path}")

