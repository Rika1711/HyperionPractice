## Capstone Project: House Price Prediction with Linear Regression

This capstone project involves building and evaluating a multiple linear regression model to predict house prices using the `ames.csv` dataset. The project will cover data cleaning, exploratory data analysis, model building, and performance evaluation.

### Instructions:

* Read the `ames.csv` file into the Jupyter notebook named `Linear_Regression_Ames.ipynb`.
* Complete all the following steps within this notebook.

### Requirements:

1.  **Load Data:**
    * Read the `ames.csv` file into your Jupyter notebook. (Ensure `ames.csv` is in the same directory or provide the correct path).

2.  **Data Cleaning and Preparation:**
    * Clean and prepare the dataset as necessary (e.g., handling missing values, encoding categorical variables if needed for other features, though the specified independent variables are numerical).

3.  **Exploratory Data Analysis (EDA):**
    * Perform exploratory data analysis to gain insights into the dataset.
    * Visualize the distributions of the dependent variable (SalePrice) and the chosen independent variables (`Gr_Liv_Area`, `Garage_Area`).
    * Identify any patterns or trends in the data relevant to house prices.

4.  **Define Variables:**
    * For the linear regression model, use the following independent variables:
        * `Gr_Liv_Area`: size of above grade, ground living area in square feet
        * `Garage_Area`: size of garage in square feet
    * Split the dataset into the independent variables (`X`) and the single dependent variable (`Y`, which is likely 'SalePrice').

5.  **Visualize Relationships:**
    * Generate plots (e.g., scatter plots) to explore the relationships between the independent variables (`Gr_Liv_Area`, `Garage_Area`) and the dependent variable (SalePrice).

6.  **Train-Test Split:**
    * Split the data into training and test sets using a split ratio of 75% for training and 25% for testing.

7.  **Build Multiple Linear Regression Model:**
    * Build a multiple linear regression model using the training set with both independent variables.

8.  **Print Model Parameters:**
    * Print out the intercept and coefficients of the trained model.

9.  **Generate Predictions:**
    * Generate predictions for the test set using your trained model.

10. **Evaluate Model Performance:**
    * Evaluate the model's performance by computing the Mean Squared Error (MSE) or Root Mean Squared Error (RMSE) on the test set.

11. **Error Plot:**
    * Generate an error plot to visualize the differences between the predicted and actual values in the test set.

12. **Interpret Coefficients:**
    * Print the coefficients and interpret them within the context of the house price prediction. Explain what each coefficient signifies.

13. **Summarize Findings:**
    * Summarise the findings from the entire analysis within the notebook. This should include insights from the exploratory data analysis, the model's performance, and any notable observations or conclusions.
   

### Libraries:

* `numpy`
* `pandas`
* `matplotlib.pyplot`
* `seaborn`
* `sklearn`
* `statistics`
