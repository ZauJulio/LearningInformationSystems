DROP DATABASE IF EXISTS`db_library`;
CREATE SCHEMA db_library
	CHARACTER SET 'utf8'
    COLLATE 'utf8_unicode_ci';

use db_library;
SET time_zone = 'UTC';


CREATE TABLE address (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    street VARCHAR(50) NOT NULL,
    neighborhood VARCHAR(50),
    zipcode NUMERIC NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(5) NOT NULL,
    country VARCHAR(50) NOT NULL,
    number NUMERIC NOT NULL
);

CREATE TABLE library (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL,
    cod_address INT NOT NULL,
    CONSTRAINT fk_library_address FOREIGN KEY (cod_address)
        REFERENCES address (id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE author (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE gender (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE publisher (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    telephone VARCHAR(16) NOT NULL,
    email VARCHAR(256) NOT NULL,
    cod_address INT NOT NULL,
    CONSTRAINT fk_publisher_address FOREIGN KEY (cod_address)
        REFERENCES address (id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE book (
    id BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    isbn BIGINT NOT NULL,
    unity BIGINT NOT NULL,
    title VARCHAR(100) NOT NULL,
    subtitle VARCHAR(50),
    status NUMERIC NOT NULL,
    cod_author INT NOT NULL,
    cod_publisher INT NOT NULL,
    cod_gender INT NOT NULL,
    cod_category INT NOT NULL,
    CONSTRAINT fk_book_category FOREIGN KEY (cod_category)
        REFERENCES category (id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_book_gender FOREIGN KEY (cod_gender)
        REFERENCES gender (id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_book_publisher FOREIGN KEY (cod_publisher)
        REFERENCES publisher (id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_book_author FOREIGN KEY (cod_author)
        REFERENCES author (id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE functionary (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL,
    cpf BIGINT NOT NULL,
    telephone VARCHAR(16) NOT NULL,
    email VARCHAR(256) NOT NULL,
    salary FLOAT NOT NULL,
    cod_address INT NOT NULL,
    CONSTRAINT fk_functionary_address FOREIGN KEY (cod_address)
        REFERENCES address (id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE operation (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(100) NOT NULL,
    day NUMERIC NOT NULL,
    horary_start TIME NOT NULL,
    horary_end TIME NOT NULL,
    workload NUMERIC NOT NULL,
    cod_functionary INT NOT NULL,
    cod_library INT NOT NULL,
    CONSTRAINT fk_operation_functionary FOREIGN KEY (cod_functionary)
        REFERENCES functionary (id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_operation_library FOREIGN KEY (cod_library)
        REFERENCES library (id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE user (
    id BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    username VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    telephone VARCHAR(16) NOT NULL,
    email VARCHAR(256) NOT NULL,
    password VARCHAR(32) NOT NULL,
    status INT NOT NULL,
    cod_address INT NOT NULL,
    cod_library INT NOT NULL,
    CONSTRAINT fk_user_address FOREIGN KEY (cod_address)
        REFERENCES address (id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_user_library FOREIGN KEY (cod_library)
        REFERENCES library (id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE loan (
    id BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    deadline DATE NOT NULL,
    expedition DATE NOT NULL,
    cod_book BIGINT NOT NULL,
    cod_user BIGINT NOT NULL,
    CONSTRAINT fk_loan_book FOREIGN KEY (cod_book)
        REFERENCES book (id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_loan_user FOREIGN KEY (cod_user)
        REFERENCES user (id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE session (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL,
    cod_category INT NOT NULL,
    cod_library INT NOT NULL,
    CONSTRAINT fk_session_category FOREIGN KEY (cod_category)
        REFERENCES category (id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_session_library FOREIGN KEY (cod_library)
        REFERENCES library (id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

INSERT INTO address(id, street, neighborhood, zipcode, city, state, country, number)
  VALUES
    (NULL, "Rua João Pedro", NULL, 59300000, "Caíco", "RN", "Brasil", 35),
    (NULL, "Av Pedro Augosto", NULL, 39840923, "João Pessoa", "PB", "Brasil", 64),
    (NULL, "Rua Roraraima Braga", NULL, 56632236, "Bentinho", "RS", "Brasil", 5643),
    (NULL, "Av Júlio César", NULL, 62353000, "São Paulo", "SP", "Brasil", 543),
    (NULL, "Rua João Gomes", NULL, 24323674, "Natal", "RN", "Brasil", 85)
;

INSERT INTO author(id, name)
  VALUES
    (NULL, "João"),
    (NULL, "Maria"),
    (NULL, "Pedro"),
    (NULL, "Júlio"),
    (NULL, "Emanuel")
;

INSERT INTO gender(id, name)
  VALUES
    (NULL, "Ação"),
    (NULL, "Filosofia"),
    (NULL, "Fantasia"),
    (NULL, "Matemática"),
    (NULL, "Aventura")
;

INSERT INTO category (id, name)
  VALUES
    (NULL, "Matemática"),
    (NULL, "Engenharia"),
    (NULL, "História"),
    (NULL, "Filosofia"),
    (NULL, "Ajuda")
;

INSERT INTO author(id, name)
  VALUES
    (NULL, "João"),
    (NULL, "Maria"),
    (NULL, "Pedro"),
    (NULL, "Júlio"),
    (NULL, "Emanuel")
;

INSERT INTO library (id, name, cod_address)
  VALUES
    (NULL, "Biblioteca Maria Texeira", 1),
    (NULL, "Biblioteca Municipal", 2),
    (NULL, "Biblioteca Pedro Alvez", 5),
    (NULL, "Biblioteca João&Maria", 3),
    (NULL, "Biblioteca Carlos Cabral", 4)
;

INSERT INTO publisher(id, name, cnpj, telephone, email, cod_address)
  VALUES
    (NULL, "Iluz", "65.500.846/0001-36","(84)2344-3443", "iluz@edt.com", 1),
    (NULL, "PubEdit", "79.985.005/0001-70","(84)6453-4543", "pubEdit@gmail.com", 4),
    (NULL, "Kabum", "70.067.312/0001-06","(84)5329-3783", "kabum@hyper.com", 2),
    (NULL, "Porto", "17.508.480/0001-07","(84)0993-3443", "porto@uol.com", 5),
    (NULL, "Mega", "65.202.121/0001-61","(84)4928-1243", "mega@mega.editor.com", 3)
;

INSERT INTO book(id, cod_author, cod_publisher, isbn, unity, title, subtitle, status, cod_gender, cod_category)
  VALUES
    (NULL, 1, 3, 9788541106993, 1, "Aleatório", NULL, 0, 1, 4),
    (NULL, 2, 2, 7968525816632, 1, "História é tudo que me deixou", NULL, 0, 2, 1),
    (NULL, 2, 4, 8373571800587, 1, "Vermelho, Branco e Sangue Azul", NULL, 0, 3, 2),
    (NULL, 3, 1, 5614827216374, 1, "15 Dias", NULL, 0, 4, 5),
    (NULL, 4, 5, 2125251257992, 1, "Entre o Céu e o Inferno", NULL, 0, 5, 5)
;

INSERT INTO functionary(id, name, cpf, telephone, email, salary, cod_address)
  VALUES
    (NULL, "Gustavo", 11122233344, "(32)5198-2394", "gustavo@email.com", 1500, 4),
    (NULL, "Augusto", 43773475645, "(34)1938-4324", "augusto@oul.com", 2000, 3),
    (NULL, "Xuxa", 73575645645, "(47)7246-4534", "xuxa@outlook.com", 1500, 2),
    (NULL, "Mário", 52513523552, "(34)4534-5624", "mário@gmail.com", 3500, 1),
    (NULL, "Sonic", 42534555325, "(54)4366-5452", "sonic@email.com", 4750, 5);
;

INSERT INTO operation(id, cod_functionary, name, description, day, horary_start, horary_end, workload, cod_library)
  VALUES
    (NULL, 1, "Limpeza", "Realiza limpeza dos andares inferiores", 1,"08:00:00", "18:00:00", 50, 3),
    (NULL, 2, "Atendente", "Atendimento", 2,"08:00:00", "12:00:00", 20, 4),
    (NULL, 3, "Devolução", "Gestão de devolução", 5,"08:00:00", "13:00:00", 25, 2),
    (NULL, 4, "Empréstimo", "Gestão de empréstimos", 3,"08:00:00", "18:00:00", 50, 5),
    (NULL, 5, "Fornecimento", "Recebimento de novos livros", 4,"08:00:00", "17:00:00", 45, 1)
;

INSERT INTO session (id, name, cod_category, cod_library)
  VALUES
    (NULL, "Estrangeiros", 1, 3),
    (NULL, "Brasileiros", 4, 2),
    (NULL, "Antigos", 3, 1),
    (NULL, "Clássicos", 5, 4),
    (NULL, "Jovem", 2, 5)
;

INSERT INTO user(id, username, name, telephone, email, password, status, cod_address, cod_library)
  VALUES
    (NULL, "joazinho", "João Alvez", "(23)3592-5213", "joaozinho@gmail.com", "2941ehijd1", 0, 1, 2),
    (NULL, "pedrinho", "Pedro Gomes", "(23)4398-5533", "pedrinho@gmail.com", "t3ccr2x", 0, 2, 4),
    (NULL, "amemIrmao", "Maria Silva", "(23)3492-6713", "amemIrmao@gmail.com", "3v4c2x", 0, 3, 1),
    (NULL, "davi22", "Bruno Costa", "(23)9562-5273", "davi22@gmail.com", "5b2vc52", 0, 4, 5),
    (NULL, "megaVic", "Victor Luiz", "(23)3652-4533", "megaVic@gmail.com", "senha", 0, 5, 3)
;
    
INSERT INTO loan(id, deadline, expedition, cod_book, cod_user)
  VALUES
    (NULL, "2021-03-17", "2021-04-17", 1, 2),
    (NULL, "2021-01-17", "2021-02-17", 2, 5),
    (NULL, "2021-04-20", "2021-05-20", 3, 1),
    (NULL, "2022-01-17", "2021-01-17", 4, 3),
    (NULL, "2021-02-01", "2021-03-01", 5, 4)
;


SELECT * FROM
  book,
  author,
  gender,
  publisher,
  functionary,
  operation,
  loan,
  address,
  user,
  library,
  session;