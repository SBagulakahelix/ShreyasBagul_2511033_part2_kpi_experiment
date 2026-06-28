import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

project_dir = r"C:\Users\bagul\OneDrive\Desktop\assignment\shreyasbagul_2511033_part2_kpi_experiment"
out_path = os.path.join(project_dir, "outputs", "kpi_tree.png")
preview_path = os.path.join(project_dir, "screenshots", "kpi_tree.png")

# Ensure folders exist
os.makedirs(os.path.dirname(out_path), exist_ok=True)
os.makedirs(os.path.dirname(preview_path), exist_ok=True)

# Configure Matplotlib styles
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'DejaVu Sans']

# Setup Figure
fig, ax = plt.subplots(figsize=(15, 9), dpi=200)
ax.set_xlim(-8, 8)
ax.set_ylim(-1, 5)
ax.axis('off')

# Style Constants
color_ns = '#1F4E79'   # Deep Steel Blue for North Star
color_dr = '#2F5597'   # Medium Steel Blue for Drivers
color_sub = '#DDEBF7'  # Very Light Blue for Sub-drivers
color_gr = '#FCE4D6'   # Soft Red/Orange for Guardrails
text_dark = '#333333'
text_light = '#FFFFFF'
border_color = '#7F7F7F'

# Helper function to draw a box
def draw_box(x, y, w, h, text, facecolor, textcolor=text_dark, is_bold=False):
    rect = patches.FancyBboxPatch(
        (x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.1",
        facecolor=facecolor,
        edgecolor=border_color,
        linewidth=1.2,
        mutation_scale=0.4
    )
    ax.add_patch(rect)
    
    # Split text into lines for multi-line boxes
    lines = text.split('\n')
    num_lines = len(lines)
    y_starts = [y + (num_lines - 1 - 2*i)*0.08 for i in range(num_lines)] if num_lines > 1 else [y]
    
    for line, y_pos in zip(lines, y_starts):
        ax.text(
            x, y_pos, line,
            ha='center', va='center',
            fontsize=8.5, weight='bold' if is_bold else 'normal',
            color=textcolor
        )

# Helper function to draw an arrow
def draw_arrow(x_start, y_start, x_end, y_end):
    ax.annotate(
        '', xy=(x_end, xy_y_offset(y_end, 'end')), xytext=(x_start, xy_y_offset(y_start, 'start')),
        arrowprops=dict(arrowstyle="->", color=border_color, lw=1.2, shrinkA=5, shrinkB=5)
    )

def xy_y_offset(y, direction):
    # Adjust arrow positions to touch box edges
    if direction == 'start':
        return y - 0.2
    else:
        return y + 0.2

# 1. Title Block
ax.text(0, 4.7, "BUSINESS KPI FRAMEWORK & EXPERIMENT TREE", fontsize=15, weight='bold', color='#1F4E79', ha='center')
ax.text(0, 4.5, "Subscription Product Onboarding Experiment - Shreyas Bagul (ID: 2511033)", fontsize=10, fontstyle='italic', color='#595959', ha='center')

# 2. NORTH STAR METRIC (Level 4)
draw_box(0, 3.8, 3.0, 0.5, "NORTH STAR METRIC\nPaid Conversion Rate\n(Converted Users / Total Users)", color_ns, text_light, is_bold=True)

# 3. PRIMARY DRIVERS (Level 3)
draw_box(-4.5, 2.7, 2.5, 0.45, "1. Trial Acquisition\nTrial Start Rate\n(Trial Users / Total Users)", color_dr, text_light, is_bold=True)
draw_box(0, 2.7, 2.5, 0.45, "2. Early Activation\nOnboarding Completion Rate\n(Completed / Total Users)", color_dr, text_light, is_bold=True)
draw_box(4.5, 2.7, 2.5, 0.45, "3. Monetization Quality\nPaid Upgrade Rate\n(Paid Users / Trial Users)", color_dr, text_light, is_bold=True)

# Draw arrows from North Star to Drivers
draw_arrow(0, 3.8, -4.5, 2.7)
draw_arrow(0, 3.8, 0, 2.7)
draw_arrow(0, 3.8, 4.5, 2.7)

# 4. SUB-DRIVERS (Level 2)
# Under Trial Acquisition
draw_box(-5.8, 1.5, 2.1, 0.4, "1.1. Landing Page Visit Rate\n(Visits / Total Users)", color_sub, text_dark)
draw_box(-3.2, 1.5, 2.1, 0.4, "1.2. Trial Signup CTR\n(Trial Starts / Visits)", color_sub, text_dark)
draw_arrow(-4.5, 2.7, -5.8, 1.5)
draw_arrow(-4.5, 2.7, -3.2, 1.5)

# Under Early Activation
draw_box(-1.3, 1.5, 2.1, 0.4, "2.1. Completion CTR\n(Completed / Trial Starts)", color_sub, text_dark)
draw_box(1.3, 1.5, 2.1, 0.4, "2.2. Engagement Score\n(Average Activity)", color_sub, text_dark)
draw_arrow(0, 2.7, -1.3, 1.5)
draw_arrow(0, 2.7, 1.3, 1.5)

# Under Monetization Quality
draw_box(3.2, 1.5, 2.1, 0.4, "3.1. Plan Upgrade Mix\n(Basic vs Premium Tiers)", color_sub, text_dark)
draw_box(5.8, 1.5, 2.1, 0.4, "3.2. Conversion Speed\n(Average Days to Convert)", color_sub, text_dark)
draw_arrow(4.5, 2.7, 3.2, 1.5)
draw_arrow(4.5, 2.7, 5.8, 1.5)

# 5. GUARDRAIL METRICS (Bottom Level)
# Header for Guardrails
rect_gr_hdr = patches.Rectangle((-7.8, -0.6), 15.6, 1.4, fill=False, edgecolor='#A6A6A6', linestyle='--', linewidth=1.2)
ax.add_patch(rect_gr_hdr)
ax.text(-7.6, 0.6, "GUARDRAIL METRICS (Risk, Cost & Revenue Quality Control)", fontsize=10, weight='bold', color='#C0392B')

draw_box(-4.5, -0.1, 2.6, 0.45, "Guardrail 1: Support Ticket Rate\n(Tickets Raised / Total Users)\n- Target: Keep low (< 15%)", color_gr, text_dark, is_bold=True)
draw_box(0, -0.1, 2.6, 0.45, "Guardrail 2: Refund Requested Rate\n(Refund Requests / Total Users)\n- Target: Keep low (< 0.5%)", color_gr, text_dark, is_bold=True)
draw_box(4.5, -0.1, 2.6, 0.45, "Guardrail 3: Revenue Quality (ARPU)\n(Revenue / Total Users)\n- Target: Maintain/Grow ARPU", color_gr, text_dark, is_bold=True)

# Add dotted connection from drivers/sub-drivers to guardrails
# Just visually showing they monitor the system
plt.tight_layout()

# Save image
print(f"Saving KPI tree image to {out_path}...")
plt.savefig(out_path, bbox_inches='tight')
print(f"Saving KPI tree preview image to {preview_path}...")
plt.savefig(preview_path, bbox_inches='tight')
plt.close()
print("KPI tree images saved successfully!")
