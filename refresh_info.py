"""
Refresh droplet info.

requires a saved token, or retreiving it from https://cloud.digitalocean.com/account/api/tokens.
"""

import os.path
import json
import requests

def retrieve_token():
    """check if have a saved Digital Ocean API token, or retreive one."""

    token_file_name = 'DIGITALOCEAN_TOKEN'

    if os.path.isfile(token_file_name):
        print('token found...')

        with open(token_file_name, 'r') as token_f:
            digitalocean_token = token_f.read().replace('\n', '')
    else:
        digitalocean_token = input(
            '''Digital Ocean API token not found, retrieve your token from digitalocean.
visit https://cloud.digitalocean.com/account/api/tokens.
enter token: '''
        )

        with open(token_file_name, 'w') as token_f:
            token_f.write(digitalocean_token)

        print('token saved to DIGITALOCEAN_TOKEN.')

    return digitalocean_token

def refresh_droplet_cache(token):
    """check if have saved catcobralizard droplet info, or retrieve it."""

    cached_droplet_info_file = 'droplet_info.json'

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    print('attempting to retrieve catcobralizard info...')

    request = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)

    refreshed = False
    for droplet in request.json()['droplets']:
        if droplet['name'] == 'catcobralizard':
            with open(cached_droplet_info_file, 'w') as info_f:
                info_f.write(json.dumps(droplet))
            droplet_id = droplet['id']
            print(f'saving info for droplet {droplet_id}...')
            refreshed = True
            break

    if not refreshed:
        print('no catcobralizard droplets found.')

def get_droplet_id():
    """get droplet id from cached info, prevents unnecessary requests."""

    cached_droplet_info_file = 'droplet_info.json'

    with open(cached_droplet_info_file, 'r') as info_f:
        droplet_info = json.load(info_f)
        return droplet_info['id']

if __name__ == '__main__':
    refresh_droplet_cache(retrieve_token())
