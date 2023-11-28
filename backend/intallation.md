

API REST  E-DCP

## INSTALLATION API REST E-DCP EN LOCAL

- Création de la base de données Mariadb
	- Nom de la base de donnée : ex: bd_dcp
	- paramètres de connexion à la base de donnée:
	>	USER_NAME = app.config['MYSQL_DATABASE_USER'] = 'user_bd'
		PASSWORD = app.config['MYSQL_DATABASE_PASSWORD'] = '' password_bd"
		DB_NAME = app.config['MYSQL_DATABASE_DB'] = 'bd_name'
		RDS_HOST = app.config['MYSQL_DATABASE_HOST'] = 'ip_host'
		RDS_PORT = app.config['MYSQL_DATABASE_PORT'] = port_connexion

- S'assurer que git est installer sur la machine, si non installer git
lien d'installation de git : [https://git-scm.com/downloads](https://git-scm.com/downloads)

- S'assurer que python est installer sur la machine, si non installer python3.10, ou Python3.7
lien d'installation de python : [https://www.python.org/downloads/](https://www.python.org/downloads/)

- S'assurer que pip est installer sur la machine, si non installer pip et pip3
Il s'agit d'un script Python qui utilise une logique d'amorçage pour installer pip:
Téléchargez le script depuis [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py)
Ouvrez un terminal/invite de commande `cd`dans le dossier contenant le `get-pip.py`fichier et exécutez :
   >     python  get-pip.py
   >     python get-pip.py
   >     C:> py get-pip.py

- S'assurer que virtualenv est installer sur la machine, si non installer virtualenv
[virtualenv](https://pypi.org/project/virtualenv) est un outil CLI qui nécessite un interpréteur Python pour s'exécuter.
- via le pip ou pipx
>     pipx install virtualenv
>     virtualenv --help
- via python
   python -m pip install --user virtualenv
python -m virtualenv --help
- créer l'environnement virtuel
   >     python -m venv name_env

- Activez l'environnement virtuel
source venv/bin/activate # Pour Linux/Mac
- pour desactiver
   >     deactivate

.\venv\Scripts\activate # Pour Windows

- Cloner le depôt du projet depuis la plateforme Github
   >      git clone -b api_edcp [https://github.com/saint0101/e_dcp.git](https://github.com/saint0101/e_dcp.git)

-  se deplacer dans le dossier backend/
installer les dependances
   >     pip install -r requirements.txt
   >     python -m pip install -r requirements.txt

- lancer l'application
   >     python app.py

- Accéder à l'application dans le navigateur :

Ouvrez votre navigateur et accédez à l'URL
[http://127.0.0.1:5500/](http://127.0.0.1:5000/)
 ou
[http://localhost:5500/](http://localhost:5000/)