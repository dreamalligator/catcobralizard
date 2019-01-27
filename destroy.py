"""take down a catcobralizard instance"""

import requests
from refresh_info import get_droplet_id, retrieve_token

def destroy_droplet(token):
    """destroy a droplet"""

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    params = {
        'id': get_droplet_id()
    }

    print(f'destroying droplet ...')
    requests.delete('https://api.digitalocean.com/v2/droplets', headers=headers, params=params)

if __name__ == '__main__':
    destroy_droplet(retrieve_token())
