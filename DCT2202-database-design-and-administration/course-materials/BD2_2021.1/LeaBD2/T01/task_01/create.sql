drop table if exists empregado cascade;

drop table if exists companhia cascade;

drop table if exists trabalha cascade;

drop table if exists gerente cascade;

CREATE TABLE empregado(
  cod_empregado NUMERIC(4) PRIMARY KEY NOT NULL,
  nome_empregado CHAR(256) NOT NULL,
  rua CHAR(256) NOT NULL,
  cidade CHAR(120) NOT NULL,
  salario FLOAT NOT NULL
);

CREATE TABLE companhia (
  cod_companhia NUMERIC(4) PRIMARY KEY NOT NULL,
  cnpj CHAR(12) UNIQUE NOT NULL,
  nome_companhia CHAR(50) NOT NULL,
  cidade_companhia CHAR(120) NOT NULL
);

CREATE TABLE trabalha (
  cod_empregado NUMERIC(4) PRIMARY KEY NOT NULL,
  cod_companhia NUMERIC(4) NOT NULL,
  CONSTRAINT fk_empregado FOREIGN KEY (cod_empregado) REFERENCES empregado(cod_empregado) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_cod_companhia FOREIGN KEY (cod_companhia) REFERENCES companhia(cod_companhia) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE gerente (
  cod_empregado NUMERIC(4) PRIMARY KEY NOT NULL,
  cod_companhia NUMERIC(4) NOT NULL,
  CONSTRAINT fk_empregado FOREIGN KEY (cod_empregado) REFERENCES empregado(cod_empregado) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_companhia FOREIGN KEY (cod_companhia) REFERENCES companhia(cod_companhia) ON DELETE RESTRICT ON UPDATE CASCADE
);