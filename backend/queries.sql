INSERT INTO registrations (user_id, typeclient_id, raisonsociale, representant, rccm, secteur_id, secteur_description, presentation, telephone, email_contact, site_web, pays_id, ville, adresse_geo, adresse_bp, gmaps_link, effectif) VALUES (56, 1, "G corp", "GG", "12345 GG", 2, "", "blabla", "01 02 03 04 05", "mail@mail.corp", "www.gg.corp", 3, "Abidjan", "localisation", "BP 000", "https://gmaps", 30);

SELECT r.id, u.id, CONCAT(u.nom, ' ', u.prenoms), r.created_at, r.raisonsociale, r.rccm, r.presentation, r.telephone, r.email_contact, r.site_web, r.ville, r.adresse_geo, r.effectif 
FROM registrations as r 
INNER JOIN users as u 
ON r.id = u.id;