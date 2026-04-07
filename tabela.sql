CREATE DATABASE sistema;
use sistema;
CREATE TABLE pessoa (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INTEGER,
    endereco VARCHAR(150),
    territorio VARCHAR(100)
);
CREATE TABLE atendimento (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    pessoa_id INTEGER,
    tipo_violencia VARCHAR(255),
    numero_prontuario VARCHAR(100),
    FOREIGN KEY (pessoa_id) REFERENCES pessoa(id)
);
CREATE TABLE oficio (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    pessoa_id INTEGER,
    descricao VARCHAR(1000),
    orgao_origem VARCHAR(100),
    FOREIGN KEY (pessoa_id) REFERENCES pessoa(id)
);