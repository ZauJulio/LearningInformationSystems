-- Aluno: Zaú Júlio A. Galvão

-- 1 - Faça uma consulta que selecione o nome dos funcionários que recebem salários superiores aos salários pagos no departamento 5.

SELECT nome
FROM Funcionario as f
WHERE f.cod_depto != 5 AND f.salario > (
       SELECT MAX(salario) FROM Funcionario WHERE f.cod_depto = 5
);

-- 17 - Faça uma consulta que selecione o código  e descrição do projeto cujo gerente do departamento que ele faz parte ganhe mais que os outros gerentes de departamento.

SELECT codigo, descricao
FROM Projeto as p 
WHERE p.cod_depto = (
  SELECT codigo
  FROM Departamento as d, Projeto as pe
  WHERE
    pe.cod_depto = d.codigo AND de.cod_gerente = (
    SELECT codigo
    FROM Funcionario as fe
    WHERE fe.salario >= (
      SELECT MAX(salario) FROM Funcionario
    )
  )
);
