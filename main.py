from flask import *
from flask_mail import *
from config import DevelopmentConfig
import model



app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_SSL = False,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = 'juncosantiago11@gmail.com',
    MAIL_PASSWORD = 'wohxdaxfqklpdiic',
))
mail = Mail(app)

# mail = Mail()
username = ''

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']

@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('iniciarSesion'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/', methods = ['GET', 'POST'])
def home():
    if 'username' in session:
        enSesion = True
        esAdmin = model.checkAdmin(session['email'])
        if request.method == 'POST':
            idProd = request.form.get('id')
            titulo = request.form.get('titulo')
            descripcion = request.form.get('descripcion')
            precio = request.form.get('precio')
            talle = request.form.get('talle')
            foto = request.form.get('foto')
            foto2 = request.form.get('foto2')
            model.guardar(idProd, titulo, descripcion, precio, session['email'], talle, foto, foto2)
        productos = model.productos()
        return render_template('home.html', sesion = enSesion, admin = esAdmin, listProd = productos)
    productos = model.productos()
    return render_template('home.html',listProd = productos)

@app.route('/miSeleccion', methods = ['GET', 'POST'])
def miSeleccion():
    if request.method == 'POST':
        idProd = request.form.get('id')
        model.quitar(idProd, session['email'])
    productos = model.prodSelec(session['email'])
    cant = len(productos)
    esAdmin = model.checkAdmin(session['email'])
    return render_template('miSeleccion.html', listProd = productos, admin = esAdmin, cantidad = cant)

@app.route('/cat/<cat>', methods = ['GET', 'POST'])
def categorias(cat):
    productos = model.prodCat(cat)
    message = cat
    if 'username' in session:
        esAdmin = model.checkAdmin(session['email'])
        enSesion = True
        if request.method == 'POST':
            idProd = request.form.get('id')
            titulo = request.form.get('titulo')
            descripcion = request.form.get('descripcion')
            precio = request.form.get('precio')
            talle = request.form.get('talle')
            foto = request.form.get('foto')
            foto2 = request.form.get('foto2')
            model.guardar(idProd, titulo, descripcion, precio, session['email'], talle, foto, foto2)
        return render_template('home.html', listProd = productos, sesion = enSesion, admin = esAdmin, message = message)
    return render_template('home.html', listProd = productos, message = message)
    
@app.route('/panelControl')
def panelControl():
    usuarios = model.usuarios()
    return render_template('panelControl.html', lista = usuarios)

@app.route('/registrarse', methods = ['GET', 'POST'])
def registrarse():
    if request.method == "GET":
        return render_template('signup.html', message = "")
    else:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        conf_pwd = request.form['password2']
        verifPass = model.validarPass(password)
        if model.existe(email) is not None:
            message = "Ya existe una cuenta con el email {email}".format(email = email)
            return render_template('signup.html', message = message)
        else:
            if verifPass:
                if password == conf_pwd:
                    message = model.signup(username, password, email)
                    msg = Message('Hola {username}, ¡te damos la bienvenida a Santi Deportes!'.format(username = username), sender = app.config['MAIL_USERNAME'], recipients = [email])
                    msg.html = render_template('email.html', message = 'https://santideportes.up.railway.app/verificado/{email}'.format(email = email), email = email)
                    # msg.html = render_template('email.html', message = 'http://127.0.0.1:5000/verificado/{email}'.format(email = email), email = email)
                    mail.send(msg)
                    paso = 1
                    return render_template('signup.html', message = message, paso = paso)
                else:
                    message = 'Las contraseñas no coinciden'
                    return render_template('signup.html', message = message)
            else:
                message = 'La contraseña no cumple las condiciones mencionadas'
                return render_template('signup.html', message = message)

@app.route('/verificado/<email>')
def verificado(email):
    message = model.verificar(email)
    return render_template('verificacion.html', message = message)

@app.route('/iniciarSesion', methods = ['GET', 'POST'])
def iniciarSesion():
    if request.method == 'POST':
        session.pop('username',None)
        isUser = model.chekUser(request.form['email'])
        if isUser is None:
            message = 'Email incorrecto, por favor intente de nuevo o regístrese'
            return render_template('login.html', message = message)
        elif isUser == 0:
            return render_template('login.html', message = 'Revise su correo para validar su cuenta')
        else:
            if model.checkPwd(request.form['email']) == request.form['password']:
                session['username'] = model.user(request.form['email'])
                session['email'] = request.form['email']
                return redirect(url_for('home'))
            else:
                return render_template('login.html', message = 'Contraseña incorrecta, inténtelo de nuevo')
    return render_template('login.html', message = "")

@app.route('/recuperarContraseña', methods = ['GET', 'POST'])
def recuperarContrasseña():
    if request.method == 'GET':
        return render_template('contraseña.html', desde = 'recup', message = "")
    else:
        email = request.form['email']
        existe = model.existe(email)
        if existe is None:
            message = 'El email {email} no se encuentra registrado'.format(email = email)
            return render_template('contraseña.html', message = message, desde = 'recup')
        else:
            msg = Message('Recuperación de contraseña', sender = app.config['MAIL_USERNAME'], recipients = [email])
            message = 'https://santideportes.up.railway.app/cambioContraseña/{email}'.format(email = email)
            # message = 'http://127.0.0.1:5000/cambioContraseña/{email}'.format(email = email)
            msg.html = render_template('email.html', message = message, desde = 'recup')
            mail.send(msg)
            message = 'Revise su correo para recuperar su contraseña'
            paso = 1
            return render_template('contraseña.html', message = message,  desde = 'recup', paso = paso)

@app.route('/cambioContraseña/<email>', methods = ['GET', 'POST'])
def cambioContraseña(email):
    usuario = model.user(email)
    if request.method == 'GET':
        return render_template('contraseña.html', email = email, usuario = usuario, message = "")
    else:
        password = request.form['password']
        conf_pwd = request.form['password2']
        if model.validarPass(password):
            if password == conf_pwd:
                model.cambioPwd(email, password)
                message = 'La contraseña se cambió correctamente'
                paso = 1
                return render_template('contraseña.html',email = email, message = message, usuario = usuario, paso = paso)
            else:
                message = 'Las contraseñas no coinciden'
                return render_template('contraseña.html',email = email, message = message, usuario = usuario)
        else:
            message = 'La contraseña no cumple las condiciones mencionadas'
            return render_template('contraseña.html',email = email, message = message, usuario = usuario)

@app.route('/pruebas', methods = ['GET', 'POST'])
def pruebas():
    return render_template('pruebas.html')



if __name__ == '__main__':
    mail.init_app(app)
    app.run(port = 5000)