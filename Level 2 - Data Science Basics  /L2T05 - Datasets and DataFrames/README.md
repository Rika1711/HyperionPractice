## Compulsory Task 1: Dataset Manipulation with Pandas

This task focuses on performing specific data selection and sorting operations using the Pandas library within a Jupyter Notebook.

### Instructions:

* Open the `DatasetsCompulsorytask.ipynb` file.
* Complete the following tasks by writing Python code in the notebook.
* Save your notebook (`DatasetsCompulsorytask.ipynb`) to your task folder for submission.

### Requirements:

1.  **Write the code that performs the action described in the following statements:**
    a.  Select the 'Limit' and 'Rating' columns of the first five observations.
    b.  Select the first five observations with 4 cards.
    c.  Sort the observations by 'Education'. Show users with a high education value first.

2.  **Write a short explanation in the form of a comment for the following lines of code:**
    a.  `df.iloc[:,:]`
    b.  `df.iloc[5:,5:]`
    c.  `df.iloc[:,0]`
    d.  `df.iloc[9,:]`

---

## Compulsory Task 2: Data Reporting with Pandas

This task involves creating a data report by loading data from a text file into a Pandas DataFrame and performing various analytical queries.

### Instructions:

* Open and run the example file for this task (if provided) before attempting this task.
* Open the `Report.ipynb` file in this folder.
* Complete the following tasks by writing Python code in the notebook.
* Save your notebook (`Report.ipynb`) to your task folder for submission.

### Libraries:

* `pandas`

2.  **Write the code needed to produce a report that provides the following information:**
    * Compare the average income based on ethnicity.
    * On average, do married or single people have a higher balance?
    * What is the highest income in our dataset?
    * What is the lowest income in our dataset?
    * How many cards do we have recorded in our dataset? (Hint: use `sum()`)
    * How many females do we have information for vs. how many males? (Hint: use `count()` or `value_counts()`)
