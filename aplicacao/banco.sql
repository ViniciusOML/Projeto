CREATE DATABASE IF NOT EXISTS ope;

USE ope;

CREATE TABLE IF NOT EXISTS pacientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(120),
    dataNascimento DATE,
    cpf CHAR(11),
    sexo CHAR(1),
    createdAt DATETIME DEFAULT NOW(),
    updatedAt DATETIME DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(120),
    senha VARCHAR(250),
    email VARCHAR(120),
    nusp VARCHAR(20),
    createdAt DATETIME DEFAULT NOW(),
    updatedAt DATETIME DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS atendimentos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    id_lif INT NOT NULL,
    data_consulta DATE,
);

CREATE TABLE IF NOT EXISTS lifs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(80),
    createdAt DATETIME DEFAULT NOW(),
    updatedAt DATETIME DEFAULT NOW()
);

CREATE TABLE procedimentos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    sigla VARCHAR(10),
    procedimento CHAR(1) NOT NULL,
    createdAt DATETIME DEFAULT NOW(),
    updatedAt DATETIME DEFAULT NOW()
);

-- 1 BERA
-- 2
-- 3

CREATE TABLE IF NOT EXISTS atendimento_procedimentos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_atendimento INT NOT NULL,
    id_procedimento INT NOT NULL,
    createdAt DATETIME DEFAULT NOW(),
    updatedAt DATETIME DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS atendimento_procedimento_beras (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_atendimento_procedimento INT PRIMARY KEY,
    evolucao TEXT,
    conclusao TEXT,
    createdAt DATETIME DEFAULT NOW(),
    updatedAt DATETIME DEFAULT NOW()
);

-- CREATE TABLE IF NOT EXISTS resultado_beras (
--     id  INT PRIMARY KEY AUTO_INCREMENT,
--     id_atendimento_procedimento_bera INT NOT NULL,
--     direto
-- );