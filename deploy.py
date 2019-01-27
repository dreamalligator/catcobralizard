"""deploy a fresh catcobralizard instance"""

import requests
from refresh_info import retrieve_token

def deploy_droplet(token):
    """deploy a new droplet"""

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    droplet_info = {
        'name': 'catcobralizard',
        'region': 'sfo2',
        'size': '4gb',
        'image': 'ghost-18-04'
    }

    print('deploying new droplet...')
    url = 'https://api.digitalocean.com/v2/droplets'
    request = requests.post(url, headers=headers, params=droplet_info)

    # see https://github.com/requests/requests/blob/master/requests/status_codes.py
    # pylint: disable=E1101
    if request.status_code != requests.codes.accepted:
        print('Something went wrong. ' + request.json()['message'])
        return

    print('Deployed catcobralizard! 🐱🐍🦎')

if __name__ == '__main__':
    deploy_droplet(retrieve_token())
