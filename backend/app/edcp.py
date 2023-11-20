#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-

"""
   API REST EDCP
    base_url = edcp/api/v0.1/
        . Instance de flask
        . flask-cors : Une extension Flask pour gérer le partage de ressources d'origine croisée (CORS), rendant possible AJAX d'origine croisée.
"""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app=app)
