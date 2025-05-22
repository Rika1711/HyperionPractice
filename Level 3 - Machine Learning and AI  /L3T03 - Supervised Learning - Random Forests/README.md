## Compulsory Task: Ensemble Methods for Titanic Survival Prediction

This task extends the previous Decision Trees notebook (`Decision_Trees.ipynb` or `decision_tree_titanic.ipynb` if you renamed it) to implement and compare various ensemble methods (Bagging, Random Forest, and Boosted Trees) for predicting Titanic passenger survival.

### Instructions:

* Continue working in the Jupyter notebook created in the previous task (e.g., `decision_tree_titanic.ipynb`).
* Implement and evaluate the ensemble models as described below.

### Requirements:

1.  **Create Ensemble Models:**
    * Create a **Bagged Tree** model for the Titanic dataset.
    * Create a **Random Forest** model for the Titanic dataset.
    * Create a **Boosted Tree** model (e.g., using AdaBoost or Gradient Boosting from scikit-learn) for the Titanic dataset.
    * Ensure these models are built in a similar way to how you created the regular Classification Tree, using the same prepared data (features and target).

2.  **Feature Importance (Random Forest):**
    * From the trained Random Forest model, determine which of the features (independent variables) contributes the most to predicting whether a passenger survives or not. This can typically be accessed via the `feature_importances_` attribute of the fitted Random Forest classifier.

3.  **Parameter Tuning:**
    * Pick **one** of the ensemble methods (Bagged, Random Forest, or Boosted Tree).
    * Tune its parameters, specifically `n_estimators` (number of trees/estimators) and `max_depth` (maximum depth of individual trees). Experiment with different values to find optimal performance.

4.  **Report and Compare Models:**
    * Report the accuracy of **all** models you have created (Bagged, Random Forest, Boosted, and the tuned ensemble model).
    * Report which model performed the best on your evaluation set (e.g., development/test set).
    * Include the specific values for `n_estimators` and `max_depth` that the best-performing model had (if it was one of the tuned models).
  
### Libraries:
  
* `pandas`
* `numpy`
* `seaborn`
* `sklearn`
* `matplotlib`
* `IPython.display`
* `pydot`
