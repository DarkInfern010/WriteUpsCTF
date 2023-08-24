# Enoncé
Vous venez d'être nommé responsable d'un site sensible. Malheureusement pour vous, votre site est victime d'une cyber-attaque quelques jours après. C'est le pire moment pour une prise de poste me direz-vous. Vous avez raison, mais il se pourrait bien que la cyber-attaque ne soit qu'une diversion pour vous faire passer un message. Heureusement, quelqu'un de votre équipe a réussi à récupérer les logs du serveur. Saurez-vous retrouver et déchiffrer le message que l'attaquant vous a adressé ?

Logs: https://jeuxpythiques.woody.sh/fichiers/apache_log.log

Auteurs: Triblack_k / luarsh

# Solution
*Alors pour celui-là je suis presque sûr que je n'ai pas compris la dernière partie du chall et j'ai fait n'importe quoi, mais bon*
Le but est de récupérer dans un fichier de log apache des requêtes intéressantes.
Dans un premier temps, on s'aperçoit que la liste utilisée provient certainement de RockYou en vue des premières requêtes.
On va donc isoler les requêtes qui nous intéressent.
On retrouve des bout de base64 qu'on va essayer d'assembler pour en récupérer le flag

# Flag
JP2023{pythique_log_analysis_2023}