#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-

"""
   API REST Komparat
    base_url = edcp/api/v0.1/
        . Gestion des erreurs
"""
from flask import jsonify, make_response, request

from .edcp import app


@app.errorhandler(404)
def not_found(error=None):
    """ Gestion de l'erreur des ressource pas trouvée """
    message = {
        'status': error.code,
        'description': U'{}' .format(str(error.description)),
        'name': U'{}' .format(str(error.name)),
        'url': request.url
    }
    return make_response(jsonify(message), 404)


@app.errorhandler(400)
def bad_request(error=None):
    """ Gestion de l'erreur des ressource pas trouvée """
    message = {
        'status': error.code,
        'description': U'{}'.format(str(error.description)),
        'name': U'{}'.format(str(error.name)),
        'url': request.url
    }
    return make_response(jsonify(message), 400)


@app.errorhandler(500)
def error_server(error=None):
    """ Gestion de l'erreur des ressource pas trouvée """
    message = {
        'status': error.code,
        'description': U'{}'.format(str(error.description)),
        'name': U'{}'.format(str(error.name)),
        'url': request.url
    }
    return make_response(jsonify(message), 500)


@app.errorhandler(424)
def not_found424(error=None):
    """
        Gestion de l'erreur des ressource pas trouvée
        The requested resource could not be processed.
    """
    message = {
        'status': error.code,
        'description': U'{}'.format(str(error.description)),
        'name': U'{}'.format(str(error.name)),
        'url': request.url
    }
    return make_response(jsonify(message), 424)

