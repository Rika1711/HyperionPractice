## Compulsory Task 1: Iris Classification (Logistic Regression)

This task focuses on building and evaluating a binary logistic regression classifier using the Iris dataset, with an optional extension to a multi-class problem.

### Instructions:

* Begin by reading the `Iris.csv` dataset into a Jupyter notebook.
* Name your notebook `iris_logistic_regression.ipynb`.
* Complete all the following steps within this notebook.

### Requirements:

1.  **Binary Classification Setup:**
    * The objective is to create a classifier that will predict whether an iris belongs to the 'Iris-setosa' class or not. This means you will have two classes: 'Iris-setosa' and 'not Iris-setosa' (which includes 'Iris-versicolor' and 'Iris-virginica').
    * **Identify Independent Variables (`x`):** Determine which columns from the dataset will serve as your features.
    * **Encode Dependent Variable (`y`):** Encode your dependent variable such that 'Iris-setosa' is encoded as `0`, and 'Iris-versicolor' and 'Iris-virginica' are both encoded as `1`. (So, `0` corresponds to the 'Iris-setosa' class, and `1` corresponds to the 'not Iris-setosa' class.)

2.  **Model Training and Prediction:**
    * Split the data into a training and test set.
    * Use `sklearn`'s logistic regression function (`linear_model.LogisticRegression`) to fit a model to your training data.
    * Make predictions on the test set using the fitted model.

3.  **Confusion Matrix Analysis:**
    * Use `sklearn` to generate a confusion matrix, which compares the predicted labels to the actual labels (gold labels).
    * Analyze the confusion matrix and provide a prediction, in a comment within the notebook, whether the model is likely to have higher precision, higher recall, or similar precision and recall for the 'Iris-setosa' class.

4.  **Manual Metric Calculation:**
    * Write your own Python code (without using `sklearn`'s built-in metric functions directly for this step) to calculate the accuracy, precision, and recall based on the confusion matrix.
    * Check whether your prediction from the previous step was correct based on your calculated values.

5.  **(Optional) Three-Class Problem:**
    * Repeat this task, but modify it so that you have all three categories: 'Iris-setosa', 'Iris-versicolor', and 'Iris-virginica', corresponding to the numeric values `0`, `1`, and `2` respectively. This will now be a three-class (multinomial) classification problem.
    * Observe and note how this change impacts the confusion matrix.
  
### Libraries:

* `numpy`
* `pandas`
* `matplotlib.pyplot`
* `sklearn`
