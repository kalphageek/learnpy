import json
import os

def main() -> object:
    with open(os.path.join('json', 'personal_info.json'), 'r') as f:
        info = json.load(f)

    for v in info:
        print(v)


if __name__ == '__main__':
    main()
