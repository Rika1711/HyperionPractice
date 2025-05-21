## Practical Task 1: Data Preprocessing - Missing Values

This task focuses on reading data, inspecting its initial state, and analyzing missing values within the `store_income_data_task.csv` dataset.

### Instructions:

* Open the `data_preprocessing.ipynb` file.
* Explore the provided examples in the notebook.
* Complete the following steps within the notebook.

### Requirements:

1.  **Read Data:**
    * Read in the `store_income_data_task.csv` file into a Pandas DataFrame.

2.  **Display Observations:**
    * Display the first five observations of the loaded DataFrame.

3.  **Missing Values Count:**
    * Get the number of missing values per column and print the results.

4.  **Analysis of Missing Data:**
    * Write a note (in a markdown cell in the notebook) explaining why you think there is missing data in the `store_email`, `department`, and `country` columns.
    * Remember to classify the missingness according to the three categories (e.g., Missing Completely At Random (MCAR), Missing At Random (MAR), Missing Not At Random (MNAR)).

---

## Practical Task 2: Data Preprocessing - Normalization and Standardization

This task involves understanding and applying data scaling techniques (normalization and standardization) to variables, including theoretical decisions and practical visualization.

### Instructions:

* Continue to Task 2 within the `data_preprocessing.ipynb` notebook.
* For more information about normalization and standardization, refer to external resources if needed (the prompt mentions "see here" but doesn't provide a link, so you'll need to rely on your understanding or search for resources).

### Requirements:

1.  **Scaling Method Decisions:**
    * For the following examples, decide whether normalisation or standardisation makes more sense and explain your reasoning:
        a.  You want to build a linear regression model to predict someone's grades, given how much time they have spent on various activities during a typical school week. You notice that your measurements for how much time students spend studying aren't normally distributed: some students spend almost no time studying, while others study for four or more hours daily. Should you normalise or standardise this variable?
        b.  You're still working with your student’s grades, but you also want to include information on how students perform on several fitness tests. You have information on how many jumping jacks and push-ups each student can complete in a minute. However, you notice that students perform far more jumping jacks than push-ups: the average for the former is 40, and for the latter, only 10. Should you normalise or standardise this variable?

2.  **Visualize and Scale 'EG.ELC.ACCS.ZS':**
    * Visualize the "EG.ELC.ACCS.ZS" column from the `countries` dataset (ensure this dataset is available or loaded).
    * Scale the column using the appropriate scaling method (normalisation or standardisation) based on its distribution.
    * Finally, visualize the original and scaled data alongside each other using histograms or density plots for comparison.
    * *Note:* "EG.ELC.ACCS.ZS" represents the percentage of the population with access to electricity.
  
### Libraries:

* `pandas`
* `numpy`
* `sklearn.preprocessing`
* `seaborn`
* `matplotlib.pyplot`
