import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os

project_dir = r"C:\Users\bagul\OneDrive\Desktop\assignment\shreyasbagul_2511033_part2_kpi_experiment"
output_image = os.path.join(project_dir, "screenshots", "hypothesis_test_preview.png")

# Ensure folder exists
os.makedirs(os.path.dirname(output_image), exist_ok=True)

# Configure Matplotlib styles
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'DejaVu Sans']

# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), dpi=150)

# ==========================================
# Plot 1: Standard Normal Curve & Rejection Region (Conversion Z-Test)
# ==========================================
z_stat = 3.264
alpha = 0.05
z_crit = norm.ppf(1 - alpha) # One-tailed critical value (~1.645)

# Normal curve values
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

ax1.plot(x, y, color='#1F4E79', lw=2, label='Null Hypothesis Distribution (H0)')

# Fill rejection region
x_reject = np.linspace(z_crit, 4, 200)
y_reject = norm.pdf(x_reject)
ax1.fill_between(x_reject, y_reject, color='#C0392B', alpha=0.3, label=f'Rejection Region (alpha = {alpha})')

# Mark critical value
ax1.axvline(z_crit, color='#C0392B', linestyle='--', lw=1.5)
ax1.text(z_crit - 0.1, 0.25, f'Critical Z = {z_crit:.3f}\n(alpha = 0.05)', color='#C0392B', ha='right', weight='bold', fontsize=9)

# Mark our test statistic
ax1.axvline(z_stat, color='#2E7D32', linestyle='-', lw=2)
ax1.text(z_stat + 0.1, 0.15, f'Actual Z = {z_stat:.3f}\np-value = 0.00055\n(Significant!)', color='#2E7D32', ha='left', weight='bold', fontsize=9)
ax1.plot(z_stat, norm.pdf(z_stat), 'o', color='#2E7D32', markersize=8)

# Styling Plot 1
ax1.set_title("Paid Conversion Rate Z-Test Distribution", fontsize=12, weight='bold', color='#1F4E79')
ax1.set_xlabel("Z-Score", fontsize=10)
ax1.set_ylabel("Probability Density", fontsize=10)
ax1.legend(loc='upper left', fontsize=9)
ax1.grid(True, linestyle=':', alpha=0.5)

# ==========================================
# Plot 2: Text summary of inputs and outputs
# ==========================================
ax2.axis('off')

text_box = (
    "HYPOTHESIS TEST RESULTS SUMMARY\n\n"
    "1. PAID CONVERSION RATE TEST (North Star)\n"
    "   - Test Type: Two-Proportion Z-Test (One-tailed)\n"
    "   - Control N = 690, Converted = 22 (Conversion Rate = 3.19%)\n"
    "   - Treatment N = 710, Converted = 50 (Conversion Rate = 7.04%)\n"
    "   - Absolute Conversion Lift: +3.85% (Relative Lift: +120.88%)\n"
    "   - Z-Statistic: 3.2640\n"
    "   - P-Value: 0.000549 (Highly Significant, p < 0.01)\n"
    "   - Decision: Reject Null Hypothesis (H0). Treatment leads to significant lift.\n\n"
    "2. OPERATIONAL GUARDRAIL: SUPPORT TICKET RATE\n"
    "   - Test Type: Two-Proportion Z-Test (Two-tailed)\n"
    "   - Control N = 690, Tickets = 102 (Rate = 14.78%)\n"
    "   - Treatment N = 710, Tickets = 176 (Rate = 24.79%)\n"
    "   - Absolute Ticket Rate Increase: +10.01% (Relative: +67.70%)\n"
    "   - Z-Statistic: 4.6921\n"
    "   - P-Value: 0.000003 (Highly Significant, p < 0.001)\n"
    "   - Risk Alert: Significant increase in customer support volume and friction.\n\n"
    "3. REVENUE QUALITY (ARPU) WITH & WITHOUT OUTLIERS\n"
    "   - Welch's t-test (Full data): t-stat = 0.1122, p-value = 0.9107 (Not Significant)\n"
    "   - Welch's t-test (No Outliers): t-stat = 2.4304, p-value = 0.0152 (Significant, p < 0.05)\n"
    "   - Control ARPU (no outliers): $24.13 | Treatment ARPU (no outliers): $50.58\n"
    "   - Insight: Control revenue was skewed by 3 extreme outliers ($8.6k, $6.7k, $3.8k).\n"
    "              Treatment drove consistent, healthy monetization across users."
)

props = dict(boxstyle='round,pad=0.8', facecolor='#F8F9FA', edgecolor='#D9D9D9', alpha=1.0)
ax2.text(0.05, 0.95, text_box, transform=ax2.transAxes, fontsize=8.5, verticalalignment='top', bbox=props, fontfamily='monospace')

plt.suptitle("Onboarding Experiment A/B Test Output - Shreyas Bagul (ID: 2511033)", fontsize=14, weight='bold', color='#1F4E79')
plt.tight_layout()

# Save image
print(f"Saving hypothesis test screenshot to {output_image}...")
plt.savefig(output_image, bbox_inches='tight')
plt.close()
print("Hypothesis test screenshot generated successfully!")
