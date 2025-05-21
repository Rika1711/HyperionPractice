# Compulsory Tasks Repository

This repository contains solutions for two compulsory tasks: one involving JSON data manipulation and the other involving XML parsing with Python.

---

## Compulsory Task 1: `books.json`

This task requires the creation of a JSON file named `books.json` containing data about several books.

### Requirements:

* Create a file named `books.json`.
* Populate the file with data for at least 6 books.
* Each book should be represented as a JSON object.
* Each book object must have at least four attributes (e.g., `author`, `year_of_publication`, `title`, `genre`).
* Ensure the JSON string is valid. You can use an online JSON linter/parser to validate it.

### Example `books.json` Structure (Illustrative):

```json
[
  {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "year_of_publication": 1979,
    "genre": "Science Fiction"
  },
  {
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "year_of_publication": 1813,
    "genre": "Classic"
  }
  // ... more books
]
```

## Compulsory Task 2: `taskXML.py`

This task involves creating a Python program to read and process data from an XML file named `movie.xml`.

### Requirements:

* Create a Python program named `taskXML.py`.
* The program must read the contents of an XML file named `movie.xml` (ensure this file is present in the same directory as the Python script).
* Use the `iter()` function (from the `xml.etree.ElementTree` module) to list all child tags of the `movie` element.
* Use the `itertext()` function to print out the descriptions of the movies.
* Calculate and print the number of movies marked as 'favourites' and the number of movies that are not.

### How to Run `taskXML.py`:

1.  Make sure you have a `movie.xml` file in the same directory as `taskXML.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the files.
4.  Run the Python script using the command:
    ```bash
    python taskXML.py
    ```

### Expected Output (Illustrative):

---

**Note:** Ensure that `movie.xml` is properly structured for `taskXML.py` to parse it correctly. A sample `movie.xml` might look like this:

```xml
<movies>
  <movie>
    <title>Movie Title 1</title>
    <description>A thrilling adventure.</description>
    <genre>Action</genre>
    <favourite>yes</favourite>
  </movie>
  <movie>
    <title>Movie Title 2</title>
    <description>A heartwarming story.</description>
    <genre>Drama</genre>
    <favourite>no</favourite>
  </movie>
  </movies>
