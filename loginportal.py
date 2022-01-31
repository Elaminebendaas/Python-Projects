import os



username = open('users.txt', 'w')
password = open('passwords.txt', 'w')


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def login(users, passwords):
    usernamecount = 0
    passwordcount = 0
    print("Welcome, below you will be prompted to enter you username and password.")
    while True:
        try:
            userseletion = input('Type "Yes" if you would like to create a new account or any number to proceed to the log in!: ').lower()
            if userseletion == 'yes':
                break
        except:
            if userseletion != 'yes':
                break
            

    if userseletion == 'yes':
        clearConsole()
        return True

    username = input("Username: ")
    password = input("Password: ")
    username.strip()
    password.strip()
    
    for line in users:
        if username == line:
            usernamecount =+ 1
            break
        else:
            print('Incorrect username!')
    for line in passwords:
        if password == line:
            passwordcount =+ 1 
            break
        else:
            print('Incorrect password')
    
    result = passwordcount + usernamecount
    return result
    

def accountCreation(users, passwords):
    print('You are here because you would like to create an account!')
    print('Please select a username and password')
    username = input('Username: ')
    password = input('Password: ')
    users.write(username)
    passwords.write(password)
    clearConsole()


if login(username, password) == True:
    accountCreation(username, password)

while True:
    if login != 2:
        login(username, password)
    else:
        break

print("good job lamino, you can finally start creating your cryptohub!")

