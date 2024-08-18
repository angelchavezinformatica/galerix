-- Creacion de la base de datos
CREATE DATABASE galerix;
USE galerix;

-- Creacion de tablas

CREATE TABLE usuario(
	id INTEGER NOT NULL AUTO_INCREMENT,
    nombre_usuario VARCHAR(40),
    contrasena VARCHAR(100),
    nombre VARCHAR(200),
    fecha_nacimiento DATE,
    direccion VARCHAR(100),
    PRIMARY KEY (id)
);

CREATE TABLE correo_usuario(
	id_usuario INTEGER NOT NULL,
    correo VARCHAR(256),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

CREATE TABLE foto(
	id INTEGER NOT NULL AUTO_INCREMENT,
    id_usuario INTEGER NOT NULL,
    ruta_archivo VARCHAR(100),
    instante_subida DATETIME,
    titulo VARCHAR(70),
    descripcion VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

CREATE TABLE calificacion(
	id_usuario INTEGER NOT NULL,
    id_foto INTEGER NOT NULL,
    puntaje DECIMAL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_foto) REFERENCES foto(id)
);

CREATE TABLE foto_favorita(
	id_usuario INTEGER NOT NULL,
    id_foto INTEGER NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_foto) REFERENCES foto(id)
);

CREATE TABLE galeria(
	id INTEGER NOT NULL AUTO_INCREMENT,
    id_usuario INTEGER NOT NULL,
    nombre_galeria VARCHAR(70),
    PRIMARY KEY (id),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

CREATE TABLE foto_galeria(
	id_galeria INTEGER NOT NULL,
    id_foto INTEGER NOT NULL,
    FOREIGN KEY (id_galeria) REFERENCES galeria(id),
    FOREIGN KEY (id_foto) REFERENCES foto(id)
);

CREATE TABLE comentario_foto(
	id INTEGER NOT NULL AUTO_INCREMENT,
    id_usuario INTEGER NOT NULL,
    id_foto INTEGER NOT NULL,
    comentario TEXT,
    fecha DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_foto) REFERENCES foto(id)
);

CREATE TABLE pagina(
	id INTEGER NOT NULL AUTO_INCREMENT,
	id_usuario INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

CREATE TABLE blog(
	id INTEGER NOT NULL AUTO_INCREMENT,
    id_pagina INTEGER NOT NULL,
    titulo VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (id_pagina) REFERENCES pagina(id)
);

CREATE TABLE post(
	id INTEGER NOT NULL AUTO_INCREMENT,
    id_blog INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    id_foto INTEGER NOT NULL,
    ruta_post VARCHAR(100),
	publicacion DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY (id_blog) REFERENCES blog(id),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_foto) REFERENCES foto(id)
);

CREATE TABLE comentario_post(
	id INTEGER NOT NULL AUTO_INCREMENT,
    id_post INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    comentario TEXT,
    fecha DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY (id_post) REFERENCES post(id),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
