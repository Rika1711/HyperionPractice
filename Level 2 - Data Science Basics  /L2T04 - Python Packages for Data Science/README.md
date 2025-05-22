## Compulsory Task 1: NumPy Array Manipulation

This task involves creating a Python program to explore and manipulate NumPy arrays, addressing common questions and demonstrating various indexing and slicing techniques.

### Instructions:

* Create a new Python program named `numpy_task.py`.
* Add comments within the code to explain your answers and solutions for each question/requirement.

### Questions and Requirements:

1.  **Why doesn't `np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float)` create a two-dimensional array? Write it the correct way.**
    * *Hint: Get familiar with NumPy arrays and how multi-dimensional arrays are constructed.*

2.  **What is the difference between `a = np.array([0, 0, 0])` and `a = np.array([[0, 0, 0]])`?**
    * Explain the difference in terms of array dimensions and shape.

3.  **A 3 by 4 by 4 array is created with `arr = np.linspace(1, 48, 48).reshape(3, 4, 4)`. Index or slice this array to obtain the following specific outputs:**
    * `20.0`
    * `[9. 10. 11. 12.]`
    * `[[33. 34. 35. 36.]`
        ` [37. 38. 39. 40.]`
        ` [41. 42. 43. 44.]`
        ` [45. 46. 47. 48.]]`
    * `[[5. 6.], [21. 22.], [37. 38.]]`
    * `[[36. 35.], [40. 39.], [44. 43.], [48. 47.]]`
    * `[[13. 9. 5. 1.], [29. 25. 21. 17.], [45. 41. 37. 33.]]`
    * `[[1. 4.], [45. 48.]]`
    * `[[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]`

    * *Hint: Look into these NumPy tools:*
        * *Array manipulation routines*
        * *`numpy.linspace`*
        * *`numpy.reshape`*
        * *`numpy.ndarray.flatten`*

### Libraries:

* `numpy`

### How to Run `numpy_task.py`:

1.  Make sure you have NumPy installed (`pip install numpy`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved `numpy_task.py`.
4.  Run the Python script using the command:
    ```bash
    python numpy_task.py
    ```
