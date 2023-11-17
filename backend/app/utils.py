#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
"""
   API REST E-DCP
    base_url = edcp/api/v0.1/
        . Implementation de l'Api
"""

import pymysql
import json
import mariadb

from config_bd import RDS_HOST, USER_NAME, DB_NAME, mysql, logger, PASSWORD, RDS_PORT


def connect_bd():
    """
    Connexion a la base de donnée api_db_edcp
    :return:
    """
    # pametre de connexiona la bd
    config = {
        'host': RDS_HOST,
        'port': RDS_PORT,
        'user': USER_NAME,
        'password': PASSWORD,
        'database': DB_NAME
    }
    try:

        conn = mariadb.connect(**config)
        return "connexion OK !", conn
    except Exception:
        logger.exception(
            "problème de connexion a la base de donnée, veillez revoir votre vos paramètres, et s'assurer votre service"
            " MySQL est actif.",
        )
