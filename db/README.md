# Database and Data Import Instructions

Execute `create_tables.sql` query to create the 3 tables: `questions`, `question_options` and `question_answers`. If there is a conflict, delete the previous created tables. Then populate the database following one of the two methods mentioned bellow.

## Folder Contents

This package provides two methods for populating the database:

1. Importing the `.csv` files using an import wizard.
2. Executing SQL queries: `question_answers_insert.sql`, `question_options_insert.sql`, and `question_answers_insert.sql`.

### `data` Folder

Contains the original and processed data in various formats:

- `questions.xls`: This Excel file contains sanitized data split into three sheets - `questions`, `question_options`, and `question_answers`. It serves as the primary source showing the structure and content of the question database.
- `questions.csv`, `question_options.csv`, `question_answers.csv`: These CSV files hold data formatted for direct import into the database via an import wizard.

### `data_statements` Folder

Includes SQL scripts for manual database population:

- `question_answers_insert.sql`: SQL script to populate the `questions` table.
- `question_options_insert.sql`: SQL script to populate the `question_options` table.
- `question_answers_insert.sql`: SQL script to populate the `question_answers` table.

## Database Structure

The database comprises three interconnected tables, each serving a distinct function in managing question data.

### `questions` Table

- `id` (Primary Key, Integer): Unique identifier for each question.
- `subject` (String): The subject or category of the question.
- `type` (String): The format of the question (e.g., 'true or false', 'multiple choice').
- `difficulty` (String): The assessed difficulty level of the question.
- `description` (Text): The full text of the question.

### `question_options` Table

- `id` (Primary Key, Integer): Unique identifier for each option.
- `question_id` (Foreign Key, Integer): Links to `id` in `questions` table, denoting to which question the option belongs.
- `description` (String): The text of the option.

### `question_answers` Table

- `id` (Primary Key, Integer): Unique identifier for each answer.
- `question_id` (Foreign Key, Integer): Links to `id` in `questions` table, indicating the related question.
- `option_id` (Foreign Key, Integer): Links to `id` in `question_options` table, identifying the correct option.

## Algorithm to Retrieve Options and Correct Answer for a Specific Question

### Retrieving Options for a Specific Question

To retrieve the options for a specific question, you can use the following SQL query:

```sql
SELECT qo.id, qo.description
FROM question_options AS qo
JOIN questions AS q ON q.id = qo.question_id
WHERE q.id = [Question ID];
```

Replace `[Question ID]` with the ID of the specific question for which you want to retrieve the options.

### Retrieving the Correct Answer for a Specific Question

To retrieve the correct answer for a specific question, use the following SQL query:

```sql
SELECT qo.id, qo.description
FROM question_answers AS qa
JOIN question_options AS qo ON qa.option_id = qo.id
WHERE qa.question_id = [Question ID];
```

Replace `[Question ID]` with the ID of the specific question for which you want to find the correct answer.
