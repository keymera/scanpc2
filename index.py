from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import socket
import re, uuid
import os
import subprocess
import psutil
import string
import os.path
import shutil
import platform
from datetime import date
from datetime import datetime



# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'scanpc'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template ('index1.html')


@app.route('/prueba2')
def prueba2():
    return render_template('prueba2.html')

@app.route('/inventari1o')
def inventario():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM scan')
    data = cur.fetchall()
    cur.close()
    return render_template('inventario.html', contacts = data)

# routes
@app.route('/inventario')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM scan')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        #obtencion del nombre
        hostname = socket.gethostname()
        #obtencion de la IP
        addr = socket.gethostbyname(hostname)
        s = platform.system()
        x = platform.release()
        os = (s + " " + str(x))
        ID = request.form['ID']
        name = request.form['name']
        user = request.form['user']
        area = request.form['area']
        correo = request.form['correo']
        cur = mysql.connection.cursor()
        registro = date.today()
        cur.execute("INSERT INTO scan (ID,name, user,correo, area, addr,os, hostname, registro) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (ID,name, user,correo, area,addr,os,hostname,registro))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM scan WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        #obtencion del nombre
        hostname = socket.gethostname()
        #obtencion de la IP
        addr = socket.gethostbyname(hostname)
        s = platform.system()
        x = platform.release()
        os = x
        name = request.form['name']
        user = request.form['user']
        area = request.form['area']
        #addr = request.form['addr']
        #os = request.form['os']
        cur = mysql.connection.cursor()
        registro = datetime.now
        cur.execute("""
            UPDATE scan
            SET name = %s,
                user = %s,
                area = %s,
                systema = %s,
                addr = %s,
                os = %s,
                hostname = %s,
                registro = %s,
            WHERE id = %s
        """, (name, user, area, id,addr,os,hostname))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM scan WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))


@app.route('/register')
def register():
    #crar cuenta
    return render_template('register.html')

@app.route('/login')
def login():
    #login de usuario
    return render_template('dashboard.html')


@app.route('/logout')
def logout():
    #cerrar sesion
    return 'adios'

@app.route('/list_device')
def list_device():
    #lista de esquipos PC/notebook/server
    return 'lista de equipos'
    

@app.route('/profile')
def profile():
    #perfil
    return 'perfil'


# starting the app
if __name__ == "__main__":
    app.run(port=4000, debug=True)