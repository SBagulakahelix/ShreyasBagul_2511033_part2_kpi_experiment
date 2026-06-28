# Hypothesis Testing Notes & Experiment Guardrails

**Student Name:** Shreyas Bagul  
**Student ID:** 2511033  
**Date:** June 23, 2026  

This document explains the statistical framework, hypotheses, tests performed, and guardrail analysis for the onboarding experiment (Deduplicated Users N = 1400: Control N = 690, Treatment N = 710).

---

## 1. Primary Success Hypothesis: Paid Conversion Rate

### Hypothesis Formulation
- **Metric Being Tested:** **Paid Conversion Rate** ($CR = \text{Converted to Paid} / \text{Total Users}$).
- **Reason for Choice:** The paid conversion rate directly measures the ultimate success of the onboarding flow—converting signups into paying subscribers. Other metrics (landing page visits, trial starts, onboarding completions) are leading indicators of conversion.
- **Null Hypothesis ($H_0$):** The onboarding onboarding flow (Treatment) does not increase the Paid Conversion Rate compared to the existing experience (Control).
  $$H_0: CR_{\text{Treatment}} \le CR_{\text{Control}}$$
- **Alternate Hypothesis ($H_a$):** The onboarding onboarding flow (Treatment) increases the Paid Conversion Rate compared to the existing experience (Control).
  $$H_a: CR_{\text{Treatment}} > CR_{\text{Control}}$$
- **Test Structure:** **One-tailed Two-Proportion Z-Test** (since we are testing for positive improvement). We also report the **Two-tailed Two-Proportion Z-Test** and the **Chi-Square Test of Independence** for completeness and robustness.
- **Significance Level ($\alpha$):** **0.05** (Standard 95% confidence level).

### Statistical Inputs & Output
- **Control Group ($N_c$):** 690 users, 22 conversions. Paid Conversion Rate ($CR_c$) = **3.19%**
- **Treatment Group ($N_t$):** 710 users, 50 conversions. Paid Conversion Rate ($CR_t$) = **7.04%**
- **Absolute Lift:** $+3.85\%$ (percentage points)
- **Relative Lift:** $+120.88\%$ (paid conversions more than doubled)
- **Z-Statistic:** **3.2640**
- **P-Value (One-Tailed):** **0.000549**
- **P-Value (Two-Tailed):** **0.001099**
- **Chi-Square Statistic ($\chi^2$):** **9.8782** (dof = 1, p-value = 0.001672)

### Decision Rule & Business Interpretation
- **Decision Rule:** Reject the Null Hypothesis ($H_0$) if $p$-value $< \alpha$ (0.05).
- **Statistical Result:** Since the one-tailed $p$-value ($0.00055$) and two-tailed $p$-value ($0.0011$) are far below the significance level $\alpha = 0.05$, **we reject the Null Hypothesis ($H_0$)**.
- **Business Interpretation:** There is overwhelming statistical evidence that the new onboarding and activation campaign significantly improves user conversion to paid. This is a highly robust and positive result.

---

## 2. Secondary Success Hypothesis: Engagement Score

- **Metric Being Tested:** Average in-app Engagement Score (0 to 100).
- **Null Hypothesis ($H_0$):** $Mean_{\text{Treatment}} \le Mean_{\text{Control}}$
- **Alternate Hypothesis ($H_a$):** $Mean_{\text{Treatment}} > Mean_{\text{Control}}$
- **Statistical Test:** **Two-Sample Welch's t-test** (unequal variances assumed).
- **Results:**
  - **Control Mean:** **57.03**
  - **Treatment Mean:** **62.94**
  - **t-Statistic:** **7.9282**
  - **P-Value:** **0.000000** (p < 0.00001)
- **Business Interpretation:** The Treatment group has a statistically significant lift in early engagement. This supports the primary finding: the new onboarding experience successfully drives activation and usage.

---

## 3. Guardrail Metrics Evaluation

To prevent business risk, we evaluate three critical guardrail metrics:

### Guardrail 1: Support Ticket Rate (Operational Overhead)
- **Metric:** Support Ticket Rate (proportion of users raising at least 1 ticket).
- **Z-Test Inputs:** 
  - Control: 102 users with tickets out of 690 (**14.78%**)
  - Treatment: 176 users with tickets out of 710 (**24.79%**)
  - Z-Statistic: **4.6921**, P-Value: **0.000003**
- **t-Test Inputs (Avg tickets per user):**
  - Control: 0.220 tickets/user
  - Treatment: 0.373 tickets/user
  - t-Statistic: **4.2141**, P-Value: **0.000027**
- **Business Risk:** **CRITICAL RISK**. The support ticket rate has increased by **+10.01%** (relative increase of **+67.7%**), which is highly statistically significant. This indicates that while the new onboarding flow is driving conversions, it is causing substantial user confusion, technical friction, or onboarding fatigue, which increases customer support costs and operational overhead.

### Guardrail 2: Refund Requested Rate (Buyer's Remorse)
- **Metric:** Refund Requested Rate (proportion of users requesting a refund).
- **Inputs:**
  - Control: 0 refunds out of 690 (**0.00%**)
  - Treatment: 3 refunds out of 710 (**0.42%**)
- **Business Risk:** **LOW RISK**. While refunds increased from 0 to 3 in Treatment, the absolute rate remains very low (0.42%) and within the acceptable industry benchmark of < 1%. However, it should be monitored closely post-launch.

### Guardrail 3: Revenue Quality (Outlier-Sensitive ARPU)
- **Metric:** Average Revenue Per User (ARPU) and Revenue Per Converted User.
- **Inputs (Full Dataset):**
  - Control ARPU: **$51.97** | Treatment ARPU: **$54.25** (Welch's t-test p-value = 0.9107)
  - Control Revenue per Converted User: **$1,630.10** | Treatment: **$770.41**
- **IQR Outlier Check:** We identified 4 positive revenue outliers (revenues > $2,340.63):
  - Three in Control ($8,610.72, $6,788.95, $3,887.98)
  - One in Treatment ($2,660.21)
- **Inputs (Without Outliers):**
  - Control ARPU (no outliers): **$24.13** (Total: $16,574.63)
  - Treatment ARPU (no outliers): **$50.58** (Total: $38,520.71)
  - Welch's t-test p-value (no outliers): **0.015215**
- **Business Risk:** **MODERATE RISK**. In the raw data, the average revenue per converted user in Treatment is less than half of Control. This is because Control's revenue was heavily skewed by 3 high-value outliers (possibly large enterprise signups).
  - Without outliers, **Treatment ARPU ($50.58) is more than double Control ($24.13)**, which is statistically significant (p = 0.0152 < 0.05).
  - This demonstrates that Treatment drives broad-based, high-conversion revenue growth rather than relying on a few high-value outliers.

---

## 4. Segment-Level Decline: The Social Traffic Segment

When analyzing the segments, we identified a critical segment-level decline:

### Segment: Traffic Source - **Social**
- **Control N:** 129 users | **Treatment N:** 132 users
- **Paid Conversion Rate:**
  - Control: **7.75%** (10 conversions)
  - Treatment: **6.06%** (8 conversions)
  - Absolute Difference: **-1.69%** (relative decline of **-21.8%**)
- **ARPU:**
  - Control: **$137.14**
  - Treatment: **$51.94**
  - Absolute Difference: **-$85.20** (relative decline of **-62.1%**)
- **Interpretation:** The Social traffic source is the **only segment** that showed a decline in conversion and revenue. Social media users typically have shorter attention spans and higher bounce rates. The new campaign onboarding flow might be too long, complex, or tedious for this cohort, introducing friction that drove them away.

---

## 5. Summary Recommendation

Based on the statistical findings:
1. **Conversion Lift:** Highly significant (p = 0.0011), supporting the onboarding flow.
2. **Support Ticket Guardrail:** Highly significant increase in support load (p = 0.000003), presenting operational risk.
3. **Social Segment Decline:** Negative impact on Social users.
4. **Recommendation:** **Launch with Segment-Level Restriction**. Roll out the Treatment onboarding flow for all traffic sources **except Social**. For Social, keep the Control onboarding experience while the product team optimizes and runs user tests to resolve the friction.
