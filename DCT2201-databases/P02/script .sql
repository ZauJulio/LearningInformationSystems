-- Aluno: Zaú Júlio A. Galvão
-- Matricula: 20190022453

-- 1
-- CHARACTER SET = Defini a códificação dos dados.
-- COLLATE = São as regras para comparar e classificar
-- conjuntos de caracteres.
CREATE SCHEMA db_banco
	CHARACTER SET 'utf8'
    COLLATE 'utf8_unicode_ci';

-- 2
use db_banco;

-- Zona temporal
SET time_zone = 'UTC';

CREATE TABLE banco (
    codigo INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE agencia (
    numero_agencia INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    cod_banco INT NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    CONSTRAINT fk_cod_agencia_banco FOREIGN KEY (cod_banco)
        REFERENCES banco (codigo)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Caso um banco seja deletado não a motivos para armazenar
-- informações de agência, cliente, conta e etc. Caso seja atualizado
-- deve-se atualizar as demais tabelas.

CREATE TABLE cliente (
    cpf BIGINT PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    sexo VARCHAR(5) NOT NULL,
    endereco VARCHAR(100) NOT NULL
);

CREATE TABLE conta (
    numero_conta INT PRIMARY KEY NOT NULL,
    saldo FLOAT NOT NULL,
    tipo_conta VARCHAR(5) NOT NULL,
    cod_banco INT NOT NULL,
    num_agencia INT NOT NULL,
    CONSTRAINT fk_num_agencia FOREIGN KEY (num_agencia)
        REFERENCES agencia (numero_agencia)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_cod_banco FOREIGN KEY (cod_banco)
        REFERENCES banco (codigo)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Caso uma agência seja apagada uma conta deve ser
-- re-alocada para continuar existindo, e caso seja
-- atualizada deve ser aplicada as demais tabelas,
-- assim como a atualização e remoção do banco.

CREATE TABLE historico (
    cpf BIGINT PRIMARY KEY NOT NULL,
    num_conta INT NOT NULL,
    data_inicio DATE NOT NULL,
    CONSTRAINT fk_cpf FOREIGN KEY (cpf)
        REFERENCES cliente (cpf)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_num_conta FOREIGN KEY (num_conta)
        REFERENCES conta (numero_conta)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Nesse caso especifico todas as alterações, de todas
-- as dependências estrangeiras(cliente e conta) devem
-- ser reproduzidas nas tabelas dependentes.

CREATE TABLE telefone_cliente (
    cpf BIGINT PRIMARY KEY NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    CONSTRAINT fk_cpf_tel_cliente FOREIGN KEY (cpf)
        REFERENCES cliente (cpf)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Nesse caso todas as alterações em cliente também
-- devem ser reproduzidas nas tabelas dependentes.

-- 3
ALTER TABLE cliente
  ADD COLUMN email VARCHAR(256) NOT NULL;

-- 4
ALTER TABLE historico
  ADD COLUMN data_encerramento DATETIME,
  MODIFY data_inicio DATETIME NOT NULL;

-- 5
RENAME TABLE historico TO conta_cliente;

-- 6
CREATE TABLE transacoes (
    id BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    datahora DATETIME NOT NULL,
    conta_debito INT,
    conta_credito INT,
    valor BIGINT NOT NULL,
    tipo_transacao CHAR NOT NULL,
    descricao VARCHAR(280) NOT NULL
);

-- |                   DESCRIÇÃO SOLICITADA DA QUESTÃO 6                        |
-- ==============================================================================
-- |      ATTR      |     TIPO     |                   MOTIVO                   |
-- | id             | BIGINT       | Alto número de transações                  |
-- | datahora       | DATETIME     | Armazena data e hora                       |
-- | conta_debito   | BIGINT       | Segui o tipo de conta(numero)              |
-- | conta_credito  | BIGINT       | Segui o tipo de conta(numero)              |
-- | valor          | BIGINT       | Alto valor de transações, INT é limitador  |
-- | tipo_transacao | CHAR         | Um único caracter é capaz de identificar   |
-- | descricao      | VARCHAR(280) | Número de caracteres de um twitter         |

-- 7


INSERT INTO banco(codigo, nome) VALUES (NULL, "Banco do Brasil"), (NULL, "CEF");

INSERT INTO agencia(numero_agencia, endereco, cod_banco)
	VALUES
		(0562, "Rua Joaquim Texeira Alves, 1555", 1),
        (3153, "Av. Marcelino Pires, 1960", 2);

INSERT INTO cliente(cpf, nome, sexo, endereco, email)
	VALUES
		(11122233344, "Jennifer B Souza", "F", "Rua Cuiabá, 1050", "jenn.b@gmail.com"),
        (55544477733, "Caetano K Lima", "M", "Rua Ivinhema, 879", "caetano.nao.veloso@uol.com"),
        (66677788899, "Silvia Macedo", "F", "Rua Estados Unidos, 735", "silvia.mado@outlook.com");

INSERT INTO conta(numero_conta, saldo, tipo_conta, num_agencia, cod_banco)
	VALUES
		(863402, 763.05, 2, 3153, 1),
        (235847, 3879.12, 1, 0562, 2);

INSERT INTO telefone_cliente(cpf, telefone)
	VALUES
		(11122233344, "(67)3422-7788"),
        (55544477733, "(67)3423-9900"),
        (66677788899, "(67)8121-8833");

INSERT INTO conta_cliente(cpf, num_conta, data_inicio)
	VALUES
		(11122233344, 235847, '1997-12-17 02:55:05'),
        (55544477733, 235847, '1997-12-17 02:55:05'),
        (66677788899, 863402, '2010-11-29 13:15:20');

-- 8

INSERT INTO conta(numero_conta, saldo, tipo_conta, num_agencia, cod_banco)
	VALUES
		(563514, 9999.99, 2, 3153, 1),
        (454613, 248.09, 1, 0562, 2);
        
INSERT INTO transacoes(datahora, conta_debito, conta_credito, valor, tipo_transacao, descricao)
	VALUES
		('2021-04-01 02:55:05', 454613, 563514, 250, "s", "Saque de 2500 unidades"),
        ('3189-06-27 16:23:07', 454613, 563514, 100000, "d", "Deposito de 100 mil unidades");

-- Preferi não completar a questão 8.

SELECT * FROM conta;

-- Esse site fornece uma visualização rápida e interessante:
-- https://sqlflow.gudusoft.com/#/

-- SELECT * FROM
--     conta,
--     telefone_cliente,
--     conta_cliente,
--     banco,
--     cliente,
--     agencia,
--     transacoes;