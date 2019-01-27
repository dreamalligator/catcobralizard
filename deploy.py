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

    requests.post('https://api.digitalocean.com/v2/droplets', headers=headers, params=droplet_info)

if __name__ == '__main__':
    deploy_droplet(retrieve_token())
