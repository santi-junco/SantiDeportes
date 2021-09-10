import sqlite3

connection = sqlite3.connect('catalogo.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password,
        email,
        validado,
        admin
        )VALUES(
            'Santiago',
            'SANTIjunco11',
            'santijunco4@gmail.com',
            1,
            1
        );"""
)

cursor.execute(
    """INSERT INTO productos(
        titulo,
        descripcion,
        precio,
        categoria,
        talle,
        foto,
        foto2
        )VALUES(
            'ZAPATILLA ALL STAR CONVERSE',
            'Color blanca',
            7899,
            'calzados',
            '36 al 40',
            'z1.jpg',
            'z11.jpg'
    );"""
)
cursor.execute(
    """INSERT INTO productos(
        titulo,
        descripcion,
        precio,
        categoria,
        talle,
        foto,
        foto2
        )VALUES(
            'ZAPATILLA ADIDAS',
            'Color negro',
            10000,
            'calzados',
            '39 al 42',
            'z2.jpg',
            'z21.jpg'
    );"""
)
cursor.execute(
    """INSERT INTO productos(
        titulo,
        descripcion,
        precio,
        categoria,
        talle,
        foto,
        foto2
        )VALUES(
            'REMERA ADIDAS',
            'Remera deportiva color azul',
            1230,
            'remeras',
            'M-L-XL',
            'r1.jpg',
            'r11.jpg'
    );"""
)
cursor.execute(
    """INSERT INTO productos(
        titulo,
        descripcion,
        precio,
        categoria,
        talle,
        foto,
        foto2
        )VALUES(
            'ZAPATILLA ASICS',
            'Color blanca y azul',
            8569,
            'calzados',
            '39 al 41',
            'z3.jpg',
            'z31.jpg'
    );"""
)
cursor.execute(
    """INSERT INTO productos(
        titulo,
        descripcion,
        precio,
        categoria,
        talle,
        foto,
        foto2
        )VALUES(
            'REMERA NIKE',
            'Remera deportiva color negra',
            1499.99,
            'remeras',
            'M-L-XL',
            'r2.jpg',
            'r21.jpg'
    );"""
)
cursor.execute(
    """INSERT INTO productos(
        titulo,
        descripcion,
        precio,
        categoria,
        talle,
        foto,
        foto2
        )VALUES(
            'CALZA ADIDAS',
            'Calza color gris',
            8000,
            'pantalones',
            'M-L-XL',
            'p3.jpg',
            'p31.jpg'
    );"""
)
cursor.execute(
    """INSERT INTO productos(
        titulo,
        descripcion,
        precio,
        categoria,
        talle,
        foto,
        foto2
        )VALUES(
            'PANTALON ADIDAS',
            'Short seleccion suplente',
            1250,
            'pantalones',
            'M-L-XL',
            'p2.jpg',
            'p21.jpg'
    );"""
)
cursor.execute(
    """INSERT INTO productos(
        titulo,
        descripcion,
        precio,
        categoria,
        talle,
        foto,
        foto2
        )VALUES(
            'REMERA ADIDAS',
            'Remera classic negra',
            1000,
            'remeras',
            'M-L-XL',
            'r3.jpg',
            'r31.jpg'
    );"""
)
cursor.execute(
    """INSERT INTO productos(
        titulo,
        descripcion,
        precio,
        categoria,
        talle,
        foto,
        foto2
        )VALUES(
            'PANTALON ADIDAS',
            'Joggin color negro',
            12321,
            'pantalones',
            'M-L-XL',
            'p1.jpg',
            'p11.jpg'
    );"""
)

connection.commit()
cursor.close()
connection.close()