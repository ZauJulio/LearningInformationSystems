# Data dictionary

# Table: Loan

| Field name | Key              | Data type | Field Description                             | Field Size (bytes) |
| ---------- | ---------------- | --------- | --------------------------------------------- | ------------------ |
| id         | NOT NULL PRIMARY | BIGINT    | Incremental identifier of the session schema. | 4                  |
| deadline   | NOT NULL         | DATE      | Unique identifier of the book.                | 8                  |
| expedition | NOT NULL         | DATE      | Unit identifier.                              | 8                  |
| cod_book   | NOT NULL FOREIGN | BIGINT    | Reference to a book.                          |                    |
| cod_user   | NOT NULL FOREIGN | BIGINT    | Reference for a user.                         |                    |

# Table: Category

| Field name | Key              | Data type   | Field Description                                 | Field Size (bytes) |
| ---------- | ---------------- | ----------- | ------------------------------------------------- | ------------------ |
| id         | NOT NULL PRIMARY | NUMERIC     | Incremental identifier of the Category schema.    | 4                  |
| name       | NOT NULL         | VARCHAR(50) | Name, can be abbreviated. Limit of 50 characters. | 50                 |

## Table: Operation

| Field name      | Key                  | Data type    | Field Description                                                      | Field Size (bytes) |
| --------------- | -------------------- | ------------ | ---------------------------------------------------------------------- | ------------------ |
| id              | NOT NULL PRIMARY     | INT          | Incremental identifier of the work scheme.                             | 4                  |
| name            | NOT NULL             | VARCHAR(50)  | Name of the employee's operation.                                      | 50                 |
| description     | NOT NULL             | VARCHAR(100) | Description of the employee's operation.                               | 100                |
| day             | NOT NULL             | NUMERIC      | Number corresponding to the day of the week, Sunday - 1: Saturday - 7. | 4                  |
| horary_start    | NOT NULL             | TIME         | Opening hours with time zone.                                          | 12                 |
| horary_end      | NOT NULL             | TIME         | Closing time with time zone.                                           | 12                 |
| workload        | NOT NULL             | NUMERIC      | Employee hourly load.                                                  | 4                  |
| cod_functionary | NOT NULL FOREIGN KEY | INT          | Reference for an employees.                                            |                    |

# Table: Session

| Field name   | Key              | Data type    | Field Description                                  | Field Size (bytes) |
| ------------ | ---------------- | ------------ | -------------------------------------------------- | ------------------ |
| id           | NOT NULL PRIMARY | NUMERIC      | Incremental identifier of the session schema.      | 4                  |
| name         | NOT NULL         | VARCHAR(100) | Name, can be abbreviated. 100 character limit. 100 |
| cod_category | NOT NULL FOREIGN | INT          | Reference to a categorie.                          |                    |
| cod_library  | NOT NULL FOREIGN | INT          | Reference to a library.                            |                    |

# Table: Author

| Field name | Key              | Data type    | Field Description                                  | Field Size (bytes) |
| ---------- | ---------------- | ------------ | -------------------------------------------------- | ------------------ |
| id         | NOT NULL PRIMARY | NUMERIC      | Incremental identifier of the session schema.      | 4                  |
| name       | NOT NULL         | VARCHAR(100) | Name, can be abbreviated. 100 character limit. 100 |

# Table: Publisher

| Field name | Key              | Data type     | Field Description                              | Field Size (bytes) |
| ---------- | ---------------- | ------------- | ---------------------------------------------- | ------------------ |
| id         | NOT NULL PRIMARY | NUMERIC       | Incremental identifier of the session schema.  | 4                  |
| name       | NOT NULL         | VARCHAR(100)  | Name, can be abbreviated. 100 character limit. | 100                |
| cnpj       | NOT NULL         | VARCHAR [14]  | cnpj, in formart "xx.xxx.xxx/xxxx-xx".         | 14                 |
| telephone  | NOT NULL         | VARCHAR [16]  | telephone, international limit.                | 16                 |
| email      | NOT NULL         | VARCHAR [256] | email, default 256 limited size.               | 256                |
| cod_adress | NOT NULL FOREIGN | INT           | Reference to an address.                       |                    |

# Table: Gender

| Field name | Key              | Data type    | Field Description                                  | Field Size (bytes) |
| ---------- | ---------------- | ------------ | -------------------------------------------------- | ------------------ |
| id         | NOT NULL PRIMARY | NUMERIC      | Incremental identifier of the session schema.      | 4                  |
| name       | NOT NULL         | VARCHAR(100) | Name, can be abbreviated. 100 character limit. 100 |

# Table: User

| Field name  | Key              | Data type    | Field Description                                     | Field Size (bytes) |
| ----------- | ---------------- | ------------ | ----------------------------------------------------- | ------------------ |
| id          | NOT NULL PRIMARY | NUMERIC      | Incremental identifier of the session schema.         | 4                  |
| username    | NOT NULL         | VARCHAR(20)  | username, As User Surname. Limit of 20 characters.    | 20                 |
| name        | NOT NULL         | VARCHAR(100) | Name, can be abbreviated. Limit of 100 characters.    | 100                |
| telephone   | NOT NULL         | VARCHAR(16)  | Formatted telephone: "(XX)XXXXX-XXXX" OR LIKE         | 16                 |
| email       | NOT NULL         | VARCHAR(256) | Email following the standard limit of 256 characters. | 256                |
| password    | NOT NULL         | VARCHAR(32)  | Alphanumeric password of up to 32 characters.         | 32                 |
| status      | NOT NULL         | INT          | Validity status for loan.                             | 4                  |
| cod_library | NOT NULL FOREIGN | INT          | Reference for a library.                              |                    |
| cod_adress  | NOT NULL FOREIGN | INT          | Reference to an address.                              |                    |

# Table: Library

| Field name | Key              | Data type   | Field Description                                 | Field Size (bytes) |
| ---------- | ---------------- | ----------- | ------------------------------------------------- | ------------------ |
| name       | NOT NULL         | VARCHAR(50) | Name, can be abbreviated. Limit of 50 characters. | 100                |
| cod_adress | NOT NULL FOREIGN | INT         | Reference to an address.                          |                    |

# Table: Functionary

| Field name | Key              | Data type    | Field Description                                  | Field Size (bytes) |
| ---------- | ---------------- | ------------ | -------------------------------------------------- | ------------------ |
| id         | PRIMARY          | NUMERIC      | Incremental identifier of the employee scheme.     | 4                  |
| name       | NOT NULL         | VARCHAR(100) | Name, can be abbreviated. Limit of 100 characters. | 100                |
| cpf        | NOT NULL         | BIGINT       | CPF with numbers.                                  | 8                  |
| telephone  | NOT NULL         | VARCHAR(16)  | telephone, international limit.                    | 16                 |
| email      | NOT NULL         | VARCHAR(256) | email, default 256 limited size.                   | 256                |
| salary     | NOT NULL         | FLOAT        | Salary with two decimal places.                    | 8                  |
| cod_adress | NOT NULL FOREIGN | INT          | Reference to an address.                           |                    |

# Table: Book

| Field name    | Key              | Data type    | Field Description                               | Field Size (bytes) |
| ------------- | ---------------- | ------------ | ----------------------------------------------- | ------------------ |
| id            | NOT NULL PRIMARY | NUMERIC      | Incremental identifier of the session schema.   | 4                  |
| isbn          | NOT NULL         | NUMERIC      | Unique identifier of the book.                  | 4                  |
| unity         | NOT NULL         | NUMERIC      | Unit identifier.                                | 4                  |
| title         | NOT NULL         | VARCHAR(100) | Book title limited to 100 characters.           | 100                |
| subtitle      |                  | VARCHAR [50] | Sub-title of the book limited to 50 characters. | 50                 |
| status        | NOT NULL         | NUMERIC      | Numeric status.                                 | 4                  |
| cod_gender    | NOT NULL FOREIGN | INT          | Reference to a genre.                           |                    |
| cod_author    | NOT NULL FOREIGN | INT          | Reference for an authors.                       |                    |
| cod_publisher | NOT NULL FOREIGN | INT          | Reference for a publisher.                      |                    |
| cod_category  | NOT NULL FOREIGN | INT          | Reference for a category.                       |                    |

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
