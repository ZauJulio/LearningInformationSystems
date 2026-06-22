# Data dictionary

# Table: Loan

| Field name | Key              | Data type | Field Description                             | Field Size (bytes) |
| ---------- | ---------------- | --------- | --------------------------------------------- | ------------------ |
| id         | NOT NULL PRIMARY | NUMERIC   | Incremental identifier of the session schema. | 4                  |
| deadline   | NOT NULL         | NUMERIC   | Unique identifier of the book.                | 8                  |
| expedition | NOT NULL         | NUMERIC   | Unit identifier.                              | 8                  |
| loan_book  | NOT NULL FOREIGN | NUMERIC   | Reference to a book.                          |                    |
| loan_user  | NOT NULL FOREIGN | NUMERIC   | Reference for a user.                         |                    |

# Table: Category

| Field name    | Key              | Data type     | Field Description                                      | Field Size (bytes) |
| ------------- | ---------------- | ------------- | ------------------------------------------------------ | ------------------ |
| id            | NOT NULL PRIMARY | NUMERIC       | Incremental identifier of the Category schema.         | 4                  |
| name          | NOT NULL         | VARCHAR [100] | Name, can be abbreviated. Limit of 100 characters. 100 |
| category_book | NOT NULL FOREIGN | NUMERIC       | Reference for a books.                                 |                    |

## Table: Operation

| Field name            | Key                  | Data type | Field Description                                                      | Field Size (bytes) |
| --------------------- | -------------------- | --------- | ---------------------------------------------------------------------- | ------------------ |
| id                    | NOT NULL PRIMARY     | NUMERIC   | Incremental identifier of the work scheme.                             | 4                  |
| day                   | NOT NULL             | NUMERIC   | Number corresponding to the day of the week, Sunday - 1: Saturday - 7. | 4                  |
| horary_start          | NOT NULL             | TIME      | Opening hours with time zone.                                          | 12                 |
| horary_end            | NOT NULL             | TIME      | Closing time with time zone.                                           | 12                 |
| workload              | NOT NULL             | NUMERIC   | Employee hourly load.                                                  | 4                  |
| operation_functionary | NOT NULL FOREIGN KEY | NUMERIC   | Reference for an employees.                                            |                    |

# Table: Session

| Field name       | Key              | Data type     | Field Description                                  | Field Size (bytes) |
| ---------------- | ---------------- | ------------- | -------------------------------------------------- | ------------------ |
| id               | NOT NULL PRIMARY | NUMERIC       | Incremental identifier of the session schema.      | 4                  |
| name             | NOT NULL         | VARCHAR [100] | Name, can be abbreviated. 100 character limit. 100 |
| session_category | NOT NULL FOREIGN | NUMERIC       | Reference to a categorie.                          |                    |

# Table: Author

| Field name | Key              | Data type     | Field Description                                  | Field Size (bytes) |
| ---------- | ---------------- | ------------- | -------------------------------------------------- | ------------------ |
| id         | NOT NULL PRIMARY | NUMERIC       | Incremental identifier of the session schema.      | 4                  |
| name       | NOT NULL         | VARCHAR [100] | Name, can be abbreviated. 100 character limit. 100 |

# Table: Publisher

| Field name | Key              | Data type     | Field Description                                  | Field Size (bytes) |
| ---------- | ---------------- | ------------- | -------------------------------------------------- | ------------------ |
| id         | NOT NULL PRIMARY | NUMERIC       | Incremental identifier of the session schema.      | 4                  |
| name       | NOT NULL         | VARCHAR [100] | Name, can be abbreviated. 100 character limit. 100 |
| cnpj       | NOT NULL         | VARCHAR [14]  | Name, can be abbreviated. 100 character limit. 100 |
| telephone  | NOT NULL         | VARCHAR [16]  | Name, can be abbreviated. 100 character limit. 100 |
| email      | NOT NULL         | VARCHAR [256] | Name, can be abbreviated. 100 character limit. 100 |

# Table: Gender

| Field name | Key              | Data type     | Field Description                                  | Field Size (bytes) |
| ---------- | ---------------- | ------------- | -------------------------------------------------- | ------------------ |
| id         | NOT NULL PRIMARY | NUMERIC       | Incremental identifier of the session schema.      | 4                  |
| name       | NOT NULL         | VARCHAR [100] | Name, can be abbreviated. 100 character limit. 100 |

# Table: User

| Field name   | Key              | Data type        | Field Description                                     | Field Size (bytes) |
| ------------ | ---------------- | ---------------- | ----------------------------------------------------- | ------------------ |
| id           | NOT NULL PRIMARY | NUMERIC          | Incremental identifier of the session schema.         | 4                  |
| username     | NOT NULL         | NUMERIC          | Unique identifier of the book.                        | 8                  |
| name         | NOT NULL         | VARCHAR [100]    | Name, can be abbreviated. Limit of 100 characters.    | 100                |
| registration | NOT NULL         | NUMERIC AUTO INC | Self incremental user registration.                   | 4                  |
| telephone    | NOT NULL         | VARCHAR [14]     | Formatted telephone: (XX) XXXXX-XXXX                  | 14                 |
| email        | NOT NULL         | VARCHAR [256]    | Email following the standard limit of 256 characters. | 256                |
| password     | NOT NULL         | VARCHAR [32]     | Alphanumeric password of up to 32 characters.         | 32                 |
| status       | NOT NULL         | NUMERIC          | Validity status for loan.                             | 4                  |
| user_loan    | NOT NULL FOREIGN | NUMERIC          | Reference for a loan made.                            |                    |
| user_adress  | NOT NULL FOREIGN | NUMERIC          | Reference to an address.                              |                    |

# Table: Library

| Field name        | Key              | Data type | Field Description                  | Field Size (bytes) |
| ----------------- | ---------------- | --------- | ---------------------------------- | ------------------ |
| library_operation | NOT NULL FOREIGN | NUMERIC   | Reference to an operating diagram. |                    |
| library_user      | NOT NULL FOREIGN | NUMERIC   | Reference for a user.              |                    |
| library_session   | NOT NULL FOREIGN | NUMERIC   | Reference for a session.           |                    |

# Table: Functionary

| Field name | Key      | Data type     | Field Description                                  | Field Size (bytes) |
| ---------- | -------- | ------------- | -------------------------------------------------- | ------------------ |
| id         | PRIMARY  | NUMERIC       | Incremental identifier of the employee scheme.     | 4                  |
| name       | NOT NULL | VARCHAR [100] | Name, can be abbreviated. Limit of 100 characters. | 100                |

# Table: Book

| Field name     | Key              | Data type     | Field Description                               | Field Size (bytes) |
| -------------- | ---------------- | ------------- | ----------------------------------------------- | ------------------ |
| id             | NOT NULL PRIMARY | NUMERIC       | Incremental identifier of the session schema.   | 4                  |
| isbn           | NOT NULL         | NUMERIC       | Unique identifier of the book.                  | 4                  |
| unity          | NOT NULL         | NUMERIC       | Unit identifier.                                | 4                  |
| title          | NOT NULL         | VARCHAR [100] | Book title limited to 100 characters.           | 100                |
| subtitle       | NOT NULL         | VARCHAR [50]  | Sub-title of the book limited to 50 characters. | 50                 |
| status         | NOT NULL         | NUMERIC       | Numeric status.                                 | 4                  |
| book_gender    | NOT NULL FOREIGN | NUMERIC       | Reference to a genre.                           |                    |
| book_author    | NOT NULL FOREIGN | NUMERIC       | Reference for an authors.                       |                    |
| book_publisher | NOT NULL FOREIGN | NUMERIC       | Reference for a publisher.                      |                    |

# Table: Address

| Field name   | Key              | Data type    | Field Description                             | Field Size (bytes) |
| ------------ | ---------------- | ------------ | --------------------------------------------- | ------------------ |
| id           | NOT NULL PRIMARY | NUMERIC      | Incremental identifier of the address scheme. | 4                  |
| street       | NOT NULL         | VARCHAR [50] | Street limited to 50 characters.              | 50                 |
| neighborhood | NOT NULL         | VARCHAR [50] | Neighborhood limited to 50 characters.        | 50                 |
| zipcode      | NOT NULL         | NUMERIC      | CEP / Zip code, numeric entry.                | 4                  |
| city ​​      | NOT NULL         | VARCHAR [50] | City name limited to 50 characters.           | 50                 |
| state        | NOT NULL         | VARCHAR [5]  | State acronym up to 5 characters.             | 5                  |
| country      | NOT NULL         | VARCHAR [50] | Country limited to 50 characters.             | 50                 |
| number       | NOT NULL         | NUMERIC      | House number.                                 | 4                  |
