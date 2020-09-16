#!/usr/bin/env python3


# Importation des modules
import os
import sys
import signal


# Permet les terminaisons silencieuses (évite les traces laides)
signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # Évite les traces d'ereur:casse

# Capture le retour de la frappe Ctrl-C
signal.signal(signal.SIGINT, signal.SIG_DFL)




# Arguments dans le srcript: inférieur à trois"
if len(sys.argv) < 3:

	BLACK='\030[30m'
	END='\033[0m'



def banner():
    cisco_automation = """\030
    _         _                        _   _           _
   / \  _   _| |_ ___  _ __ ___   __ _| |_(_)___  __ _| |_(_) ___  _ __
  / _ \| | | | __/ _ \| '_ ` _ \ / _` | __| / __|/ _` | __| |/ _ \| '_ \
 / ___ \ |_| | || (_) | | | | | | (_| | |_| \__ \ (_| | |_| | (_) | | | |
/_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|___/\__,_|\__|_|\___/|_| |_|

     _             _             _                  ____ ___ ____   ____ ___
  __| | ___  ___  | |_ __ _  ___| |__   ___  ___   / ___|_ _/ ___| / ___/ _ \
 / _` |/ _ \/ __| | __/ _` |/ __| '_ \ / _ \/ __| | |    | |\___ \| |  | | | |
| (_| |  __/\__ \ | || (_| | (__| | | |  __/\__ \ | |___ | | ___) | |__| |_| |
 \__,_|\___||___/  \__\__,_|\___|_| |_|\___||___/  \____|___|____/ \____\___/
 \033"""
    return cisco_automation



# Affichage du menu
def menu():
    print (banner() + """\030
 [*] Gérer vos switchs & routeurs en tapant votre choix 1 ou 2, puis Entrée [*]

	[1]--Vérification et sauvegarde des configurations sur Routeurs
	[2]--Vérification et sauvegarde des configurations sur Switchs
\033[0m""")
	#(exit)
menu()
choix = input()

# Choix
if choix == "1":
	os.system('./switch_routeur.py routeur_commands.txt routeurs.json')
elif choix == "2":
	os.system('./switch_routeur.py switch_commands.txt switchs.json')



exit()
