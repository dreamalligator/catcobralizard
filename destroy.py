"""take down a catcobralizard instance"""

import requests
from utils.droplets import get_droplet_id
from utils.requests import headers
from utils.cache import retrieve_token

def destroy_droplet(token):
    """destroy a droplet"""

    droplet_id = get_droplet_id()
    params = {
        'id': droplet_id
    }

    print(f'destroying droplet {droplet_id}...')
    url = 'https://api.digitalocean.com/v2/droplets'
    request = requests.delete(url, headers=headers(token), params=params)

    # see https://github.com/requests/requests/blob/master/requests/status_codes.py
    # pylint: disable=E1101
    if request.status_code != requests.codes.no_content:
        print('Something went wrong. ' + request.json()['message'])
        return

    print(f'destroyed droplet {droplet_id}.')

if __name__ == '__main__':
    destroy_droplet(retrieve_token())
