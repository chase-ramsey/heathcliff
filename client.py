import requests
import sys


# We are going to connect to the server
# Then we take a message we've written and post it.

def main(ip, custom_port=None):
    
    # check that we have an ip address
    if len(ip) == 0:
        sys.exit("You need to give an ip address or a domain name to connect to")

    # deal with ports that aren't default 80
    if custom_port:
        port = str(custom_port)
    else:
        port = '80'

    # create our full connection address
    address = 'http://{}:{}'.format(ip, port)
    print(address)

    # main loop
    on = True
    while on:
        
        message = input('> ').encode('utf-8')
        if message.decode('utf-8') == 'quit':
            sys.exit()
        r = requests.post(address, data=message)
        print(r.status_code)

if __name__ == '__main__':

    try:
        ip = sys.argv[1]
        port = sys.argv[2]
        main(ip, port)
    except IndexError:
        main(ip)

