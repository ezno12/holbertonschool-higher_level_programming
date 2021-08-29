#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""


def main():
    """ main """
    import requests
    from sys import argv

    search_url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    info = (username, password)
    result = requests.get(search_url, auth=info)
    try:
        print(result.json()['id'])
    except Exception:
        print("None")

if __name__ == '__main__':
    main()
