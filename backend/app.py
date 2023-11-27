# import the necessary packages
import os
import json
import mariadb
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, request

from backend.configs import config_local, app


@app.route('/')
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


# Route d'authentification
@app.route('/edcp/api/v0/login', methods=['POST'])
def login():
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
        return jsonify(access_token=access_token), 200
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
                    "INSERT INTO users (login, passwd, role_id, avatar, created, nom, prenoms, Organisation, email, telephone, fonction, consentement) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                    (user_data['login'], generate_password_hash(user_data['passwd'], method='sha256'), user_data['role_id'], user_data['avatar'], user_data['created'], user_data['nom'], user_data['prenoms'],
                     user_data['Organisation'], user_data['email'], user_data['telephone'], user_data['fonction'], user_data['consentement'])
                )
                # Confirmer les modifications dans la base de données
                conn.commit()

        # Création de la réponse JSON
        response_data = {
            "status_code": 201,  # Code 201 pour création réussie
            "message": "Utilisateur créé avec succès"
        }
        return jsonify(response_data), 201
    except mariadb.Error as e:
        # En cas d'erreur, retourner une réponse d'erreur
        error_data = {
            "status_code": 500,
            "error": str(e)
        }
        return jsonify(error_data)
    except Exception as e:
        return json.dumps({'error': str(e)})


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
        cursor.execute("SELECT * FROM users ;")
        rows_data = cursor.fetchall()

        # Fermeture des ressources de la base de données
        cursor.close()
        conn.close()

        # Création de la réponse JSON
        response_data = {
            "status_code": 200,
            "datas": [{
                "id": row[0],
                "login": row[1],
                "role_id": row[3],
                "name": row[6],
                "prenom": row[7],
                "organisation": row[8],
                "telephone": row[10],
                "fonction": row[11],
                "dateCreation": row[5],
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
            "datas": [{
                "id": row[0],
                "login": row[2],
                "role_id": row[3],
                "name": row[6],
                "prenom": row[7],
                "organisation": row[8],
                "telephone": row[10],
                "fonction": row[11],
                "dateCreation": row[5],
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


# Exemple de route protégée avec JWT
@app.route('/edcp/api/v0/protected', methods=['GET'])
@jwt_required()
def protected():
    # Récupérer l'identité de l'utilisateur à partir du jeton
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


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
            "datas": [{
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
            "datas": [{
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


@app.route('/edcp/api/v0/sousfinalite', methods=['GET'])
@jwt_required()
def get_all_sousfinalite():
    """
    lister les sousfinalite disponible
    :return:
    """
    try:
        # connexion a la base de données
        conn = mariadb.connect(**config_local)
        cursor = conn.cursor()

        # execution de la requête SQL
        cursor.execute("SELECT * FROM listesousfinalites ;")
        rows_data = cursor.fetchall()

        # Fermeture des ressources de la base de données
        cursor.close()
        conn.close()

        # Création de la réponse JSON
        response_data = {
            "status_code": 200,
            "datas": [{
                "id": row[0],
                "label": row[1],
                "sensible": row[2],
                "ordre": row[3],
                "finalite": row[4],
                "id_finalite": row[5]

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


# app.run()
port = int(os.environ.get('PORT', 5500))
if __name__ == '__main__':
   app.run(debug=True, threaded=True, host='127.0.0.1', port=port)
