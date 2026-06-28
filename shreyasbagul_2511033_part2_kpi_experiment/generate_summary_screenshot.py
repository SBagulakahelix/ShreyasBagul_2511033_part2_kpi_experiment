import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

project_dir = r"C:\Users\bagul\OneDrive\Desktop\assignment\shreyasbagul_2511033_part2_kpi_experiment"
output_image = os.path.join(project_dir, "screenshots", "experiment_summary_preview.png")

# Ensure folder exists
os.makedirs(os.path.dirname(output_image), exist_ok=True)

# Configure Matplotlib styles
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'DejaVu Sans']

# Setup data
metrics_data = [
    ["User Count", "690", "710", "+20", "+2.90%"],
    ["Landing Page Visit Rate", "63.62%", "72.39%", "+8.77%", "+13.78%"],
    ["Trial Start Rate", "25.07%", "29.01%", "+3.94%", "+15.71%"],
    ["Onboarding Completion Rate", "15.65%", "21.13%", "+5.48%", "+35.04%"],
    ["Paid Conversion Rate (North Star)", "3.19%", "7.04%", "+3.85%", "+120.88%"],
    ["Average Revenue Per User (ARPU)", "$51.97", "$54.25", "+$2.28", "+4.39%"],
    ["ARPU (Excluding Outliers)", "$24.13", "$50.58", "+$26.45", "+109.61%"],
    ["Average Revenue Per Converted User", "$1,630.10", "$770.41", "-$859.69", "-52.74%"],
    ["Refund Rate (Guardrail)", "0.00%", "0.42%", "+0.42%", "-"],
    ["Support Ticket Rate (Guardrail)", "14.78%", "24.79%", "+10.01%", "+67.70%"],
    ["Average Engagement Score", "57.03", "62.94", "+5.91", "+10.36%"],
    ["Average Days to Convert", "8.86 days", "6.40 days", "-2.46 days", "-27.77%"]
]

columns = ["Experiment Metric", "Control Group", "Treatment Group", "Absolute Diff", "Percentage Lift"]

# Draw Table
fig, ax = plt.subplots(figsize=(14, 8), dpi=150)
ax.axis('off')
ax.axis('tight')

table = ax.table(
    cellText=metrics_data, 
    colLabels=columns, 
    loc='center', 
    cellLoc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.0, 1.5)

# Styling Constants
header_color = '#1F4E79'   # Deep Steel Blue
zebra_color = '#F2F2F2'    # Light Gray
white_color = '#FFFFFF'
border_color = '#D9D9D9'
highlight_color = '#E2EFDA' # Soft Green for lift
risk_color = '#FCE4D6'      # Soft Red/Orange for risk

# Style Cells
for (row_idx, col_idx), cell in table.get_celld().items():
    cell.set_edgecolor(border_color)
    if row_idx == 0:
        # Header row
        cell.set_text_props(weight='bold', color=white_color)
        cell.set_facecolor(header_color)
    else:
        # Data rows
        cell.set_text_props(weight='normal')
        
        # Zebra striping
        if row_idx % 2 == 0:
            cell.set_facecolor(zebra_color)
        else:
            cell.set_facecolor(white_color)
            
        # Highlight metrics
        metric_name = metrics_data[row_idx - 1][0]
        
        # Highlight lifts
        if col_idx == 4:
            lift_val = metrics_data[row_idx - 1][col_idx]
            if '+' in lift_val and "Support Ticket" not in metric_name and "Refund" not in metric_name:
                cell.set_facecolor(highlight_color)
                cell.set_text_props(weight='bold', color='#1E4620')
            elif '-' in lift_val and "Days to Convert" in metric_name:
                # Lower days to convert is good!
                cell.set_facecolor(highlight_color)
                cell.set_text_props(weight='bold', color='#1E4620')
            elif '+' in lift_val and ("Support Ticket" in metric_name or "Refund" in metric_name):
                # Higher ticket/refund is risk!
                cell.set_facecolor(risk_color)
                cell.set_text_props(weight='bold', color='#C0392B')
                
        # Bold first column
        if col_idx == 0:
            cell.set_text_props(weight='bold')
            cell.alignment = 'left'

plt.title("Control vs Treatment Key Metrics Summary Table", fontsize=14, weight='bold', color='#1F4E79', pad=20)
plt.tight_layout()

# Save image
print(f"Saving summary metrics image to {output_image}...")
plt.savefig(output_image, bbox_inches='tight')
plt.close()
print("Summary metrics image generated successfully!")
