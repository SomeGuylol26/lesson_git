def ask_password():
    attempts = 0
    pass_word = input('Enter the password: ')
    while pass_word != 'password':
        attempts += 1
        pass_word = input('Wrong! Try again: ')
        if attempts == 3:
            return 'Access denied'
    return 'The password is accepted'
print(ask_password())