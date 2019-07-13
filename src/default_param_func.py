def connect_URI(server='localhost', port='80'):
    str = 'http://' + server + ':' + port
    return str

#server는 default값 사용
def main():
    sUri = connect_URI(port='8080')
    sUri = connect_URI()
    print(sUri)

main()