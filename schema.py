import sqlite3

connection = sqlite3.connect('catalogo.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(30) NOT NULL,
        password VARCHAR(16) NOT NULL,
        email VARCHAR(30) NOT NULL,
        validado INTEGER,
        admin INTEGER,
        UNIQUE(email)
    );"""
)

cursor.execute(
    """CREATE TABLE productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo VARCHAR(50),
        descripcion TEXT,
        precio REAL,
        categoria TEXT,
        talle TEXT,
        foto TEXT,
        foto2 TEXT
    );"""
)

cursor.execute(
    """CREATE TABLE seleccion(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        idProducto INTEGER,
        titulo VARCHAR(50),
        descripcion VARCHAR(120),
        precio REAL,
        user TEXT,
        talle TEXT,
        foto TEXT,
        foto2 TEXT
    );"""
)

connection.commit()
cursor.close()
connection.close()