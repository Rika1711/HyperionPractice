## Compulsory Task 1: SQL Database Operations

This task involves writing SQL code to create and manipulate a `Student` table, then saving the SQL commands to a text file.

### Instructions:

* **Tool:** Use the JDoodle Online SQL IDE (or any other suitable SQL environment) to write and test your SQL code.
* **File:** Once your code is verified, paste all the SQL commands into a text file and save it in your task folder as `Student.txt`.

### SQL Requirements:

1.  **Create Table:**
    Write SQL code to create a table named `Student` with the following structure. `STU_NUM` must be set as the primary key.

    | Attribute Name | Data Type   |
    | :------------- | :---------- |
    | `STU_NUM`      | `CHAR(6)`   |
    | `STU_SNAME`    | `VARCHAR(15)` |
    | `STU_FNAME`    | `VARCHAR(15)` |
    | `STU_INITIAL`  | `CHAR(1)`   |
    | `STU_STARTDATE`| `DATE`      |
    | `COURSE_CODE`  | `CHAR(3)`   |
    | `PROJ_NUM`     | `INT(2)`    |

2.  **Insert Data:**
    After creating the table, write SQL code to insert the following rows of data into the `Student` table:

    | STU_NUM | STU_SNAME  | STU_FNAME | STU_INITIAL | STU_STARTDATE | COURSE_CODE | PROJ_NUM |
    | :------ | :--------- | :-------- | :---------- | :------------ | :---------- | :------- |
    | 01      | Snow       | Jon       | E           | 2014-04-05    | 201         | 6        |
    | 02      | Stark      | Arya      | C           | 2017-07-12    | 305         | 11       |
    | 03      | Lannister  | Jamie     | C           | 2012-09-05    | 101         | 2        |
    | 04      | Lannister  | Cercei    | J           | 2012-09-05    | 101         | 2        |
    | 05      | Greyjoy    | Theon     | I           | 2015-12-09    | 402         | 14       |
    | 06      | Tyrell     | Margaery  | Y           | 2017-07-12    | 305         | 10       |
    | 07      | Baratheon  | Tommen    | R           | 2019-06-13    | 201         | 5        |

3.  **Select Records by Course Code:**
    Write SQL code that will return all records which have a `COURSE_CODE` of `305`.

4.  **Update Course Code:**
    Write SQL code to change the `COURSE_CODE` to `304` for the student whose `STU_NUM` is `07`.

5.  **Delete Specific Record:**
    Write SQL code to delete the row of the person named Jamie Lannister, who started on 5 September 2012, whose course code is 101 and project number is 2. Use logical operators to include all of the information given in this problem.

6.  **Update Project Number Conditionally:**
    Write SQL code that will change the `PROJ_NUM` to `14` for all students who started before 1 January 2016 and whose `COURSE_CODE` is at least `201`.

7.  **Delete Table:**
    Write SQL code that will delete the `Student` table entirely.
