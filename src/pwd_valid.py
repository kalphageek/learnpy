def valid_pwd(user_pwd=''):
    if len(user_pwd) < 8:
        return False
    elif user_pwd.isalpha():
        return False
    elif user_pwd.isnumeric():
        return False
    else:
        return True

def main():
    user_pwd = input('input your password: ')
    if valid_pwd(user_pwd):
        print('valid password')
    else:
        print('invalid password')


main()