CREATE DATABASE petinder_fase_2;
USE petinder_fase_2;

CREATE TABLE Especies(
    id INT AUTO_INCREMENT,
    nome VARCHAR(250) NOT NULL,
    descricao TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Racas(
    id INT AUTO_INCREMENT,
    nome VARCHAR(250) NOT NULL,
    descricao TEXT NOT NULL,
    id_especie INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (id_especie) REFERENCES Especies(id)
);

CREATE TABLE Animais(
    id INT AUTO_INCREMENT,
    nome VARCHAR(250),
    sexo CHAR NOT NULL,
    idade INT NOT NULL,
    porte VARCHAR(10),
    pelagem VARCHAR(250),
    id_raca INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(id_raca) REFERENCES Racas(id) 
)