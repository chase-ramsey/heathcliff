import requests
import sys


# We are going to connect to the server
# Then we take a message we've written and post it.

def main(ip):
    
    if len(ip) == 0:
        sys.exit("You need to give an ip address or a domain name to connect to")

    on = True
    while on:
        
        message = input('>').encode('utf-8')
        if message == 'quit':
            sys.exit()
        r = requests.post(ip, data=message)


if __name__ == '__main__':

    ip = sys.argv[x]
    main(ip)

