CREATE IF NOT EXISTS DATABASE ope;

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
    createdAt DATETIME DEFAULT NOW(),
    updatedAt DATETIME DEFAULT NOW()
);