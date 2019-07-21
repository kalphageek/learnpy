import pyperclip

PASSWORDS = {
    'gmail': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'naver': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'facebook': '12345'
}


def main():
    site = input('input your site:')

    password = PASSWORDS[site]

    if not password:
        print('not valid site')
    else:
        pyperclip.copy(password)
        print('your password is copied')


main()

