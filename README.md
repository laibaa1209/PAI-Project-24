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

# Introduction:
This project analyzes the Concrete Slump dataset from Kaggle to predict slump values based on concrete mixture ingredients using data cleaning, statistical analysis, and a Linear Regression model. A user-friendly interface will be developed for easy prediction input.

1. Data Cleaning and Preparation
Data cleaning was carried out using Pandas to ensure the dataset was ready for analysis:
Handling Missing Values: Missing values were filled with mean, median, or mode, depending on the column's characteristics.
 
Data Type Conversion: Strings (if any) were converted to numeric types.
 
Outlier Detection: Negative or nonsensical values (e.g., negative cement amounts) were identified and removed.
 

Scaling Data: Data was scaled so that it would be easy to apply Model.
 

To illustrate data cleaning techniques, intentional missing values, duplicates and inconsistencies were introduced and resolved.
 

2. Statistical Insights and Visualization
Key statistical measures and visualizations were generated using Numpy, Pandas, Matplotlib, and Seaborn to extract meaningful insights:
Statistical Analysis:
Mean, Median, and Mode: Provided averages and trends in material usage.
Standard Deviation and Variance: variability in material proportions and test results. 


Correlation Matrix: Identified relationships between material inputs and outputs like slump value and compressive strength.
 
Visualizations
Histograms: Displayed the distribution of materials (e.g., cement, water).
 


Box Plots: Highlighted outliers in slump values and other metrics. 

Heatmaps: Illustrated correlations between variables, helping to identify significant predictors of slump value.
 
Example Graph: A heatmap of the correlation matrix revealed strong relationships between slump value and water content, aiding in model feature selection. More graphs were used to visualize the statistical parts of the dataset.

3. Machine Learning Model
A Linear Regression model was implemented using the Scikit-learn library to predict the slump value based on material proportions.
Model Workflow
Feature Selection: Input features included cement, water, fine aggregate, and coarse aggregate amounts.
Model Training: The dataset was split into training and testing sets (80-20 split).
Evaluation Metrics:
Mean Squared Error (MSE): Evaluated prediction accuracy.
R-squared (R²): Assessed the model's explanatory power.
 
The model provided reasonable predictions, with significant contributions from water and cement proportions.
 

4. User Interface
A user-friendly interface was developed to demonstrate practical applications:
 
One would input the data here and click on predict.
 
This will show the predicted data.


Web Application
A web-based interface was designed using Flask, allowing users to access the application via a browser. This version provided scalability and a better user experience. This application would let the user enter the data and let the model predict the target.
5. Conclusion
This project successfully:

1.	Cleaned and prepared the Concrete Slump dataset.
2.	Generated valuable insights through statistical analysis and visualization.
3.	Developed a Linear Regression model to predict slump values.
4.	Designed a user interface for real-world applications.
The work highlights the importance of material proportions in determining concrete properties and demonstrates how data analysis can guide better construction practices. Future improvements include exploring advanced machine learning models and expanding the dataset for broader applicability.

6. References
●	Kaggle. Concrete Slump Dataset. [https://www.kaggle.com/datasets/huseyincenik/cement-slump/data]
●	Python Libraries: Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn, Flask.


