"""deploy a fresh catcobralizard instance"""

import requests
from utils.keys import get_key_fingerprints
from utils.requests import headers
from utils.cache import retrieve_token

def deploy_droplet(token):
    """deploy a new droplet"""

    droplet_info = {
        'name': 'catcobralizard',
        'region': 'sfo2',
        'size': '4gb',
        'image': 'ghost-18-04',
        'ssh_keys': get_key_fingerprints
    }

    print('deploying new droplet...')
    url = 'https://api.digitalocean.com/v2/droplets'
    request = requests.post(url, headers=headers(token), params=droplet_info)

    # see https://github.com/requests/requests/blob/master/requests/status_codes.py
    # pylint: disable=E1101
    if request.status_code != requests.codes.accepted:
        print('Something went wrong. ' + request.json()['message'])
        return

    print('Deployed catcobralizard! 🐱🐍🦎')

if __name__ == '__main__':
    deploy_droplet(retrieve_token())
