from enum import Enum



# Préfixe de l'URL de l'API
api_prefix = "/edcp/api/v0/"
#ENDPOINTS = EndPoints()

# Endpoints de l'API
class EndPoints():
  USERS = api_prefix + "users"
  ORGANISATION = api_prefix + "organisations"
  OPTIONS_ENREG = api_prefix + "options-enregistrement"