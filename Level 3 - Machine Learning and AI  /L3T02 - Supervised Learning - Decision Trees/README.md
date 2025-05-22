## Compulsory Task 1: Titanic Survival Prediction (Decision Tree)

This task involves building, visualizing, and evaluating a Decision Tree classifier to predict passenger survival on the Titanic, exploring the impact of tree depth on model performance.

### Instructions:

* Use the provided Jupyter notebook named `decision_tree_titanic.ipynb`.
* The `titanic.csv` dataset should already be loaded into this notebook.
* Complete all the following steps within this notebook.

### Requirements:

1.  **Data Preparation:**
    * Select relevant independent variables (features) from the dataset that you believe will help predict survival.
    * Split the data into three sets: a training set, a development (validation) set, and a test set.

2.  **Initial Decision Tree Model:**
    * Create a Decision Tree classifier (using `sklearn.tree.DecisionTreeClassifier`) that can predict the survival of passengers.
    * Initially, do **not** impose any restrictions on the depth of the tree (i.e., let it grow to its full depth).
    * Train this decision tree model on your training data.
    * Make a plot of your trained decision tree to visualize its structure.

3.  **Evaluate Initial Model:**
    * Compute your model's accuracy on the **development set**.

4.  **Explore `max_depth`:**
    * Build new Decision Tree models with different values for the `max_depth` parameter, ranging from `2` to `10`.
    * For each `max_depth` value:
        * Create a plot of the tree.
        * Store the accuracy on both the **training data** and the **development data**.

5.  **Analyze `max_depth` Impact:**
    * Plot a line graph of your training accuracies and another line graph of your development accuracies on the same axes.
    * In a markdown cell in the notebook, write down what shape these lines have (e.g., increasing, decreasing, plateauing, diverging) and what this shape means in terms of model bias and variance (underfitting/overfitting).

6.  **Final Model Evaluation:**
    * Report the accuracy of your final chosen model (based on your `max_depth` analysis) on the **test data**.
  
  ### Libraries:

  * `pandas`
  * `seaborn`
  * `sklearn`
  * `matplotlib`
  * `pydot`
  * `IPython.display`
