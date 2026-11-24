# Digital Life & Wellbeing
### Exploratory and Predictive Analysis of Social Media, Sleep, Stress and Productivity

A Fundamentals of Data Science project investigating digital habits, lifestyle characteristics and productivity using data preprocessing, exploratory data analysis, statistical techniques and Simple Linear Regression.

The project focuses on understanding the dataset, implementing statistical calculations using mathematical formulas and evaluating whether individual lifestyle factors can predict productivity.

---

## 1. Project Overview

Digital devices and social media are part of everyday life. Screen time, sleep duration, exercise and study/work habits are often discussed in relation to productivity and wellbeing.

This project investigates whether such relationships can be identified in a dataset using statistical analysis and predictive modelling.

The analysis follows the Data Science lifecycle, beginning with data understanding and cleaning, followed by univariate and bivariate analysis, feature engineering, correlation analysis and regression modelling.

An important part of the project is evaluating the results critically rather than assuming that every variable will have a strong relationship with productivity.

## 2. Project Objectives

The main objectives are:

- To understand the structure, attributes and quality of the dataset.
- To identify and handle missing values, duplicates, outliers and logical inconsistencies.
- To calculate descriptive statistics using mathematical formulas.
- To explore numerical and categorical variables through visualizations.
- To investigate relationships using covariance, Pearson correlation and scatterplots.
- To apply feature engineering for additional analysis.
- To implement Simple Linear Regression using Ordinary Least Squares.
- To compare individual regression models against a mean-baseline model.
- To interpret the findings and identify limitations.

## 3. Dataset Information

**Dataset:** Social Media Usage vs Sleep, Stress and Productivity

**Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/jayjoshi37/social-media-usage-vs-sleep-stress-and-productivity)

**Total observations:** 11,000

**Total attributes:** 10

The dataset contains information about digital habits, daily activities, stress levels and productivity.

### Dataset Attributes

| Attribute | Description | Data Type |
|---|---|---|
| user_id | Unique identifier for each observation | Identifier |
| age | Age of the individual | Numerical |
| daily_screen_time_hours | Total daily screen time in hours | Numerical |
| social_media_hours | Daily social-media usage in hours | Numerical |
| sleep_hours | Daily sleep duration in hours | Numerical |
| exercise_minutes | Daily exercise duration in minutes | Numerical |
| study_work_hours | Daily study or work duration | Numerical |
| stress_level | Stress category: Low, Medium or High | Categorical |
| social_media_platform | Social-media platform category | Categorical |
| productivity_score | Numerical productivity score | Numerical |

For predictive analysis, `productivity_score` was selected as the target variable.

## 4. Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Statistical calculations and data analysis |
| Pandas | Data handling and tabular operations |
| NumPy | Numerical operations and array handling |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualizations |
| Jupyter Notebook / VS Code | Code development and execution |
| GitHub | Version control and project documentation |
| Overleaf (LaTeX) | Technical project report |

The main statistical and regression calculations were implemented using mathematical formulas rather than relying entirely on predefined library functions.

## 5. Project Methodology

The project follows these stages:

**Data Collection → Data Understanding → Data Cleaning → Exploratory Data Analysis → Statistical Analysis → Feature Engineering → Regression Modelling → Model Evaluation → Interpretation**

### 5.1 Data Understanding

The dataset was initially examined to understand its dimensions, data types, attributes, numerical ranges and categorical values.

This stage helped identify which variables could be used for statistical analysis and which could serve as potential predictors of productivity.

### 5.2 Data Cleaning and Preprocessing

Data quality was examined before performing the main analysis.

The cleaning process covered:

- Missing-value detection and imputation.
- Duplicate-record identification and removal.
- Numerical range validation.
- Outlier detection using statistical methods.
- Logical consistency checks between related variables.
- Before-and-after data-quality comparisons.

The original dataset did not contain the missing values or duplicate records used in the cleaning demonstrations. Therefore, separate copies were modified to demonstrate median imputation, mode imputation and duplicate removal.

#### Logical Consistency Check

An important issue was identified when comparing daily screen time with social-media usage.

**3,217 observations** had social-media hours greater than total daily screen time.

Under the assumption that social-media usage is part of total screen time, these observations violate the expected condition:

`social_media_hours <= daily_screen_time_hours`

A constrained median-based treatment was implemented to correct flagged values without removing the observations.

The correction was checked using before-and-after comparisons.

This treatment depends on the stated assumption and does not recover the original true usage values.

## 6. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the distributions, variability and relationships present in the dataset.

### 6.1 Descriptive Statistics

The following statistics were calculated:

- Mean, median and mode.
- Minimum and maximum.
- Range and quartiles.
- Variance and standard deviation.
- Interquartile range (IQR).

Several calculations were implemented manually using mathematical formulas and Python loops or dictionaries.

### 6.2 Univariate Analysis

Univariate analysis was used to study individual variables.

**Visualizations used:**

- Histograms for numerical distributions.
- Bar charts for categorical frequencies.
- Box plots for variability and potential outliers.

#### Observations

Several numerical variables showed approximately uniform distributions across their observed ranges.

The social-media platform categories were also relatively balanced, with no single platform strongly dominating the dataset.

These findings describe the dataset's composition and should not be interpreted as evidence of real-world platform popularity or behavior.

## 7. Bivariate and Diagnostic Analysis

Bivariate analysis was performed to investigate relationships between two variables.

### 7.1 Covariance Analysis

Covariance was calculated to examine whether numerical variables tended to vary in the same or opposite directions.

The calculation was implemented using the mathematical formula:

\[
\operatorname{Cov}(X,Y)=\frac{\sum_{i=1}^{n}(X_i-\bar X)(Y_i-\bar Y)}{n-1}
\]

### 7.2 Pearson Correlation Analysis

Pearson correlation was calculated to measure the strength and direction of linear relationships.

\[
r=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}
\]

A correlation matrix and heatmap were generated to compare the numerical features.

#### Correlation with Productivity

| Feature | Pearson Correlation |
|---|---:|
| Age | -0.011 |
| Daily Screen Time | -0.002 |
| Social Media Hours | -0.006 |
| Sleep Hours | +0.016 |
| Exercise Minutes | -0.002 |
| Study/Work Hours | -0.002 |

#### Key Findings

All six numerical features showed negligible linear correlations with productivity.

Sleep duration had a small positive correlation of approximately 0.016, while the remaining features had similarly small negative correlations.

The heatmap showed that most off-diagonal correlation values were close to zero.

These results suggest that the measured numerical features have limited individual linear association with productivity in this dataset.

### 7.3 Scatterplot Analysis

Six scatterplots were generated to compare productivity with:

1. Age
2. Daily screen time
3. Social-media hours
4. Sleep duration
5. Exercise duration
6. Study/work hours

The scatterplots showed that productivity scores were widely distributed across the observed ranges of these variables.

No strong upward, downward or curved pattern was visually apparent.

### 7.4 Productivity Group Comparison

The highest 10% and lowest 10% productivity groups were compared using their average lifestyle characteristics.

The two groups showed very similar average sleep duration, screen time, exercise time and study/work hours despite their different productivity scores.

This provided further evidence that the recorded numerical lifestyle features did not clearly distinguish high- and low-productivity observations through their group means.

### 7.5 Categorical Comparisons

Categorical–numerical and categorical–categorical comparisons were also considered, including stress level versus productivity and social-media platform versus stress level.

Box plots, frequency tables and stacked bar charts were used to examine group distributions.

## 8. Feature Engineering

Feature engineering was explored to create additional variables from the existing dataset.

The work included constructing and examining variables such as:

- Sleep-duration categories.
- Screen-time categories.
- Non-social screen-time estimates.
- Productivity-based groups.

These variables helped organize observations into meaningful categories for further analysis.

An important finding was that subtracting social-media hours from total screen time produced negative values for some observations. This highlighted the need to check logical constraints before using constructed features.

The engineered variables were used for exploratory purposes; the final six-feature Simple Linear Regression comparison used the original numerical predictor definitions.

## 9. Simple Linear Regression

Simple Linear Regression was implemented to investigate whether individual numerical variables could predict productivity.

The model follows:

\[
\hat Y=b_0+b_1X
\]

Where:

- \(X\) is the independent variable.
- \(\hat Y\) is the predicted productivity score.
- \(b_0\) is the intercept.
- \(b_1\) is the slope.

### 9.1 Manual OLS Implementation

Ordinary Least Squares was implemented using mathematical formulas to calculate the slope and intercept.

\[
b_1=\frac{\sum(X_i-\bar X)(Y_i-\bar Y)}{\sum(X_i-\bar X)^2}
\]

\[
b_0=\bar Y-b_1\bar X
\]

The data was divided into 80% training and 20% testing observations.

### 9.2 Sleep Hours vs Productivity

Sleep duration was selected as the initial independent variable to demonstrate the complete regression process.

The fitted regression equation was:

\[
\hat Y=49.3643+0.1738X
\]

The slope indicates an estimated increase of approximately 0.174 productivity points for every additional hour of sleep.

However, this relationship was very weak and did not result in useful predictive performance.

### 9.3 Sleep Model Evaluation

| Evaluation Metric | Result |
|---|---:|
| MAE | 25.1429 |
| MSE | 832.6393 |
| RMSE | 28.8555 |
| R-squared | -0.0007 |

The negative test R-squared indicates that the model performed slightly worse than predicting a constant equal to the test-set mean.

Actual-versus-predicted and residual plots were generated to examine prediction errors.

## 10. Comparison of Six Regression Models

After implementing the sleep model, the same mathematical method was applied separately to all six numerical predictors.

Each model used one independent variable and the same target, `productivity_score`.

A common 80:20 train-test split was used to ensure fair comparison between the six models.

### Model Comparison Results

| Independent Variable | Test RMSE | Test R² |
|---|---:|---:|
| Age | 29.1901 | -0.0002 |
| Exercise Minutes | 29.1921 | -0.0003 |
| Daily Screen Time | 29.1922 | -0.0003 |
| Study/Work Hours | 29.1946 | -0.0005 |
| Sleep Hours | 29.1992 | -0.0008 |
| Social Media Hours | 29.2061 | -0.0013 |

**Mean-baseline RMSE: 29.1919**

### Model Comparison Findings

Age achieved the lowest RMSE among the six individual regression models.

However, its improvement over the mean baseline was only approximately 0.0018 points.

All six models produced negative test R-squared values, indicating that none performed better than a constant prediction equal to the test-set mean.

The results demonstrate that the available numerical variables provide little useful individual linear predictive information about productivity.

The original sleep-only model and the six-feature comparison used different random train-test splits, so their numerical evaluation results should not be compared directly.

## 11. Key Project Findings

The main findings from the analysis are:

**1. Data quality requires logical validation.**

A dataset may contain no missing values or duplicates and still include inconsistencies between related attributes.

**2. The numerical lifestyle variables show negligible linear correlations with productivity.**

Pearson correlation coefficients were close to zero across the selected features.

**3. High- and low-productivity observations have similar average lifestyle characteristics.**

The top and bottom productivity groups were not clearly separated by their average numerical habits.

**4. Individual Simple Linear Regression models provide limited predictive performance.**

The regression models produced negative test R-squared values and RMSE values close to the baseline.

**5. Model evaluation is as important as model implementation.**

A correctly implemented model does not necessarily produce accurate predictions. Comparing results with a simple baseline helps determine whether the model provides practical value.

## 12. Project Limitations

- The dataset's measurement definitions and generation process may limit real-world interpretation.
- Weak Pearson correlations do not prove statistical independence.
- Simple Linear Regression only models linear relationships.
- The analysis does not establish causal effects.
- Some data-cleaning treatments depend on assumptions.
- Results from different train-test splits are not directly comparable.
- The models were evaluated on one train-test split rather than repeated cross-validation.

## 13. Future Scope

Possible future improvements include:

- Investigating the origin and generation process of the dataset.
- Collecting additional real-world observations.
- Exploring nonlinear relationships.
- Comparing Multiple Linear Regression with individual regression models.
- Evaluating additional features and interactions.
- Using cross-validation for more reliable performance estimates.
- Examining other factors that may influence productivity.

## 14. Project Structure

The project is organized into separate analysis notebooks.

```text
Digital-Life-Wellbeing/
│
├── README.md
│
├── data/
│   ├── original_dataset.csv
│   └── cleaned_dataset.csv
│
├── notebooks/
│   ├── Data_cleaning.ipynb
│   ├── digital_life_analysis_Exp2.ipynb
│   ├── data-analysis_visuals_univariate.ipynb
│   ├── diagnostic_analysis.ipynb
│   └── Regression_project.ipynb
│
├── images/
│   ├── correlation_heatmap.png
│   ├── scatterplots.png
│   └── regression_comparison.png
│
├── report/
│   └── Digital_Life_Wellbeing_Report.pdf
│
└── requirements.txt
```

*The structure above is the recommended repository organization. Filenames should be updated to match the actual uploaded files.*

## 15. How to Run the Project

**Step 1:** Clone the repository.

```bash
git clone <your-repository-url>
cd Digital-Life-Wellbeing
```

**Step 2:** Install the required Python libraries.

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

**Step 3:** Start Jupyter Notebook.

```bash
jupyter notebook
```

**Step 4:** Open the notebooks in the order of the analytical workflow.

Start with data cleaning, followed by descriptive and univariate analysis, diagnostic analysis and regression.

Update local dataset paths where necessary.

## 16. Conclusion

This project applied the Data Science lifecycle to investigate relationships between digital habits, lifestyle factors and productivity.

The analysis included data-quality assessment, descriptive statistics, univariate and bivariate exploration, covariance, Pearson correlation, feature engineering and manually implemented Simple Linear Regression.

The results showed negligible linear associations between the selected numerical variables and productivity. The individual regression models also produced limited predictive performance when compared against a mean baseline.

Although the models did not achieve strong prediction accuracy, the project demonstrates the importance of validating data, implementing mathematical methods correctly and evaluating analytical results critically.

The main learning outcome was that a successful data science analysis should produce conclusions supported by evidence, even when the original expectations are not confirmed.

---

## 17. References

1. [Kaggle — Social Media Usage vs Sleep, Stress and Productivity](https://www.kaggle.com/datasets/jayjoshi37/social-media-usage-vs-sleep-stress-and-productivity)
2. [Pandas Documentation](https://pandas.pydata.org/docs/)
3. [NumPy Documentation](https://numpy.org/doc/)
4. [Matplotlib Documentation](https://matplotlib.org/stable/)
5. [Seaborn Documentation](https://seaborn.pydata.org/)
6. [Scikit-learn — Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)

---

**Project Type:** Fundamentals of Data Science — Academic Project

**Techniques:** Data Cleaning | Descriptive Statistics | EDA | Covariance | Correlation | Feature Engineering | Simple Linear Regression | Model Evaluation

**Language:** Python
