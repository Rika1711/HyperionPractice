## Compulsory Task 1: Data Cleaning and Transformation

This task focuses on cleaning and transforming specific columns within the `store_income_data_task.csv` file using a Jupyter Notebook. You should refer to `data_cleaning_example.ipynb` for guidance.

### Instructions:

* Open the Jupyter notebook named `store_income_task.ipynb`.
* Complete the following data cleaning and transformation steps within the notebook.

### Requirements:

1.  **Load Data:**
    * Load the `store_income_data_task.csv` file into a Pandas DataFrame.

2.  **Clean 'country' column:**
    * Examine all unique values in the "country" column to understand its current state.
    * Convert all entries in the "country" column to lowercase.
    * Remove any leading or trailing whitespaces from the "country" column entries.
    * Clean up the "country" column further so that there are only three distinct country names remaining.

3.  **Transform 'date_measured' column:**
    * Create a new column in the DataFrame called `days_ago`.
    * This new column should be a copy of the "date_measured" column, but its values should represent the number of days ago that the measurement was taken.
    * *Hint:* The current date can be obtained using `datetime.date.today()`.
  
### Libraries:

* `pandas`
* `numpy`
* `fuzzywuzzy`
* `datetime`
