def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        for karakter in newpassword:
            if karakter in '0123456789':
                return True
        return False
    else:
        return False

# Vraag om oud wachtwoord
oud = input('Geef je oude wachtwoord: ')
# Vraag om nieuw wachtwoord
nieuw = input('Geef je nieuwe wachtwoord: ')
print(new_password(oud, nieuw))
