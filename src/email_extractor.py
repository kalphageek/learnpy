import re
import pyperclip


#1.text를 ctrl+c로 복사
#2.email_extract.py 실행
#3.text파일에 ctrl+v

#email_regex = re.compile(r'''(
#    ([\w\-+.]+)                  #group #1 - username
#    @                           #@ symbol
#    ([\w\-.]+(\.\w{2,4}){1,2})    #domain name
#    )''', re.VERBOSE)

# Create email regex.
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot-something
    )''', re.VERBOSE)


def find_match_list():
    # 클립보드에 복사된 내용에서 이메일 패턴과 매치되는 텍스트를 찾는다.
    text = pyperclip.paste()

    matches = []

    for email in email_regex.findall(text):
        matches.append(email[0])

    return matches


def copy_result_to_clipboard(matches):
    # Copy results to the clipboard.
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('클립보드에 복사되었습니다.')
    else:
        print('메칭되는 패턴이 없습니다.')


def main():
    matches = find_match_list()
    copy_result_to_clipboard(matches)

main()






