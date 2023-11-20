"""
Config DB
"""

#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-

"""
   API REST E-DCP
    base_url = edcp/api/v0.1/
    parametres de configuration de la base de donnée
"""
from flaskext.mysql import MySQL
import logging
from edcp import app



# instance de Mysql (creation d'un objet de connexion Mysql)
mysql = MySQL

# # parametre de connexion Mariadb db a la base de donnée local
# USER_NAME = app.config['MYSQL_DATABASE_USER'] = 'root'
# PASSWORD = app.config['MYSQL_DATABASE_PASSWORD'] = ''
# DB_NAME = app.config['MYSQL_DATABASE_DB'] = 'bd_dcp'
# RDS_HOST = app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# RDS_PORT = app.config['MYSQL_DATABASE_PORT'] = 3306


# parametre de connexion Mariadb db a la base de donnée local
USER_NAME = app.config['MYSQL_DATABASE_USER'] = 'Uroot_edcp'
PASSWORD = app.config['MYSQL_DATABASE_PASSWORD'] = 'e.dcp@2023#'
DB_NAME = app.config['MYSQL_DATABASE_DB'] = 'edcp_db'
RDS_HOST = app.config['MYSQL_DATABASE_HOST'] = 'mariadb'
RDS_PORT = app.config['MYSQL_DATABASE_PORT'] = 3356

# instance logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# bd local
config_local = {
    'host': RDS_HOST,
    'port': RDS_PORT,
    'user': USER_NAME,
    'password': PASSWORD,
    'database': DB_NAME
}
# serveur test
# config = {
#     'host': '172.18.0.3',
#     'port': 3306,
#     'user': 'Uroot_edcp',
#     'password': 'e.dcp@2023#',
#     'database': 'dcp_db'
# }
