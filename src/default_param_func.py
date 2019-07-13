def connect_URI(server='localhost', port='80'):
    str = 'http://' + server + ':' + port
    return str

def main():
    sUri = connect_URI(port='8080')
    sUri = connect_URI()
    print(sUri)

main()