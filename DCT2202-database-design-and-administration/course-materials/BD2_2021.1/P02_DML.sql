-- user(id, name, email, banned);
-- room(id, name, createdIn, closedIn, createBy);
-- message(id, content, sendedIn, userId, roomId);
-- member(id, userId, roomId);
-- usuário -> Sala -> Membro -> Mensagem
INSERT INTO
  userr (id, name, email, banned)
VALUES
  (1, 'Taciano', 'taciano@gmail.com', true),
  (2, 'João', 'joão@gmail.com', false),
  (3, 'Pedro', 'pedro@gmail.com', false),
  (4, 'Lucas', 'lucas@gmail.com', true),
  (5, 'Paulo', 'paulo@gmail.com', false),
  (6, 'Marcos', 'marcos@gmail.com', false),
  (7, 'Rafael', 'rafael@gmail.com', false);

INSERT INTO
  room (id, name, created_at, closed_at, fk_user_id)
VALUES
  (1, 'Sala 1', '2021-01-10', '2021-01-11', 1),
  (2, 'Sala 2', '2021-05-08', '2021-05-09', 2),
  (3, 'Sala 3', '2021-06-12', '2021-06-13', 3),
  (4, 'Sala 4', '2021-08-02', '2021-08-03', 4),
  (5, 'Sala 5', '2021-08-04', '2021-08-05', 5),
  (6, 'Sala 6', '2021-08-04', '2021-08-05', 6),
  (7, 'Sala 7', '2021-08-04', NULL, 7);

INSERT INTO
  member (id, fk_user_id, fk_room_id)
VALUES
  (1, 1, 1),
  (2, 2, 1),
  (3, 3, 3),
  (4, 4, 1),
  (5, 5, 2),
  (6, 6, 2),
  (7, 6, 7),
  (8, 4, 7),
  (9, 7, 7);

INSERT INTO
  message (id, content, sended_at, fk_user_id, fk_room_id)
VALUES
  (1, 'Olá, tudo bem?', '2021-08-11', 1, 1),
  (
    2,
    'Alguém expulsa Taciano da sala?',
    '2021-08-11',
    2,
    1
  ),
  (3, 'Pronto', '2021-08-11', 3, 3),
  (4, 'Bem melhor', '2021-08-11', 4, 1),
  (5, 'Menos atividade', '2021-08-11', 5, 2),
  (6, 'Amém', '2021-08-11', 6, 2),
  (7, 'Bem melhor', '2021-08-11', 7, 7),
  (8, 'Qual o próximo?', '2021-08-11', 7, 7),
  (
    9,
    'Coloca ele de novo e expulsa',
    '2021-08-11',
    6,
    7
  );

-- 2- Escreva 15 consultas para o banco de dados do seu projeto (em português).
-- 2.1 - Selecionar todos os usuários que não estão banidos.
-- 2.2 - Selecionar todos os usuários que criaram uma sala.
-- 2.3 - Selecionar todos os usuários que são membros de uma sala e que não são membros de outra sala.
-- 2.4 - Selecionar todos os usuários que são membros de uma sala, que tenham postado ao menos uma mensagem.
-- 2.5 - Selecionar todas as salas que são de um dia específico.
-- 2.6 - Selecionar todas as salas que estão abertas.
-- 2.7 - Selecionar todas as salas que estão fechadas.
-- 2.8 - Selecionar todos os usuários que são membros de salas que ainda não foram fechadas.
-- 2.9 - Selecionar todas as mensagens de usuários que não foram banidos.
-- 2.10 - Selecionar todas as mensagens de usuários que foram banidos.
-- 2.12 - Selecionar todas as mensagens que foram enviadas por um usuário específico.
-- 2.13 - Selecionar todos os usuários que são membros de salas abertas, que não tenham postado ao menos uma mensagem.
-- 2.14 - Selecionar todas as salas criadas por um usuário específico.
-- 2.15 - Selecionar todas as salas criadas por usuários banidos de outras salas.
-- 3- Faça um script de consulta DML com pelo menos 10 consultas e 5 delas utilizando junção e subconsultas;
-- 2.1 - Selecionar todos os usuários que não estão banidos.
SELECT
  name,
  email
FROM
  userr
WHERE
  NOT banned;

-- 2.2 - Selecionar todos os usuários que criaram uma sala.
SELECT
  userr.name,
  email
FROM
  userr,
  room
WHERE
  fk_user_id = userr.id;

-- 2.6 - Selecionar todas as salas que estão abertas.
SELECT
  name,
  fk_user_id
FROM
  room
WHERE
  closed_at IS NULL;

-- 2.7 - Selecionar todas as salas que estão fechadas.
SELECT
  name,
  fk_user_id
FROM
  room
WHERE
  closed_at IS NOT NULL;

-- 2.8 - Selecionar todos os usuários que são membros de salas que ainda não foram fechadas.
SELECT
  userr.name,
  email
FROM
  userr,
  member,
  room
WHERE
  room.id = member.fk_room_id
  AND room.closed_at IS NULL
  AND userr.id = member.fk_user_id;

-- 2.10 - Selecionar todas as mensagens de usuários que foram banidos.
SELECT
  message.content,
  message.sended_at,
  userr.name,
  userr.email
FROM
  userr
  INNER JOIN message ON userr.id = message.fk_user_id
WHERE
  userr.banned;

