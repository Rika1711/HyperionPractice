## Compulsory Task 1: K-Means Clustering for Country Data

This task involves performing K-Means clustering on the `Country-data.csv` dataset to group countries based on various socio-economic indicators.

### Instructions:

* Open the Jupyter notebook named `Kmeans_task.ipynb`.
* Complete all the following steps within this notebook.

### Requirements:

1.  **Load Data:**
    * Load the `Country-data.csv` dataset into a Pandas DataFrame.

2.  **Data Preparation:**
    * Drop any non-numeric columns from the dataset, as K-Means typically operates on numerical features.

3.  **Exploratory Scatter Plots:**
    * Plot nine different scatter plots. Each plot should have 'GDPP' on one axis and a different combination of other numerical variables on the other axis (e.g., 'GDPP' vs 'health', 'GDPP' vs 'income', etc.).
    * In a markdown cell or comment, note which of these plots visually appears most promising for separating the data into distinct clusters.

4.  **Data Normalization:**
    * Normalize the entire dataset (after dropping non-numeric columns) using `MinMaxScaler` from `sklearn.preprocessing`. This ensures that all features contribute equally to the clustering process, regardless of their original scale.

5.  **Determine Optimal Clusters:**
    * Find the optimal number of clusters (`k`) for the scaled data using both the **elbow method** (e.g., plotting inertia) and the **silhouette score method**. Visualize the results of both methods to justify your choice of `k`.

6.  **Fit K-Means Model:**
    * Fit the K-Means model (using `sklearn.cluster.KMeans`) to the **scaled dataset** with the optimal number of clusters determined in the previous step.
    * Report the silhouette score of the final fitted model.

7.  **Visualize Clusters:**
    * Visualize the clusters for the following two specific groups of variables using scatter plots:
        * 'child_mort' vs 'GDPP'
        * 'inflation' vs 'GDPP'
    * Ensure the points in these scatter plots are colored or marked according to their assigned cluster.

8.  **Label Clusters and Justify:**
    * Based on the characteristics of the countries within each cluster (considering 'child_mortality', 'GDPP', and 'inflation'), label the groups of countries in the plots you created.
    * You may use terms such as: "least developed", "developing", and "developed", or "low income", "low-middle income", "upper-middle income", and "high income". Alternatively, you can simply rank them from highest to lowest in terms of development/income.
    * In a markdown cell, **justify the labels you assign to each group**, explaining the reasoning behind your categorization based on the cluster centroids or the range of values for the key indicators within each cluster.
  
  ### Libraries:

  * `numpy`
  * `pandas`
  * `warnings`
  * `os`
  * `matplotlib.pyplot`
  * `seaborn`
  * `sklearn`
  * `collections`
