import re
import pyperclip

email_regex = re.compile(r'''(
    ([\w\-+.]+)                  #group #1 - username
    @                           #@ symbol
    ([\w\-.]+(\.\w{2,4}){1,2})    #domain name
    )''', re.VERBOSE)

def find_match_list():
    # 클립보드에 복사된 내용에서 이메일 패턴과 매치되는 텍스트를 찾는다
    text = pyperclip.paste()
    matches = []
    for email in email_regex.findall(text):
        matches.append(email[0])

    return matches

def copy_result_to_clipboard(matches):
    # 결과를 클립보드에 복사하기
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('클립보드에 복사되었습니다.')
    else:
        print('매칭되는 패턴이 없습니다.')

def main():
    matchs = find_match_list()
    copy_result_to_clipboard(matches)