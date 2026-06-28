# KPI Framework, Business Experiment Analysis & Decision Recommendation (Part 2)

**Student Name:** Shreyas Bagul  
**Student ID:** 2511033  

---

## 1. Business Context

A subscription-based digital product company launched a new onboarding and activation campaign. To evaluate the performance of this campaign before a global rollout, the company ran an A/B test dividing signups into two cohorts:
- **Control Group**: Existing onboarding experience.
- **Treatment Group**: New onboarding campaign experience.

The goal of this project is to analyze the experiment results, establish a KPI framework, test statistical significance, assess guardrail metrics, and provide a launch recommendation to leadership.

---

## 2. Dataset Description

The clean dataset (`analysis/experiment_analysis.xlsx`) contains **1400 unique users** (N = 1400) with the following fields:
- `user_id`: Unique identifier for each signup (8 exact duplicates were removed).
- `signup_date`: Date the user signed up.
- `experiment_group`: Cohort assignment (`Control` or `Treatment`).
- `region`: Geographical region (`East`, `West`, `North`, `South`).
- `device_type`: Device used (`Mobile`, `Desktop`, `Tablet`, or `Unknown`).
- `traffic_source`: Acquisition channel (`Organic`, `Paid Search`, `Social`, `Referral`, `Email`, or `Unknown`).
- `plan_type`: Subscription plan selected (`Free`, `Basic`, `Premium`).
- `visited_landing_page`: Binary indicator (1 if landing page visited, 0 otherwise).
- `started_trial`: Binary indicator (1 if trial started, 0 otherwise).
- `completed_onboarding`: Binary indicator (1 if onboarding completed, 0 otherwise).
- `converted_to_paid`: Binary indicator (1 if converted to paid, 0 otherwise).
- `revenue_30d`: Continuous revenue generated within 30 days of signup.
- `support_tickets_30d`: Count of support tickets raised in the first 30 days.
- `refund_requested`: Binary indicator (1 if refund requested, 0 otherwise).
- `days_to_convert`: Continuous days to convert for paid users (null for non-converted).
- `engagement_score`: In-app engagement score (0 to 100).

---

## 3. Success Framework & North Star Metric

### North Star Metric: **Paid Conversion Rate**
- **Definition**: Paying Users / Total Users.
- **Rationale**: This is the ultimate activation metric that connects early product experience to actual revenue. Mid-funnel metrics (Landing Page CTR, Trial Start) feed into this North Star.
- **Blind Optimization Risk**: Maximizing conversion rate blindly might result in:
  - Down-selling users to cheaper, unprofitable plans.
  - Attracting high-support, high-refund users (post-purchase remorse).
  - Skewing plan distribution toward low-value tiers.

### KPI Tree Summary
The KPI tree hierarchically connects the North Star to primary drivers and sub-drivers:
- **North Star**: Paid Conversion Rate.
- **Primary Drivers**:
  1. **Trial Start Rate**: Measures acquisition quality and mid-funnel conversion.
  2. **Onboarding Completion Rate** & **Engagement Score**: Measures activation quality.
  3. **Plan Upgrade Rate**: Measures monetization tier quality.
- **Guardrail Metrics**:
  - Support Ticket Rate (operational overhead).
  - Refund Requested Rate (transaction quality).
  - ARPU (monetization value).

---

## 4. Hypothesis Testing & Statistical Outputs

We conducted a two-proportion z-test and a Welch's t-test to evaluate the statistical significance of the onboarding flow changes:

1. **Paid Conversion Rate (Success Metric)**:
   - Control: **3.19%** (22 conversions / 690)
   - Treatment: **7.04%** (50 conversions / 710)
   - Z-Statistic: **3.2640** | P-Value (One-tailed): **0.000549**
   - **Result**: **Highly Significant**. Reject the null hypothesis. The Treatment group has a significantly higher Paid Conversion Rate.
2. **Engagement Score (Supporting Metric)**:
   - Control Mean: **57.03** | Treatment Mean: **62.94**
   - t-Statistic: **7.9282** | P-Value: **0.000000**
   - **Result**: **Highly Significant**. Onboarding completion significantly increased user engagement.
3. **Support Ticket Rate (Guardrail Metric)**:
   - Control Rate: **14.78%** | Treatment Rate: **24.79%**
   - Z-Statistic: **4.6921** | P-Value: **0.000003**
   - **Result**: **Highly Significant Increase**. The new onboarding flow caused a statistically significant increase in support load, indicating user friction or technical bugs.

---

## 5. Guardrail Evaluation & Segment Decline

- **Revenue Quality**: In the raw data, ARPU was $51.97 (Control) vs $54.25 (Treatment). However, Control was skewed by 3 extreme outliers. Removing outliers shows that **Treatment ARPU ($50.58) was double Control ARPU ($24.13)** (p-value = 0.0152), indicating robust revenue growth.
- **Segment Decline**: The **Social Traffic segment** was the only group to show negative results:
  - Paid Conversion Rate declined from **7.75% to 6.06%** (absolute change: -1.69%).
  - ARPU declined from **$137.14 to $51.94** (absolute change: -$85.20).
  - Social media signups found the new flow too tedious, resulting in drop-off.

---

## 6. Strategic Rollout Recommendation

### Final Decision: **Launch with Segment-Level Restriction**
- **Action**: Deploy the Treatment onboarding flow for all traffic sources **except Social**. For Social, keep the Control flow.
- **Justification**: Paid Conversion Rate doubled (highly significant) and ARPU (excluding outliers) doubled. However, the Social segment saw a drop in conversions and support tickets increased significantly overall.
- **Next Steps**:
  - Audit the onboarding flow to resolve the confusion that led to the support ticket increase.
  - Design a simplified onboarding path specifically for Social media signups.

---

## 7. Included Screenshots (`screenshots/`)

| Screenshot File | Description |
| :--- | :--- |
| `experiment_summary_preview.png` | Control vs Treatment overall metrics comparison table. |
| `hypothesis_test_preview.png` | Standard normal distribution plot showing the critical region, z-statistic, and p-values. |
| `kpi_tree.png` | Complete KPI success and guardrail hierarchy diagram. |
