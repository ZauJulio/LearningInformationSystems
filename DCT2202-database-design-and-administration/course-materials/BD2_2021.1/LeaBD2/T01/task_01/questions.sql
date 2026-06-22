INSERT INTO
  empregado (
    cod_empregado,
    nome_empregado,
    rua,
    cidade,
    salario
  )
VALUES
  (0665,'Vacinelson','Rua Coronais','Santo Antônio',6000),
  (0666,'Luciane','Rua Gregório Vale','Monte Carlo',5000),
  (0667, 'Fulano', 'Av. Coronel das botas', 'São Paulo', 4000),
  (0668, 'Cicano', 'Rua Alvarez Ernandez', 'San Diego', 16500),
  (0669, 'Cigano', 'Rua Gregório Vale', 'Monte Carlo', 3500);

INSERT INTO
  companhia (cod_companhia, cnpj, nome_companhia, cidade_companhia)
VALUES
  (0000, '42343423436', 'LinkApi', 'São Paulo'),
  (0001, '42344662534', 'Vigo', 'caicó'),
  (0002, '68687625767', 'ByteSerido', 'caicó'),
  (0003, '65284578275', 'Soft Sell', 'Natal');

INSERT INTO
  trabalha (cod_empregado, cod_companhia)
VALUES
  (0665, 0002),
  (0667, 0001),
  (0666, 0001),
  (0668, 0003),
  (0669, 0001);

INSERT INTO
  gerente (cod_empregado, cod_companhia)
VALUES
  (0668, 0000),
  (0666, 0001);

--  1
SELECT
  nome_empregado
FROM
  empregado e,
  trabalha t,
  companhia c
WHERE
  c.nome_companhia = 'Soft Sell'
  AND
  e.cod_empregado = t.cod_empregado
  AND
  c.cod_companhia = t.cod_companhia;

--  2
SELECT
  e.cidade
FROM
  empregado e,
  trabalha t,
  companhia c
WHERE
  c.nome_companhia = 'Soft Sell'
  AND
  e.cod_empregado = t.cod_empregado
  AND
  c.cod_companhia = t.cod_companhia;

--  3
SELECT
  e.nome_empregado,
  e.cidade,
  e.rua
FROM
  empregado e,
  companhia c,
  trabalha t
WHERE
  c.nome_companhia = 'Soft Sell'
  AND
  e.cod_empregado = t.cod_empregado
  AND
  c.cod_companhia = t.cod_companhia
  AND
  e.salario > 10000;

--  4
SELECT
  nome_empregado
FROM
  empregado e,
  trabalha t,
  companhia c
WHERE
  e.cod_empregado = t.cod_empregado
  AND
  c.cod_companhia = t.cod_companhia
  AND
  e.cidade = c.cidade_companhia;

--  5
SELECT
  g.cod_empregado as gerente_cod,
  e.cod_empregado as empregado_cod
INTO
  gerente_empregados
FROM
  empregado e,
  trabalha t,
  companhia c,
  gerente g
WHERE
  g.cod_companhia = t.cod_companhia
  AND
  e.cod_empregado = t.cod_empregado;
 
SELECT
  e.cidade,
  e.rua
INTO
  gerente_cidades
FROM
	empregado e,
    gerente_empregados g
WHERE
  e.cod_empregado = g.gerente_cod;

SELECT
  nome_empregado
FROM
  empregado e,
  gerente_empregados g,
  gerente_cidades cg
WHERE
  e.cod_empregado = g.empregado_cod
  AND
  cg.cidade = e.cidade
  AND
  cg.rua = e.rua;

-- CLEAN
drop table if exists gerente_empregados cascade;

drop table if exists gerente_cidades cascade;
-- 

--  6
SELECT
  nome_empregado
FROM
  empregado e,
  trabalha t,
  companhia c
WHERE
  e.cod_empregado = t.cod_empregado
  AND c.nome_companhia NOT IN ('Soft Sell');