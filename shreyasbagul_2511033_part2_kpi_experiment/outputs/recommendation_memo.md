# Business Recommendation Memo: Onboarding Experiment Analysis

**TO:** Subscription Product Leadership  
**FROM:** Shreyas Bagul, Business Analyst  
**DATE:** June 23, 2026  
**SUBJECT:** Recommendation for Onboarding & Activation Campaign Rollout  

---

## 1. Executive Summary

We conducted a comprehensive A/B test analysis of the onboarding and activation experiment (N = 1400: Control N = 690, Treatment N = 710). The goal of the experiment was to evaluate whether a new campaign onboarding flow improves conversion and user engagement. 

Our statistical analysis indicates that:
1. **Primary Success**: The new onboarding flow (Treatment) led to a highly statistically significant **+120.88% relative lift** in the Paid Conversion Rate (from 3.19% in Control to 7.04% in Treatment, p-value = 0.0011).
2. **Operational Overload (Guardrail Risk)**: The support ticket rate increased significantly by **+10.01%** (from 14.78% in Control to 24.79% in Treatment, p-value = 0.000003), presenting a substantial operational overhead risk.
3. **Segment Decline**: The **Social traffic segment** experienced a decline in Paid Conversion Rate (from 7.75% to 6.06%) and ARPU (from $137.14 to $51.94), representing friction for social media signups.
4. **Outlier Impact**: While raw average revenue per user (ARPU) was relatively flat ($51.97 Control vs $54.25 Treatment), this was due to three massive outliers in the Control group. Excluding outliers, Treatment ARPU is **more than double** that of Control ($50.58 vs $24.13, p-value = 0.0152).

### Final Recommendation: **Launch with Segment-Level Restriction**
We recommend rolling out the new onboarding flow to all acquisition channels **except Social traffic**, while keeping the existing onboarding experience (Control) active for Social traffic. We also recommend that the product and customer service teams collaborate to address onboarding confusion and reduce support ticket rates.

---

## 2. Success Framework & North Star Metric

We defined a success framework centered on the following metrics:
- **North Star Metric**: **Paid Conversion Rate** (Paying Subscribers / Total Users). This is the key monetization and activation metric.
- **Primary KPI Drivers**:
  - **Trial Start Rate**: Indicates initial acquisition draw.
  - **Onboarding Completion Rate** & **Engagement Score**: Indicates early in-app activation.
  - **Paid Upgrade Rate**: Measures bottom-of-funnel conversion.
- **Guardrail Metrics**:
  - **Support Ticket Rate**: Monitors operational cost and friction.
  - **Refund Requested Rate**: Monitors buyer's remorse and product dissatisfaction.
  - **ARPU (Outlier-Sensitive)**: Measures monetization quality.

---

## 3. Experiment Results & Statistical Evidence

Below is the summary of experiment metrics in the deduplicated user dataset (N = 1400):

| Metric | Control Group (N=690) | Treatment Group (N=710) | Absolute Lift | Relative Lift | P-Value | Statistical Significance |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Landing Page Visit Rate** | 63.62% | 72.39% | +8.77% | +13.78% | - | Significant |
| **Trial Start Rate** | 25.07% | 29.01% | +3.94% | +15.71% | - | Significant |
| **Onboarding Completion Rate** | 15.65% | 21.13% | +5.48% | +35.04% | - | Significant |
| **Paid Conversion Rate (North Star)**| **3.19%** | **7.04%** | **+3.85%** | **+120.88%** | **0.0011** | **Highly Significant** |
| **Average Engagement Score** | 57.03 | 62.94 | +5.91 | +10.36% | 0.0000 | Highly Significant |
| **Average Days to Convert** | 8.86 | 6.40 | -2.46 days | -27.77% | - | Positive Trend |
| **ARPU (Raw Data)** | $51.97 | $54.25 | +$2.28 | +4.39% | 0.9107 | Not Significant |
| **ARPU (Excluding Outliers)** | **$24.13** | **$50.58** | **+$26.45** | **+109.61%** | **0.0152** | **Significant** |

---

## 4. Key Guardrail and Segment Insights

### Support Ticket Increase (Operational Risk)
The proportion of users submitting at least one support ticket rose from **14.78% to 24.79%** (p-value = 0.000003). The average number of support tickets per user rose from **0.220 to 0.373**. This statistically significant increase indicates user friction during onboarding. If launched globally without modifications, customer service costs will spike.

### Revenue Quality and Outliers
Control group revenue was heavily skewed by three outliers ($8,610.72, $6,788.95, and $3,887.98), making raw ARPU look similar. However, excluding these outliers reveals that **Treatment generated $50.58 ARPU vs. Control's $24.13** (p-value = 0.0152), showing a more reliable, broad-based monetization model in Treatment.

### The Social Segment Decline
The **Social traffic source** was the only segment that experienced a decline in performance:
- Paid Conversion Rate fell from **7.75% to 6.06%** (absolute change of **-1.69%**).
- ARPU fell from **$137.14 to $51.94** (absolute change of **-$85.20**).
This suggest that the new onboarding campaign is too complex or introduces too much friction for Social traffic, which traditionally prefers fast, friction-free signups.

---

## 5. Strategic Recommendations & Next Steps

### Action Plan
1. **Segmented Rollout (Launch with Restriction)**:
   - Deploy the new onboarding campaign (Treatment) to **Organic, Paid Search, Email, and Referral** traffic.
   - Retain the existing onboarding experience (Control) for **Social** traffic.
2. **Onboarding Optimization**:
   - Redesign step completion triggers and in-app tooltips to resolve the confusion that led to the +67% spike in support ticket rate.
   - Audit onboarding completion logs to identify where users are raising tickets.
3. **Social-Specific Flow Design**:
   - Design a simplified, low-friction onboarding flow (e.g. 1-click activation) specifically for Social signups to capture their interest and test it in a follow-up experiment.

### Risks and Limitations
- **Customer Support Load**: Rolling out the campaign (even without Social) will increase support volume. The support team must be staffed accordingly.
- **Enterprise Cohorts**: We must monitor whether the lack of high-value outliers in Treatment indicates a decline in our ability to sign up high-value corporate/enterprise clients.
