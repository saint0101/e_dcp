# -*- encoding: utf-8 -*-

# import the necessary packages
import os
import flask
import json
import mariadb
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
import secrets
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, request
from flask_cors import CORS

# from apiconfig import EndPoints

# Préfixe de l'URL de l'API
api_prefix = "/edcp/api/v0/"
#ENDPOINTS = EndPoints()

# Endpoints de l'API
class EndPoints():
  USERS = api_prefix + "users"
  ORGANISATIONS = api_prefix + "organisations"
  OPTIONS_ENREG = api_prefix + "options-enregistrement"

# creation de l'application
app = flask.Flask(__name__)
app.config["DEBUG"] = True



# config bd
"""
Config DB
"""
config_local = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'edcp-db'
}

# definir unne clé secret et cela dans la configuration "jose" génerer une clé aleatoire d'une longeur de 128 bits
#app.config["JWT_TOKEN_LOCATION"] = ["headers"] # specifying the location of JWT 
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
# app.config['JWT_SECRET_KEY'] = str( secrets.SystemRandom().getrandbits(128))
# !!! TO MODIFY : utilisé à des fins de test pour éviter le changement de la clé de signature des access-token
app.config['JWT_SECRET_KEY'] = "chelton" 
jwt = JWTManager(app=app)

# Function to format telephone number
def format_telephone_number(telephone):
    if telephone and len(telephone) == 10:  # Assuming telephone is a 10-digit number
        return "{}-{}-{}-{}-{}".format(telephone[:2], telephone[2:4], telephone[4:6], telephone[6:8], telephone[8:])
    else:
        return telephone


# Function for format responses
def format_response(status, msg, data):
    return {
        "status_code": status,
        "message": msg,
        "data": data
    }

CORS(app, origins=["http://localhost:*"])

############### TO DELETE
@app.route('/edcp/api/v0/testdb')
def testdb():
    conn = mariadb.connect(**config_local)
    
    cursor = conn.cursor()

    # execution de la requête SQL
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()

    # Fermer la connexion à la base de données
    conn.close()
    
    return jsonify(users), 200

# Exemple de route protégée avec JWT
@app.route('/edcp/api/v0/protected', methods=['GET'])
@jwt_required()
def protected():
    # Récupérer l'identité de l'utilisateur à partir du jeton
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

#####################

@app.route('/edcp/api/v0/description')
def description_edcp_api():
    """
    Description edcp Api
    :return:
    """
    ds_edcp_api = {
        'name': 'E-DCP ApiRest',
        'version': 'v0',
        'Services': {
            'Liste des utilisateurs disponibles': '{base url}-{/edcp/api/v0/users}',
            'Liste des personnes concernees': '{base url}-{/edcp/api/v0/personnes-concernees}',
            'Liste des fondements': '{base url}-{/edcp/api/v0/fondements}',
            'Recher d\'utilisateur en fonction de l\' id': '{base url}-{/edcp/api/v0/users/<int:user_id>}',
            'Liste des rôles disponibles': '{base url}-{/edcp/api/v0/roles}',
            'Liste des Entreprises disponibles': '{base url}-{/edcp/api/v0/entreprises}',
            'Supprimer un utilisateur avec valisation de token': '{base url}-{/edcp/api/v0/users/<int:user_id>}',
            'Créer un utilisateur': '{base url}-{/edcp/api/v0/users}',
            'Générer le token d\'authentification pour un utilisateur': '{base url}-{/edcp/api/v0/login}',
            'recupperer le lgin de l\'utilisateur à partir du token': '{base url}-{/edcp/api/v0/protected}',
        }
    }
    return jsonify(ds_edcp_api), 200


# Route d'authentification (login)
@app.route('/edcp/api/v0/login-email', methods=['POST'])
def login_by_email():
    """Fonction de connexion par email et mot de passe

    @param: objet JSON de type {email: "", passwd: ""}
    @returns: données de connexion de type {access_token: "", user: Object}, lui-même encapsulé dans le format de réponse par défaut
    """
    if not request.is_json:
        # return jsonify({"msg": "La demande n'est pas au format JSON"}), 400
        return format_response(400, "Format de requête JSON invalide", "");

    email = request.json.get('email', None)
    password = request.json.get('passwd', None)

    # connexion a la base de données
    conn = mariadb.connect(**config_local)
    
    cursor = conn.cursor()

    # execution de la requête SQL
    cursor.execute("SELECT * FROM users WHERE email = %s LIMIT 1;", (email, ))
    user = cursor.fetchone()

    # Fermer la connexion à la base de données
    conn.close()

    if user and check_password_hash(user[2], password):
        access_token = create_access_token(identity=user[0])

        # Formatter le numéro de téléphone
        formatted_phone = "{}-{}-{}-{}-{}".format(user[10][:2], user[10][2:4], user[10][4:6], user[10][6:8],
                                                  user[10][8:])

        # Retourner le token et les informations de l'utilisateur
        data = {
            "access_token": access_token,
            "user": {
                "id": user[0],
                "login": user[1],
                "role_id": user[3],
                "avatar": user[4],
                # "createdAt": user[5].strftime("%y-%m-%d"),
                "createdAt": user[5],
                "nom": user[6],
                "prenom": user[7],
                "organisation": user[8],
                "email": user[9],
                "telephone": formatted_phone,
                "fonction": user[11],   
            }
        }
        # return jsonify(data), 200
        return format_response(200, "Connexion réussie.", data)
    else:
        # return jsonify({"msg": "Mauvais identifiant ou mot de passe"}), 401
        return format_response(401, "Identifiant ou mot de passe incorrect.", "")


@app.route('/edcp/api/v0/login-username', methods=['POST'])
def login_by_username():
    """ Geberer le token evc le login et mot de passe """
    if not request.is_json:
        return jsonify({"msg": "La demande n'est pas au format JSON"}), 400

    login = request.json.get('login', None)
    password = request.json.get('passwd', None)

    # connexion a la base de données
    conn = mariadb.connect(**config_local)
    
    cursor = conn.cursor()

    # execution de la requête SQL
    cursor.execute("SELECT * FROM users WHERE login = %s LIMIT 1;", (login, ))
    user = cursor.fetchone()

    # Fermer la connexion à la base de données
    conn.close()

    if user and check_password_hash(user[2], password):
        access_token = create_access_token(identity=user[0])

        # Formatter le numéro de téléphone
        formatted_phone = "{}-{}-{}-{}-{}".format(user[10][:2], user[10][2:4], user[10][4:6], user[10][6:8],
                                                  user[10][8:])

        # Retourner le token et les informations de l'utilisateur
        response = {
            "access_token": access_token,
            "user": {
                "id": user[0],
                "login": user[1],
                "role_id": user[3],
                "nom": user[6],
                "prenom": user[7],
                "organisation": user[8],
                "telephone": formatted_phone,
                "fonction": user[11],
                "createdAt": user[5].strftime("%y-%m-%d"),
            }
        }
        return jsonify(response), 200
    else:
        return jsonify({"msg": "Mauvais identifiant ou mot de passe"}), 401


# Définir la route pour créer un nouvel utilisateur
@app.route('/edcp/api/v0/users', methods=['POST'])
def create_user():
    """
    Créer un nouvel utilisateur
    :return:
    """
    try:
        # Récupérer les données du corps de la requête
        user_data = request.json

        # Connexion à la base de données
        with mariadb.connect(**config_local) as conn:
            with conn.cursor() as cursor:
                # Exécution de la requête SQL pour insérer un nouvel utilisateur
                cursor.execute(
                    "INSERT INTO users (login, passwd, role_id, avatar, nom, prenoms, organisation, email, telephone, fonction, consentement) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                    (user_data['login'], generate_password_hash(user_data['passwd'], method='sha256'), user_data['role_id'], user_data['avatar'], user_data['nom'], user_data['prenoms'],
                     user_data['organisation'], user_data['email'], user_data['telephone'], user_data['fonction'], user_data['consentement'])
                )
                # Confirmer les modifications dans la base de données
                conn.commit()

        # Création de la réponse JSON
        response_data = {
            "status_code": 201,  # Code 201 pour création réussie
            "message": "Inscription effectuée avec succès",
            "data": "OK"
        }
        return jsonify(response_data)
    except mariadb.Error as e:
        # En cas d'erreur, retourner une réponse d'erreur
        error_data = {
            "status_code": 500,
            "message": str(e)
        }
        return jsonify(error_data)
    except Exception as e:
        return json.dumps({'error': str(e)})


# Route pour obtenir la liste des utilisateurs
@app.route('/edcp/api/v0/users', methods=['GET'])
@jwt_required()
def get_all_users():
    """
    lister les utilisateurs disponible
    :return:
    """
    try:
        # connexion a la base de données
        conn =  mariadb.connect(**config_local)
        cursor = conn.cursor()

        # execution de la requête SQL
        # cursor.execute("SELECT * FROM users ;")   # Execution de la requête SQL avec jointure pour récupérer le rôle
        cursor.execute("""
            SELECT u.id, u.login, u.role_id, u.createdAt, u.nom, u.prenom,
                   u.organisation, u.telephone, u.fonction, u.consentement,
                   r.role
            FROM users u
            JOIN roles r ON u.role_id = r.id;
        """)

        rows_data = cursor.fetchall()

        # Fermeture des ressources de la base de données
        cursor.close()
        conn.close()

        # Création de la réponse JSON
        # "createdAt": row[3].strftime("%y-%m-%d-%H-%M"),  # Format the timestamp
        response_data = {
            "status_code": 200,
            "data": [{
                "id": row[0],
                "login": row[1],
                "createdAt": row[3].strftime("%y-%m-%d"),
                "nom": row[4],
                "prenom": row[5],
                "organisation": row[6],
                "telephone": format_telephone_number(row[7]),
                "fonction": row[8],
                "consentement": row[9],
                "role": row[10]
            } for row in rows_data]
        }
        return jsonify(response_data)

    except mariadb.Error as e:
        # En cas d'erreur, retourner une réponse d'erreur
        error_data = {
            "status_code": 500,
            "error": str(e)
        }
        return jsonify(error_data)

    except Exception as e:
        return json.dumps({'error': str(e)})


# Route pour obtenir un utilisateur par son Id
@app.route("/edcp/api/v0/users/<int:user_id>", methods=['GET'])
@jwt_required()
def get_user_by_id(user_id):
    """ afficher un utilisateur en fonctiond de son id"""
    try:
        # connexion a la base de données
        conn =  mariadb.connect(**config_local)
        cursor = conn.cursor()

        # execution de la requête SQL
        cursor.execute("SELECT * FROM users WHERE id=%s;", (user_id,))
        rows_data = cursor.fetchall()

        # Fermeture des ressources de la base de données
        cursor.close()
        conn.close()

        # Création de la réponse JSON
        response_data = {
            "status_code": 200,
            "data": [{
                "id": row[0],
                "login": row[2],
                "role_id": row[3],
                "name": row[6],
                "prenom": row[7],
                "organisation": row[8],
                "telephone": row[10],
                "fonction": row[11],
                "createdAt": row[5],
        }
        for row in rows_data]

        }
        return jsonify(response_data)

    except mariadb.Error as e:
        # En cas d'erreur, retourner une réponse d'erreur
        error_data = {
            "status_code": 500,
            "error": str(e)
        }
        return jsonify(error_data)

    except Exception as e:
        return json.dumps({'error': str(e)})


# url pour supprimer un utilisateur
@app.route('/edcp/api/v0/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    try:
        # Connexion à la base de données
        with mariadb.connect(**config_local) as conn:
            with conn.cursor() as cursor:

                # Exécution de la requête SQL pour supprimer un utilisateur par son ID
                cursor.execute("DELETE FROM users WHERE id = ?;", (user_id,))
                # Confirmer les modifications dans la base de données
                conn.commit()

        # Création de la réponse JSON
        response_data = {
            "status_code": 200,  # Code 200 pour succès de la suppression
            "message": "Utilisateur supprimé avec succès"
        }
        return jsonify(response_data), 200

    except mariadb.Error as e:
        # En cas d'erreur, retourner une réponse d'erreur
        error_data = {
            "status_code": 500,
            "error": str(e)
        }
        return jsonify(error_data)

    except Exception as e:
        return json.dumps({'error': str(e)})


####################### ENREGISTREMENTS & ORGANISATIONS ###################

@app.route(EndPoints.OPTIONS_ENREG, methods=['GET'])
@jwt_required()
def get_options_enregistrement():
    # return jsonify(dict(request.headers))
    try:
        conn = mariadb.connect(**config_local)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM typeclients ;")
        rows_data_type = cursor.fetchall()
        
        cursor.execute("SELECT * FROM secteurs ;")
        rows_data_secteurs = cursor.fetchall()

        cursor.execute("SELECT * FROM pays ;")
        rows_data_pays = cursor.fetchall()

        cursor.close()
        conn.close()

        data_type = [{
            "id": row[0],
            "label": row[1],
            "description": row[2],
            "sensible": row[3],
            "ordre": row[4],
        } for row in rows_data_type]

        data_pays = [{
            "id": row[0],
            "label": row[1],
        } for row in rows_data_pays]

        data_secteurs = [{
            "id": row[0],
            "label": row[1],
            "sensible": row[2],
            "ordre": row[3],
        } for row in rows_data_secteurs]

        response_data = {
            "typesClient": data_type,
            "pays": data_pays,
            "secteursActivite": data_secteurs
        }

        return format_response(200, "Options chargées", response_data)
    
    except mariadb.Error as err :
        return format_response(500, str(e), "Erreur mariadb")
    
    except Exception as e :
        return format_response(500, str(e), "Erreur serveur")


# Route : créer une nouvelle organisation   
@app.route(EndPoints.ORGANISATIONS, methods=['POST'])
# @app.route('/edcp/api/v0/organisations/', methods=['POST'])
@jwt_required()
def create_organisation():
    try:
        data = request.json
        # return data, 200
        with mariadb.connect(**config_local) as conn :
            with conn.cursor() as cursor :
                query = f"INSERT INTO registrations (user_id, typeclient_id, raisonsociale, representant, rccm, secteur_id, secteur_description, presentation, telephone, email_contact, site_web, pays_id, ville, adresse_geo, adresse_bp, gmaps_link, effectif) VALUES ({data['user_id']}, {data['typeclient_id']}, '{data['raisonsociale']}', '{data['representant']}', '{data['rccm']}', {data['secteur_id']}, '{data['secteur_description']}', '{data['presentation']}', '{data['telephone']}', '{data['email_contact']}', '{data['site_web']}', {data['pays_id']}, '{data['ville']}', '{data['adresse_geo']}', '{data['adresse_bp']}', '{data['gmaps_link']}', {data['effectif']});"
                #return query, 200
                cursor.execute(query)
                conn.commit()
        return format_response(201, "Enregistrement effectué", None)
            
    except mariadb.Error as err :
        return format_response(500, str(err), "Erreur mariadb")
    
    except Exception as e :
        return format_response(500, str(e), "Erreur serveur")


# Route liste des organisations
@app.route('/edcp/api/v0/entreprises', methods=['GET'])
@jwt_required()
def get_all_entreprises():
    """
    lister les Entreprises disponible
    :return:
    """
    try:
        # connexion a la base de données
        conn = mariadb.connect(**config_local)
        cursor = conn.cursor()

        # execution de la requête SQL
        cursor.execute("SELECT * FROM listeentreprises ;")
        rows_data = cursor.fetchall()

        # Fermeture des ressources de la base de données
        cursor.close()
        conn.close()

        # Création de la réponse JSON
        response_data = {
            "status_code": 200,
            "data": [{
                "id": row[0],
                "typeClient": row[1],
                "nomRaisonSociale": row[2],
                "presentation": row[3],
                "numRccm": row[4],
                "domaine": row[5],
                "telephone": row[6],
                "contactEmail": row[7],
                "pays": row[8],
                "ville": row[9],
                "localisation": row[10],
                "gmapsLink": row[11],
                "cateDonnees": row[12],
                "effectif": row[13]
            }
                for row in rows_data]
        }
        return jsonify(response_data)

    except mariadb.Error as e:
        # En cas d'erreur, retourner une réponse d'erreur
        error_data = {
            "status_code": 500,
            "error": str(e)
        }
        return jsonify(error_data)

    except Exception as e:
        return json.dumps({'error': str(e)})



# Route liste des rôles
@app.route('/edcp/api/v0/roles', methods=['GET'])
@jwt_required()
def get_all_roles():
    """
    lister les rôles disponible
    :return:
    """
    try:
        # connexion a la base de données
        conn =  mariadb.connect(**config_local)
        cursor = conn.cursor()

        # execution de la requête SQL
        cursor.execute("SELECT * FROM roles ;")
        rows_data = cursor.fetchall()

        # Fermeture des ressources de la base de données
        cursor.close()
        conn.close()

        # Création de la réponse JSON
        response_data = {
            "status_code": 200,
            "data": [{
                "id": row[0],
                "role": row[1]
        }
        for row in rows_data]
        }
        return jsonify(response_data)

    except mariadb.Error as e:
        # En cas d'erreur, retourner une réponse d'erreur
        error_data = {
            "status_code": 500,
            "error": str(e)
        }
        return jsonify(error_data)

    except Exception as e:
        return json.dumps({'error': str(e)})



@app.route('/edcp/api/v0/personnes-concernees', methods=['GET'])
@jwt_required()
def get_all_personnes_concernees():
    """
    lister les personnes concernees
    :return:
    """
    try:
        # connexion a la base de données
        conn = mariadb.connect(**config_local)
        cursor = conn.cursor()

        # execution de la requête SQL
        cursor.execute("SELECT * FROM persconcernees ;")
        rows_data = cursor.fetchall()

        # Fermeture des ressources de la base de données
        cursor.close()
        conn.close()

        # Création de la réponse JSON
        response_data = {
            "status_code": 200,
            "data": [{
                "id": row[0],
                "label": row[1],
                "sensible": row[2],
                "ordre": row[3]
            }
                for row in rows_data]
        }
        return jsonify(response_data)

    except mariadb.Error as e:
        # En cas d'erreur, retourner une réponse d'erreur
        error_data = {
            "status_code": 500,
            "error": str(e)
        }
        return jsonify(error_data)

    except Exception as e:
        return json.dumps({'error': str(e)})


@app.route('/edcp/api/v0/fondements', methods=['GET'])
@jwt_required()
def get_all_fondements():
    """
    lister les fondements
    :return:
    """
    try:
        # connexion a la base de données
        conn = mariadb.connect(**config_local)
        cursor = conn.cursor()

        # execution de la requête SQL
        cursor.execute("SELECT * FROM fondjuridiques ;")
        rows_data = cursor.fetchall()

        # Fermeture des ressources de la base de données
        cursor.close()
        conn.close()

        # Création de la réponse JSON
        response_data = {
            "status_code": 200,
            "data": [{
                "id": row[0],
                "label": row[1],
                "description": row[2],
            }
                for row in rows_data]
        }
        return jsonify(response_data)

    except mariadb.Error as e:
        # En cas d'erreur, retourner une réponse d'erreur
        error_data = {
            "status_code": 500,
            "error": str(e)
        }
        return jsonify(error_data)

    except Exception as e:
        return json.dumps({'error': str(e)})


@app.route('/edcp/api/v0/finalites', methods=['GET'])
@jwt_required()
def get_all_finalite():
    try:
        # connexion à la base de données
        conn = mariadb.connect(**config_local)
        cursor = conn.cursor()

        # execution de la requête SQL pour récupérer les finalités et sous-finalités
        cursor.execute("SELECT * FROM finalites;")
        finalites_data = cursor.fetchall()

        cursor.execute("SELECT * FROM listesousfinalites;")
        sous_finalites_data = cursor.fetchall()

        # Fermeture des ressources de la base de données
        cursor.close()
        conn.close()

        # Organiser les données en un dictionnaire pour faciliter la création de la réponse JSON
        finalites_dict = {}
        for row in finalites_data:
            finalite_id = row[0]
            finalites_dict[finalite_id] = {
                "id": str(finalite_id),
                "label": row[1],
                "sensible": bool(row[2]),
                "ordre": int(row[3]),
                "sousFinalites": []
            }

        for row in sous_finalites_data:
            sous_finalite_id = row[0]
            finalite_id = row[5]

            sous_finalite_info = {
                "id": str(sous_finalite_id),
                "label": row[1],
                "sensible": bool(row[2]),
                "ordre": int(row[3])
            }
            finalites_dict[finalite_id]["sousFinalites"].append(sous_finalite_info)
        # Convertir le dictionnaire en une liste pour la réponse JSON
        finalites_list = list(finalites_dict.values())

        # Création de la réponse JSON
        response_data = {
            "status_code": 200,
            "data": finalites_list
        }

        return jsonify(response_data)

    except mariadb.Error as e:
        # En cas d'erreur, retourner une réponse d'erreur
        error_data = {
            "status_code": 500,
            "error": str(e)
        }
        return jsonify(error_data)

    except Exception as e:
        return json.dumps({'error': str(e)})


# app.run()
port = int(os.environ.get('PORT', 5500))
if __name__ == '__main__':
   app.run(debug=True, threaded=True, host='127.0.0.1', port=port)
