USE exercise_11_4_5;

CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL UNIQUE,
    fecha_registro DATE 
);

CREATE TABLE Categorias (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255)
);

CREATE TABLE Productos (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre_producto VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255),
    precio INTEGER NOT NULL,
    cantidad_stock INTEGER NOT NULL,
    id_categoria INTEGER NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id)
);

CREATE TABLE Ordenes (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_cliente INTEGER NOT NULL,
    fecha_orden DATE NOT NULL, 
    total_compra INTEGER NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Usuarios(id)
);

CREATE TABLE OrdenProductos (
    id_orden INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad_comprada INTEGER NOT NULL,
    FOREIGN KEY (id_orden) REFERENCES Ordenes(id),
    FOREIGN KEY (id_producto) REFERENCES Productos(id)
);

CREATE TABLE Comentarios (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_producto INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    texto_comentario VARCHAR(255),
    fecha_comentario DATE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id),
    FOREIGN KEY (id_producto) REFERENCES Productos(id)
);
