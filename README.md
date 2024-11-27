# Team Members:

<table>
<tr>
  <th>Name</th>
  <th>Roll Number</th>
</tr>
<tr>
  <td>Alisha Zaidi</td>
  <td>23K-0025</td>
</tr>
<tr>
  <td>Laiba</td>
  <td>23K-0006</td>
</tr>
</table>

# Project Proposal: Concrete Slump predictor

[Link For Project Proposal](https://github.com/laibaa1209/PAI-Project-24/tree/main/proposal)

# Concrete Slump Prediction Project

This project focuses on analyzing the Concrete Slump dataset from Kaggle to predict slump values based on concrete mixture ingredients. It involves data cleaning, statistical analysis, a Linear Regression model, and a user-friendly interface for practical applications.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Data Cleaning and Preparation](#data-cleaning-and-preparation)
3. [Statistical Insights and Visualization](#statistical-insights-and-visualization)
4. [Machine Learning Model](#machine-learning-model)
5. [User Interface](#user-interface)
6. [Conclusion](#conclusion)
7. [References](#references)

---

## Introduction
This project analyzes the **Concrete Slump dataset** to predict slump values using:
- **Data Cleaning**: Ensuring data readiness.
- **Statistical Analysis**: Extracting insights using various statistical measures.
- **Machine Learning**: Building a Linear Regression model.
- **User Interface**: Creating a web-based application for easy predictions.

---

## Data Cleaning and Preparation
Data cleaning was performed using **Pandas** to ensure the dataset was ready for analysis. Key steps include:

1. **Handling Missing Values**:
   - Missing values were filled using mean, median, or mode depending on the column characteristics.

2. **Data Type Conversion**:
   - Converted string values (if any) to numeric types.

3. **Outlier Detection**:
   - Identified and removed nonsensical values (e.g., negative cement amounts).

4. **Scaling Data**:
   - Applied data scaling to standardize feature ranges.

5. **Demonstration of Cleaning**:
   - Introduced intentional inconsistencies, duplicates, and missing values to showcase cleaning techniques.

---

## Statistical Insights and Visualization
Key statistical measures and visualizations were generated using **Numpy**, **Pandas**, **Matplotlib**, and **Seaborn**.

### Statistical Analysis:
- **Mean, Median, and Mode**: Provided trends in material usage.
- **Standard Deviation and Variance**: Showed variability in material proportions and results.
- **Correlation Matrix**: Identified relationships between input materials and outputs like slump value.

### Visualizations:
- **Histograms**: Displayed distributions of materials (e.g., cement, water).
- **Box Plots**: Highlighted outliers in slump values and other metrics.
- **Heatmaps**: Visualized correlations to identify significant predictors.

#### Example:
- A heatmap revealed strong relationships between slump value and water content, aiding feature selection.

---

## Machine Learning Model
A **Linear Regression** model was developed using **Scikit-learn** to predict slump values based on material proportions.

### Model Workflow:
1. **Feature Selection**:
   - Input features: Cement, water, fine aggregate, and coarse aggregate amounts.
2. **Model Training**:
   - Split dataset into training and testing sets (80-20 split).
3. **Evaluation Metrics**:
   - **Mean Squared Error (MSE)**: Assessed prediction accuracy.
   - **R-squared (R²)**: Evaluated the model's explanatory power.

### Performance:
The model achieved reasonable predictions, with water and cement proportions significantly influencing slump values.

---

## User Interface
A user-friendly web interface was created using **Flask** to make predictions accessible.

### Features:
1. **Input Fields**:
   - Users can input data for concrete material proportions.
2. **Prediction Output**:
   - Displays the predicted slump value.

### Web Application:
- The application is browser-based, scalable, and intuitive for real-world usage.

---

## Conclusion
This project successfully:
1. Cleaned and prepared the **Concrete Slump dataset**.
2. Extracted valuable insights through **statistical analysis and visualization**.
3. Developed a **Linear Regression model** for slump value prediction.
4. Designed a **web interface** for real-world applications.

### Future Work:
- Implement advanced machine learning models.
- Expand the dataset for broader applicability.

---

## References
- **Dataset**: [Concrete Slump Dataset](https://www.kaggle.com/datasets/huseyincenik/cement-slump/data) (Kaggle).  
- **Python Libraries**:  
  - Pandas  
  - Numpy  
  - Matplotlib  
  - Seaborn  
  - Scikit-learn  
  - Flask  

---


