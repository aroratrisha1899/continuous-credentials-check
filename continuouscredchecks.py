#Check Credentials Continuous

while True:   
    Var_username_checks=str(input('Please enter the correct username: '))
    Var_Pass_checks= str(input('Please enter the correct password: '))

    Var_username=str(input('Please enter your username: '))
    Var_Pass=str(input('Please enter your password: '))
    if (Var_Pass_checks==Var_Pass and Var_username_checks==Var_username):
        print('Password Matched')

    else:
        print('Authentication failed. Please retry')
