from getpass import getpass

# Connection sur le prompt des appareils
def get_input(prompt=''):
    try:
        line = raw_input(prompt)

    except NameError:

        line = input(prompt)
    return line

def get_credentials():
#Invite, et retourne, un nom d'utilisateur et un mot de passe.
    username = get_input('Entrer nom d\'utilisateur: ')
    password = None
    while not password:
        password = getpass()
        password_verify = getpass('Retaper le mot de passe: ')
        if password != password_verify:
            print('Le mot de passe ne correspond pas. Réessayer')
            password = None
    return username, password
