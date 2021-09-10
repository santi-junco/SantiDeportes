import sqlite3
import re

def validarPass(password):
    if 8 <= len(password):
        if re.search('[a-z]', password) and re.search('[A-Z]', password):
            if re.search('[0-9]', password):
                return True
    return False

def signup(username, password, email):
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
            '{username}',
            '{password}',
            '{email}',
            0,
            0
        );""".format(username = username, password = password, email = email)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return 'Por favor revise su correo para validar su cuenta.'

def verificar(email):
    connection = sqlite3.connect('catalogo.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT validado FROM users WHERE email = '{email}';""".format(email = email))
    user = cursor.fetchone()
    if user is None:
        message = 'No se encontró el email {email}, por favor regístrese'.format(email = email)
    else:
        user = user[0]
        if user == 1:
            message = 'Usted ya realizo de manera exitosa la validación de la cuenta, por favor inicie sesión'
        elif user == 0:
            cursor.execute("""UPDATE users SET validado = 1 WHERE email = '{email}';""".format(email = email))
            message = "Validación de la cuenta exitosa, inicie sesión para continuar"

    connection.commit()
    cursor.close()
    connection.close()
    return message

def chekUser(email):
    connection = sqlite3.connect('catalogo.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT validado FROM users WHERE email = '{email}';""".format(email = email))
    user = cursor.fetchone()
    if user is None:
        connection.commit()
        cursor.close()
        connection.close()
    else:
        user = user[0]
        connection.commit()
        cursor.close()
        connection.close()
        return user

def checkPwd(email):
    connection = sqlite3.connect('catalogo.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM users WHERE email = '{email}';""".format(email = email))
    pwd = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return pwd

def productos():
    connection = sqlite3.connect('catalogo.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT id, titulo, descripcion, precio, talle, foto, foto2 FROM productos;""")
    produc = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return produc

def prodSelec(email):
    connection = sqlite3.connect('catalogo.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT idProducto, titulo, descripcion, precio, talle, foto, foto2 FROM seleccion WHERE user = '{email}';""".format(email = email))
    produc = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return produc

def prodCat(categoria):
    connection = sqlite3.connect('catalogo.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT id, titulo, descripcion, precio, talle, foto, foto2 FROM productos WHERE categoria = '{categoria}';""".format(categoria = categoria))
    produc = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return produc

def user(email):
    connection = sqlite3.connect('catalogo.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT username FROM users WHERE email='{email}';""".format(email = email))
    username = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return username

def checkAdmin(email):
    connection = sqlite3.connect('catalogo.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT admin FROM users WHERE email='{email}';""".format(email = email))
    admin = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return admin

def usuarios():
    connection = sqlite3.connect('catalogo.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT username, email, admin FROM users;""")
    lista = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return lista
    
def existe(email):
    connection = sqlite3.connect('catalogo.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT 1 FROM users WHERE email = '{email}';""".format(email = email))
    user = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return user

def cambioPwd(email, password):
    connection = sqlite3.connect('catalogo.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""UPDATE users SET password = '{password}' WHERE email = '{email}';""".format(email = email, password = password))
    connection.commit()
    cursor.close()
    connection.close()

def guardar(idProd, titulo, descripcion, precio, email, talle, foto, foto2):
    connection = sqlite3.connect('catalogo.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT 1 FROM seleccion WHERE idProducto = {idProd} AND user = '{email}';""".format(idProd = idProd, email = email))
    exist = cursor.fetchone()
    if exist is None:
        cursor.execute(
            """INSERT INTO seleccion(
                idProducto,
                titulo,
                descripcion,
                precio,
                user,
                talle,
                foto,
                foto2
            )VALUES(
                '{idProd}',
                '{titulo}',
                '{descripcion}',
                {precio},
                '{email}',
                '{talle}',
                '{foto}',
                '{foto2}'
            );""".format(idProd = idProd, titulo = titulo, descripcion = descripcion, precio = precio,  email = email, talle = talle, foto = foto, foto2 = foto2)
        )
    connection.commit()
    cursor.close()
    connection.close()

def quitar(idProd, email):
    connection = sqlite3.connect('catalogo.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM seleccion WHERE idProducto = {idProd} AND user = '{email}';""".format(idProd = idProd, email = email))
    connection.commit()
    cursor.close()
    connection.close()
