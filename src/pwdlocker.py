import pyperclip

PASSWORDS = {
    'gmail':'jeong112@',
    'naver':'jeong11211@',
    '11st':'jeong112@'
}

def main():
    site = input('input your site:')
    pwd = PASSWORDS[site]

    if not pwd:
        print('not valid site')
    else:
        pyperclip.copy(pwd)
        print('your pwd is copied')


main()
