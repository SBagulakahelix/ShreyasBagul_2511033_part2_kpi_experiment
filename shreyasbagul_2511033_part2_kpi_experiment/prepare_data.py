import pandas as pd
import numpy as np
import os

project_dir = r"C:\Users\bagul\OneDrive\Desktop\assignment\shreyasbagul_2511033_part2_kpi_experiment"
raw_path = os.path.join(project_dir, "data", "campaign_experiment_data.xlsx")
analysis_path = os.path.join(project_dir, "analysis", "experiment_analysis.xlsx")

print("--- Loading Experiment Data ---")
df = pd.read_excel(raw_path, sheet_name="experiment_data")
print(f"Original shape: {df.shape}")

# ==========================================
# 1. Drop Exact Duplicates
# ==========================================
dup_mask = df.duplicated()
print(f"Exact duplicate rows found: {dup_mask.sum()}")
df_clean = df.drop_duplicates().copy()
print(f"Shape after deduplication: {df_clean.shape}")

# Verify duplicate user IDs
dup_users = df_clean.duplicated(subset=['user_id']).sum()
print(f"Duplicate user_id counts in clean data: {dup_users}")

# ==========================================
# 2. Impute Missing Values
# ==========================================
# device_type -> 'Unknown'
device_nulls = df_clean['device_type'].isnull().sum()
df_clean.loc[df_clean['device_type'].isnull(), 'device_type'] = 'Unknown'
print(f"Imputed {device_nulls} missing device_type values with 'Unknown'")

# traffic_source -> 'Unknown'
traffic_nulls = df_clean['traffic_source'].isnull().sum()
df_clean.loc[df_clean['traffic_source'].isnull(), 'traffic_source'] = 'Unknown'
print(f"Imputed {traffic_nulls} missing traffic_source values with 'Unknown'")

# engagement_score -> Respective group median
engagement_nulls = df_clean['engagement_score'].isnull().sum()
if engagement_nulls > 0:
    for group in df_clean['experiment_group'].unique():
        median_val = df_clean[df_clean['experiment_group'] == group]['engagement_score'].median()
        mask = (df_clean['experiment_group'] == group) & (df_clean['engagement_score'].isnull())
        df_clean.loc[mask, 'engagement_score'] = median_val
    print(f"Imputed {engagement_nulls} missing engagement_score values with group-specific medians")

# days_to_convert: Keep missing values as null (represent non-converted users)
print(f"Remaining nulls in days_to_convert: {df_clean['days_to_convert'].isnull().sum()} (Non-converted users)")

# ==========================================
# 3. Validate Column Types & Values
# ==========================================
binary_cols = ['visited_landing_page', 'started_trial', 'completed_onboarding', 'converted_to_paid', 'refund_requested']
for col in binary_cols:
    invalid_mask = ~df_clean[col].isin([0, 1])
    invalid_count = invalid_mask.sum()
    print(f"Column '{col}' invalid binary values (not 0 or 1): {invalid_count}")

# Make sure support_tickets_30d is positive integer
invalid_tickets = (df_clean['support_tickets_30d'] < 0).sum()
print(f"Column 'support_tickets_30d' negative values: {invalid_tickets}")

# ==========================================
# 4. Save Cleaned Dataset to analysis/
# ==========================================
print(f"Saving prepared dataset to {analysis_path}...")
with pd.ExcelWriter(analysis_path, engine='openpyxl') as writer:
    df_clean.to_excel(writer, sheet_name='experiment_data', index=False)
    # copy the business_context sheet from raw workbook
    xl_raw = pd.ExcelFile(raw_path)
    if 'business_context' in xl_raw.sheet_names:
        df_context = xl_raw.parse('business_context')
        df_context.to_excel(writer, sheet_name='business_context', index=False)

print("Dataset prepared and saved successfully!")
