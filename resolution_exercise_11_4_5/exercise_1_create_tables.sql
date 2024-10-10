CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE,
    fecha_registro DATE
) CREATE TABLE Categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_categoria TEXT NOT NULL,
    descripcion TEXT
) CREATE TABLE Productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_producto TEXT NOT NULL,
    descripcion TEXT,
    precio INTEGER NOT NULL,
    cantidad_stock INTEGER NOT NULL,
    id_categoria INTEGER NOT NULL,
    Foreign key (id_categoria) REFERENCES Categorias(id)
) CREATE TABLE Ordenes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    fecha_orden DATE NOT NULL,
    total_compra INTEGER NOT NULL,
    Foreign key (id_cliente) REFERENCES Usuarios(id)
) CREATE TABLE OrdenProductos (
    id_orden INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    catidad_comprada INTEGER NOT NULL,
    FOREIGN KEY (id_orden) REFERENCES Ordenes(id),
    FOREIGN KEY (id_producto) REFERENCES Productos(id)
) CREATE TABLE Comentarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_producto INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    texto_comentario TEXT,
    fecha_comentario DATE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id),
    FOREIGN KEY (id_producto) REFERENCES Productos(id)
)