## Compulsory Task 1: Database Concepts and File Analysis

This task covers fundamental database concepts and requires analysis of a given file structure.

### Questions:

1.  **Define each of the following terms:**
    a)  **Data:** Raw, unorganized facts, figures, or symbols that have no inherent meaning until they are processed. Examples include numbers, text, images, or sounds.
    b)  **Field:** A single piece of information or an attribute within a record. It represents a specific category of data, such as a name, an age, or a project code. In a table, fields are columns.
    c)  **Record:** A collection of related fields that describes a single entity or instance. It represents a complete set of information about a particular item, person, or event. In a table, records are rows.
    d)  **File:** A collection of related records that are stored together. Historically, a file often referred to a flat file containing data, but in database contexts, it can refer to a collection of tables or data structures stored on a storage device.

2.  **What is a DBMS and what are its advantages?**
    * **DBMS (Database Management System):** A software system that allows users to define, create, maintain, and control access to a database. It acts as an interface between the database and end-users or application programs, ensuring data consistency, integrity, and security.
    * **Advantages of a DBMS:**
        * **Data Redundancy Control:** Reduces duplication of data, saving storage space and preventing inconsistencies.
        * **Data Consistency:** Ensures that data values are consistent across the database, avoiding conflicting information.
        * **Data Sharing:** Allows multiple users and applications to access and share the same data concurrently.
        * **Data Integrity:** Enforces rules and constraints to ensure the accuracy and reliability of data.
        * **Data Security:** Provides mechanisms for access control, preventing unauthorized access and modifications.
        * **Data Backup and Recovery:** Offers tools for creating backups and restoring data in case of system failures or data loss.
        * **Improved Data Access:** Provides powerful query languages (like SQL) for efficient retrieval and manipulation of data.
        * **Data Independence:** Separates the logical view of data from its physical storage, allowing changes to one without affecting the other.

3.  **Explain the difference between data and information.**
    * **Data:** Raw, unprocessed facts and figures. It is the raw material that, by itself, may not have context or meaning.
        * *Example:* `25`, `John Doe`, `New York`
    * **Information:** Data that has been processed, organized, structured, or presented in a given context to make it meaningful and useful. It provides answers to questions and supports decision-making.
        * *Example:* "John Doe is 25 years old and lives in New York."

4.  **What is metadata?**
    * **Metadata:** "Data about data." It describes the characteristics of data, providing context and information about its structure, meaning, relationships, and origin. Metadata helps in understanding, managing, and using data effectively.
    * *Examples:* The data type of a field (e.g., "text", "integer"), the length of a field, the author of a document, the creation date of a file, or the definition of a table schema.

5.  **Given the file below, answer the following questions:**

    ```
    PROJECT_CODE    PROJECT_MANAGER   MANAGER_PHONE        MANAGER_ADDRESS                 PROJECT_BID_PRICE
    21-5U           Holly Parker      33-5-592000506       180 Boulevard du General, Paris, 64700   $13179975.00
    21-7Y           Jane Grant        0181-898-9909        218 Clark Blvd, London, NW3, TRY    $45423415.00
    25-9T           George Dorts      0181-227-1245        124 River Dr, London, N6, 7YU       $78287312.00
    29-7P           Holly Parker      33-5-592000506       180 Boulevard du General, Paris, 64700   $20883467.00
    ```

    e)  **How many records does the file contain?**
        * The file contains **4 records**. (Each row below the header is a record).

    f)  **How many fields are there per record?**
        * There are **5 fields** per record. (PROJECT_CODE, PROJECT_MANAGER, MANAGER_PHONE, MANAGER_ADDRESS, PROJECT_BID_PRICE).
