from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class CommentForm(Form):

    username= StringField('username',
                        [   validators.Required(message='se nececita ingresar usuario')
                            validators.length(min=4, max = 20, menssage='ingrese un nombre valido') 
                        ]
                        )
    email   = EmailField('Correo Electronico', 
                        [   validators.Required(message='se nececita ingresar un Email')
                            validators.Email(message='Ingrese un Email valido') 
                        ])
    comment = TextField('comentario'
                            validators.length(min=0,max = 100, menssage='el comentario no puede sobrepasar los 10 caracteres') 
                        ])


class ScanForm(Form):


