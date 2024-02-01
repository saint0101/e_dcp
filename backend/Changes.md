 # Changements apportés à l'API/BD


1. **Corrections des noms des colonnes de la table users et des champs des requêtes JSON**
> prenom --> prenoms \
> Organisation --> organisation

2. **Mise à jour des messages de réponse**
3. **Prise en charge du CORS (Cross-Origin Resource Sharing)**  
* installation (terminal) :
> pip install flask_cors  
* code (app.py) :  
```python
from flask_cors import CORS  
CORS(app, origins=["http://localhost:*"])
```
4. **Ajout d'une méthode de login par email (à améliorer)**
5. **Standardidation du format des réponses et ajout d'une méthode de formattage des réponses**  
```JSON
{
  "status_code": "", //200, 201, 400 etc.
  "message": "",
  "data": Object // corps de la réponse
}
```
6. **Modifications de noms de colonnes des tables typeclient, pays, ville etc.**
Utilisation de "label" au lieu de "pays", "ville" etc.
7. **Fixation de la clé de signature des access-token JWT**
Utilisation d'une clé fixe 'chelton' pour les tests afin d'éviter le changement des signatures des access-token à chaque rechargement du script du serveur.
!! A modifier
