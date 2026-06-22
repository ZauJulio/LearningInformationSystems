CREATE TABLE Usuario (
    matricula VARCHAR PRIMARY KEY,
    cpf VARCHAR,
    nome VARCHAR,
    username VARCHAR,
    login VARCHAR,
    password VARCHAR
);

CREATE TABLE Turma (
    id NUMERIC PRIMARY KEY,
    nome VARCHAR,
    periodo NUMERIC,
    monitor VARCHAR
);

CREATE TABLE Admin (
    id NUMERIC,
    fk_Usuario_matricula VARCHAR,
    PRIMARY KEY (id, fk_Usuario_matricula)
);

CREATE TABLE Discente (
    id NUMERIC,
    fk_Usuario_matricula VARCHAR,
    PRIMARY KEY (id, fk_Usuario_matricula)
);

CREATE TABLE Docente (
    id NUMERIC,
    fk_Usuario_matricula VARCHAR,
    PRIMARY KEY (id, fk_Usuario_matricula)
);

CREATE TABLE Monitor (
    id NUMERIC,
    fk_Usuario_matricula VARCHAR,
    fk_Turma_id NUMERIC,
    PRIMARY KEY (id, fk_Usuario_matricula)
);

CREATE TABLE Atendimento (
    id NUMERIC PRIMARY KEY,
    data_hora TIMESTAMP,
    duracao NUMERIC,
    fk_Monitor_id NUMERIC,
    fk_Monitor_fk_Usuario_matricula VARCHAR,
    fk_Turma_id NUMERIC
);

CREATE TABLE Duvida (
    id NUMERIC PRIMARY KEY,
    descricao VARCHAR,
    titulo VARCHAR,
    permitido VARCHAR,
    fk_Atendimento_id NUMERIC,
    fk_Discente_id NUMERIC,
    fk_Discente_fk_Usuario_matricula VARCHAR
);

CREATE TABLE Resposta (
    id NUMERIC PRIMARY KEY,
    titulo VARCHAR,
    permitido BOOLEAN,
    descricao VARCHAR,
    fk_Discente_id NUMERIC,
    fk_Discente_fk_Usuario_matricula VARCHAR,
    fk_Docente_id NUMERIC,
    fk_Docente_fk_Usuario_matricula VARCHAR,
    fk_Monitor_id NUMERIC,
    fk_Monitor_fk_Usuario_matricula VARCHAR,
    fk_Duvida_id NUMERIC
);

CREATE TABLE docente_turma (
    fk_Docente_id NUMERIC,
    fk_Docente_fk_Usuario_matricula VARCHAR,
    fk_Turma_id NUMERIC
);

CREATE TABLE discente_turma (
    fk_Turma_id NUMERIC,
    fk_Discente_id NUMERIC,
    fk_Discente_fk_Usuario_matricula VARCHAR
);

CREATE TABLE atendimento_discente (
    fk_Discente_id NUMERIC,
    fk_Discente_fk_Usuario_matricula VARCHAR,
    fk_Atendimento_id NUMERIC
);

CREATE TABLE duvida_turma (
    fk_Duvida_id NUMERIC,
    fk_Turma_id NUMERIC
);
 
ALTER TABLE Admin ADD CONSTRAINT FK_Admin_2
    FOREIGN KEY (fk_Usuario_matricula)
    REFERENCES Usuario (matricula)
    ON DELETE CASCADE;
 
ALTER TABLE Discente ADD CONSTRAINT FK_Discente_2
    FOREIGN KEY (fk_Usuario_matricula)
    REFERENCES Usuario (matricula)
    ON DELETE CASCADE;
 
ALTER TABLE Docente ADD CONSTRAINT FK_Docente_2
    FOREIGN KEY (fk_Usuario_matricula)
    REFERENCES Usuario (matricula)
    ON DELETE CASCADE;
 
ALTER TABLE Monitor ADD CONSTRAINT FK_Monitor_2
    FOREIGN KEY (fk_Usuario_matricula)
    REFERENCES Usuario (matricula)
    ON DELETE CASCADE;
 
ALTER TABLE Monitor ADD CONSTRAINT FK_Monitor_3
    FOREIGN KEY (fk_Turma_id)
    REFERENCES Turma (id)
    ON DELETE SET NULL;
 
ALTER TABLE Atendimento ADD CONSTRAINT FK_Atendimento_2
    FOREIGN KEY (fk_Monitor_id, fk_Monitor_fk_Usuario_matricula)
    REFERENCES Monitor (id, fk_Usuario_matricula)
    ON DELETE SET NULL;
 
ALTER TABLE Atendimento ADD CONSTRAINT FK_Atendimento_3
    FOREIGN KEY (fk_Turma_id)
    REFERENCES Turma (id)
    ON DELETE SET NULL;
 
ALTER TABLE Duvida ADD CONSTRAINT FK_Duvida_2
    FOREIGN KEY (fk_Atendimento_id)
    REFERENCES Atendimento (id)
    ON DELETE CASCADE;
 
ALTER TABLE Duvida ADD CONSTRAINT FK_Duvida_3
    FOREIGN KEY (fk_Discente_id, fk_Discente_fk_Usuario_matricula)
    REFERENCES Discente (id, fk_Usuario_matricula)
    ON DELETE CASCADE;
 
ALTER TABLE Resposta ADD CONSTRAINT FK_Resposta_2
    FOREIGN KEY (fk_Discente_id, fk_Discente_fk_Usuario_matricula)
    REFERENCES Discente (id, fk_Usuario_matricula)
    ON DELETE CASCADE;
 
ALTER TABLE Resposta ADD CONSTRAINT FK_Resposta_3
    FOREIGN KEY (fk_Docente_id, fk_Docente_fk_Usuario_matricula)
    REFERENCES Docente (id, fk_Usuario_matricula)
    ON DELETE CASCADE;
 
ALTER TABLE Resposta ADD CONSTRAINT FK_Resposta_4
    FOREIGN KEY (fk_Monitor_id, fk_Monitor_fk_Usuario_matricula)
    REFERENCES Monitor (id, fk_Usuario_matricula)
    ON DELETE CASCADE;
 
ALTER TABLE Resposta ADD CONSTRAINT FK_Resposta_5
    FOREIGN KEY (fk_Duvida_id)
    REFERENCES Duvida (id)
    ON DELETE CASCADE;
 
ALTER TABLE docente_turma ADD CONSTRAINT FK_docente_turma_1
    FOREIGN KEY (fk_Docente_id, fk_Docente_fk_Usuario_matricula)
    REFERENCES Docente (id, fk_Usuario_matricula)
    ON DELETE RESTRICT;
 
ALTER TABLE docente_turma ADD CONSTRAINT FK_docente_turma_2
    FOREIGN KEY (fk_Turma_id)
    REFERENCES Turma (id)
    ON DELETE RESTRICT;
 
ALTER TABLE discente_turma ADD CONSTRAINT FK_discente_turma_1
    FOREIGN KEY (fk_Turma_id)
    REFERENCES Turma (id)
    ON DELETE RESTRICT;
 
ALTER TABLE discente_turma ADD CONSTRAINT FK_discente_turma_2
    FOREIGN KEY (fk_Discente_id, fk_Discente_fk_Usuario_matricula)
    REFERENCES Discente (id, fk_Usuario_matricula)
    ON DELETE RESTRICT;
 
ALTER TABLE atendimento_discente ADD CONSTRAINT FK_atendimento_discente_1
    FOREIGN KEY (fk_Discente_id, fk_Discente_fk_Usuario_matricula)
    REFERENCES Discente (id, fk_Usuario_matricula)
    ON DELETE RESTRICT;
 
ALTER TABLE atendimento_discente ADD CONSTRAINT FK_atendimento_discente_2
    FOREIGN KEY (fk_Atendimento_id)
    REFERENCES Atendimento (id)
    ON DELETE SET NULL;
 
ALTER TABLE duvida_turma ADD CONSTRAINT FK_duvida_turma_1
    FOREIGN KEY (fk_Duvida_id)
    REFERENCES Duvida (id)
    ON DELETE SET NULL;
 
ALTER TABLE duvida_turma ADD CONSTRAINT FK_duvida_turma_2
    FOREIGN KEY (fk_Turma_id)
    REFERENCES Turma (id)
    ON DELETE SET NULL;