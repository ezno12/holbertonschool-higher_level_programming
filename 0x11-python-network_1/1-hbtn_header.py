#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""


def main():
    """ main """
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])

if __name__ == '__main__':
    main()
