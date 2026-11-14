# Digital Life & Wellbeing Analysis

**Part 01: Data Understanding, Data Quality Assessment & Univariate Statistical Analysis**

## Project Overview

This project investigates a dataset containing information about digital habits, sleep, exercise, study/work duration, stress and productivity.

It is being developed progressively as part of my undergraduate Data Science learning journey.

The goal is to understand the dataset, assess its quality, explore statistical characteristics, and later investigate relationships between digital habits and wellbeing.

## Dataset Overview

| Attribute | Details |
|---|---|
| Observations | 11,000 |
| Variables | 10 |
| Numerical measurement variables | 7 |
| Categorical variables | 2 |
| Identifier | `user_id` |
| Format | CSV |
| Source | Add original dataset URL and attribution |

## Tools and Technologies

- Python
- Pandas
- Jupyter Notebook
- Visual Studio Code

## Work Completed

### 1. Data Understanding

- Imported and explored the dataset.
- Examined dimensions, datatypes and unique values.
- Classified numerical and categorical variables.
- Created a data dictionary.

### 2. Data Quality Assessment

Checked for missing values, duplicate records, numerical range violations, categorical consistency and logical inconsistencies.

**Findings:**

- No missing values reported.
- No completely duplicated rows reported.
- No numerical range violations reported under the defined constraints.
- Potential logical inconsistencies identified between social-media usage and daily screen time.

The potentially inconsistent observations were retained rather than automatically deleted or modified.

### 3. Univariate Statistical Analysis

Implemented the following statistical measures using mathematical formulas and Python:

- Mean, median and mode
- Sample variance and standard deviation
- Range
- Quartiles (Q1, Q2, Q3)
- Interquartile Range (IQR)

The calculations were used to understand central tendency, dispersion and positional characteristics.

## Key Statistical Findings

| Variable | Mean | Median | Standard Deviation |
|---|---:|---:|---:|
| Age (years) | 32.56 | 33.00 | 9.69 |
| Screen time (hours) | 6.56 | 6.57 | 3.18 |
| Social media (hours) | 4.25 | 4.25 | 2.16 |
| Sleep (hours) | 5.99 | 6.00 | 1.73 |
| Exercise (minutes) | 59.47 | 59.00 | 34.72 |
| Study/work (hours) | 5.54 | 5.56 | 2.59 |
| Productivity score | 50.62 | 50.22 | 28.84 |

### Interpretation

The dataset shows variation in digital usage, sleep duration, exercise, study/work habits and productivity.

The middle 50% of screen-time observations range from 3.81 to 9.33 hours, while sleep duration ranges from 4.50 to 7.49 hours for the central half of observations.

Productivity scores show substantial variation, with a standard deviation of 28.84 and an IQR of 50.50.

These descriptive results do not establish relationships or causation between variables.

## Limitations

- Potential logical inconsistencies remain unresolved.
- Some numerical validation ranges are based on assumptions requiring dataset documentation.
- The productivity scoring methodology requires confirmation.
- No causal conclusions can be drawn from descriptive statistics.

## Project Roadmap

- [x] Dataset exploration and data dictionary
- [x] Initial data-quality assessment
- [x] Formula-based descriptive statistics
- [x] Statistical interpretation
- [ ] Histograms and distribution visualizations
- [ ] Bivariate and multivariate analysis
- [ ] Hypothesis testing
- [ ] Predictive modelling
- [ ] Prescriptive insights

## Next Stage

Univariate visualizations will be used to examine distribution shapes, concentration and potential outliers. Later analysis will investigate associations between digital habits, stress and productivity.

---

**Status:** Part 01 completed — Statistical Analysis Foundation
