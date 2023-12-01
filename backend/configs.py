from flaskext.mysql import MySQL
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import secrets


# ----------------------------------Creation de l'api -----------------------------------------------------------------------------------
app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app=app)

# ----------------------------------Creation de la bd-----------------------------------------------------------------------------------
# instance de Mysql (creation d'un objet de connexion Mysql)
mysql = MySQL

# # parametre de connexion Mariadb db a la base de donnée local
# USER_NAME = app.config['MYSQL_DATABASE_USER'] = 'Uroot_edcp'
# PASSWORD = app.config['MYSQL_DATABASE_PASSWORD'] = 'e.dcp@2023#'
# DB_NAME = app.config['MYSQL_DATABASE_DB'] = 'edcp_db'
# RDS_HOST = app.config['MYSQL_DATABASE_HOST'] = 'mariadb'
# RDS_PORT = app.config['MYSQL_DATABASE_PORT'] = 3306

# parametre de connexion Mariadb db a la base de donnée local
USER_NAME = app.config['MYSQL_DATABASE_USER'] = 'root'
PASSWORD = app.config['MYSQL_DATABASE_PASSWORD'] = ''
DB_NAME = app.config['MYSQL_DATABASE_DB'] = 'bd_dcp'
RDS_HOST = app.config['MYSQL_DATABASE_HOST'] = 'localhost'
RDS_PORT = app.config['MYSQL_DATABASE_PORT'] = 3306

# connexion bd
config_local = {
    'host': RDS_HOST,
    'port': RDS_PORT,
    'user': USER_NAME,
    'password': PASSWORD,
    'database': DB_NAME
}

# -----------------------------------------------------------------Creation du jeton de login -------------------------------------------------------------
# definir unne clé secret et cela dans la configuration "jose" génerer une clé aleatoire d'une longeur de 128 bits
app.config['JWT_SECRET_KEY'] = str( secrets.SystemRandom().getrandbits(128))
jwt = JWTManager(app=app)
