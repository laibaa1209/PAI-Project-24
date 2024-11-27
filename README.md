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

# Introduction

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
     ![image](https://github.com/user-attachments/assets/3398bd12-f8fd-4e3d-a245-32ca01fe8c83)


2. **Data Type Conversion**:
   - Converted string values (if any) to numeric types.
     ![image](https://github.com/user-attachments/assets/518c7687-7be9-4425-bb63-36a32f4c653e)


3. **Outlier Detection**:
   - Identified and removed nonsensical values (e.g., negative cement amounts).
     ![image](https://github.com/user-attachments/assets/716b9113-9942-4f72-a332-4dee25491e7f)


4. **Scaling Data**:
   - Applied data scaling to standardize feature ranges.
   - ![image](https://github.com/user-attachments/assets/7dbffeb7-3bdd-48e9-b091-197f48dfc928)


5. **Demonstration of Cleaning**:
   - Introduced intentional inconsistencies, duplicates, and missing values to showcase cleaning techniques.
     ![image](https://github.com/user-attachments/assets/67f11c41-8d63-4d5b-bf5c-ab0fa5481d09)


---

## Statistical Insights and Visualization
Key statistical measures and visualizations were generated using **Numpy**, **Pandas**, **Matplotlib**, and **Seaborn**.

### Statistical Analysis:
- **Mean, Median, and Mode**: Provided trends in material usage.
- **Standard Deviation and Variance**: Showed variability in material proportions and results.
  ![image](https://github.com/user-attachments/assets/d0506138-f730-445f-9bac-e4635297ab33)

- **Correlation Matrix**: Identified relationships between input materials and outputs like slump value.
  ![image](https://github.com/user-attachments/assets/2309fb70-3cf2-4171-9bc7-0028a26869b8)


### Visualizations:
- **Histograms**: Displayed distributions of materials (e.g., cement, water).
  ![image](https://github.com/user-attachments/assets/8f592cfe-92a9-4aca-937a-972f38eec3bf)

- **Box Plots**: Highlighted outliers in slump values and other metrics.
  ![image](https://github.com/user-attachments/assets/3792e722-c594-432a-8ce1-2c13e46c81c4)

- **Heatmaps**: Visualized correlations to identify significant predictors.
 ![image](https://github.com/user-attachments/assets/ba249001-459b-4c37-b47d-bd4bbfc5a010)

- **Joint Plot**: Visualized the relationship between SLUMP(cm) and FLOW(cm).
  ![image](https://github.com/user-attachments/assets/e23e68d2-de46-49ff-ac7b-3bd9410a08f4)
  
- **Bar Chart**: Visualized the mean values.
  ![image](https://github.com/user-attachments/assets/91c66de0-5fcf-4fef-95ef-2844e1857a74)

- **Scatter Plot**: The scatter plot shows the relationship between SLUMP and Compressive Strength, helping to identify trends, correlations, or patterns between these two variables.
  ![image](https://github.com/user-attachments/assets/57a426ba-5b6f-45f6-8e25-ced95183e0c0)



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
     ![image](https://github.com/user-attachments/assets/53f3a268-733b-4d4b-8001-ccc3dff90eac)

3. **Evaluation Metrics**:
   - **Mean Squared Error (MSE)**: Assessed prediction accuracy.
   - **R-squared (R²)**: Evaluated the model's explanatory power.
     ![image](https://github.com/user-attachments/assets/790ed50f-e0e7-47f1-9e8e-ab875866bc7d)


### Performance:
The model achieved reasonable predictions, with water and cement proportions significantly influencing slump values.
![image](https://github.com/user-attachments/assets/86c59aa4-93c5-4b25-bb31-3d86eb61c2f9)


---

## User Interface
A user-friendly web interface was created using **Flask** to make predictions accessible.

### Features:
1. **Input Fields**:
   - Users can input data for concrete material proportions.
   1. Accepts input parameters for concrete composition:
     - Water
     - Cement
     - Slag
     - Fly Ash
     - Superplasticizer (SP)
     - Coarse Aggregate
     - Fine Aggregate
     - Flow
     - Compressive Strength (28-day)
     ![image](https://github.com/user-attachments/assets/229657d2-40a3-4fe1-b887-ae9c003913e3)

2. **Prediction Output**:
   - 2. Predicts the slump value using a trained machine learning model.
   - 3. Displays the predicted slump value on a results page.
     ![image](https://github.com/user-attachments/assets/61c46659-84e2-46e8-a2d3-f132dc3384d9)


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


