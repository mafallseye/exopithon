import sys
import pyperclip

passwords = {
    'google': 'googlepass',
    'paypal': 'paypalpass',
    'facebook': 'facebookpass'
}


if len(sys.argv) < 2:
    print("HELP : python pass_manager[account]")
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('password pour '+account+'à ete copié avec succès')
else:
    print("il y'a pas de compte de ce nom")
