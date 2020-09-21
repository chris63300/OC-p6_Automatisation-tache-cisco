#!/usr/bin/env python3


# Importation des modules et dictionnaires
import json
import outils
import netmiko
import os
import sys
import signal
import time

# Permet les terminaisons silencieuses (évite les traces laides)
signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # Évite les traces d'ereur:casse

# Capture le retour de la frappe Ctrl-C
signal.signal(signal.SIGINT, signal.SIG_DFL)


# Arguments dans le srcript: inférieur à trois"
if len(sys.argv) < 3:
    exit()

# Session SSH chronométrée en essayant de se connecter à l'appareil.
# Exception d'authentification SSH basée sur Paramiko AuthenticationException.
netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)

# Identfication de connexion (fichier 'outils.py')
username, password = outils.get_credentials()


# Lecture des arguments
# Identification du premier argument (fichier command)
with open(sys.argv[1]) as cmd_file:
    commands = cmd_file.readlines() #Chaque ligne devient un élément disctinct

# Identification du deuxième argument (fichier .json)
with open(sys.argv[2]) as dev_file:
    devices = json.load(dev_file) #Chargement des identifiants indiqués dans .json

# Itération des commandes
for device in devices:
    device['username'] = username
    device['password'] = password
    try:
# Séparation des sorties par des -------
        print('-'*80)
        print('Connexion en cours', device['ip'])
        connection = netmiko.ConnectHandler(**device)

        # Création d'un nouveau répertoire portant le nom d'invite de base \
        # (nom de machine)
        newdir = connection.base_prompt

# relance l'exception si une autre erreur s'est produite.
# Cette relance va permettre de pouvoir avoir en sortie \
# la configuration de toutes les machines identifiées \
# dans le fichier .json
        try:
           os.mkdir(newdir)
        except OSError as error:
             # Le fichier existe erreur
            if error.errno == 17:
               print('Repertoire', newdir, 'existe déjà')
            else:

                raise

# Création d'un fichier pour chaque commande (boucle for)
        for command in commands:

# Nom de fichier(les espaces seront remplacés par des traits de soulignements). \
# les noms de fichiers se termineront par .txt
            filename = command.replace(' ','_') + '.txt'

# Stockage des fichiers dans le nouveau répertoire créé
            filename = '/'.join((newdir, filename))
            with open(filename, 'w') as out_file:
                out_file.write(connection.send_command(command) + '\n')
# Édition (e) du retour de netmiko_exeptions
        connection.disconnect()
    except netmiko_exceptions as w:
        print('Echec de la machine', device['ip'], w )
