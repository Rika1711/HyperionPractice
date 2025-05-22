## Compulsory Task 1: Garden Path Sentences and spaCy NLP

This task involves exploring "garden path sentences" and applying fundamental Natural Language Processing (NLP) techniques like tokenization and Named Entity Recognition (NER) using the spaCy library in Python.

### Instructions:

* Read the introduction about garden path sentences and study a few examples provided on Wikipedia (or other resources).
* Create a new Python file called `garden.py` and save it to your task folder.
* Complete all the following steps within this Python file.

### Requirements:

1.  **Sentence Collection:**
    * Find at least 2 garden path sentences from the web, or create your own.
    * Store these sentences in a Python list called `gardenpathSentences`.
    * Add the following sentences to your `gardenpathSentences` list:
        * "Mary gave the child a Band-Aid."
        * "That Jill is never here hurts."
        * "The cotton clothing is made of grows in Mississippi."

2.  **Tokenization and Named Entity Recognition (NER):**
    * For each sentence in your `gardenpathSentences` list:
        * Tokenize the sentence using spaCy.
        * Perform Named Entity Recognition (NER) on the tokenized sentence.

3.  **Examine and Explain Entities:**
    * Examine how spaCy has categorized entities within each sentence.
    * For any entities that you don't immediately understand, use `spacy.explain()` to look up and print their meaning. For example: `print(spacy.explain("FAC"))`.

4.  **Reflection and Explanation:**
    * At the bottom of your `garden.py` file, write a comment block about two specific entities that you looked up using `spacy.explain()`.
    * For each of these two entities, answer the following questions within your comment:
        * What was the entity (e.g., "FAC") and its explanation that you looked up?
        * Did the entity's explanation make sense in terms of the word or phrase it was associated with in your sentences? Justify your answer.

### Setup and How to Run `garden.py`:

1.  **Install spaCy:**
    If you don't have spaCy installed, open your terminal or command prompt and run:
    ```bash
    pip install spacy
    ```
2.  **Download a spaCy Model:**
    You need a language model for spaCy to perform NER. A common choice is the 'en_core_web_sm' model. Download it by running:
    ```bash
    python -m spacy download en_core_web_sm
    ```
3.  **Run the Python Script:**
    Navigate to the directory where you saved `garden.py` in your terminal or command prompt, and run:
    ```bash
    python garden.py
    ```

### Libraries:

* `spacy`
    
