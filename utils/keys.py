"""
SSH Key related utils
"""

import requests
from utils.requests import headers

def get_key_fingerprints(token):
    """
    Using ssh_key fingerprints because array of ids seems broken on Digital
    Ocean's side.
    """

    request = requests.get('https://api.digitalocean.com/v2/account/keys', headers=headers(token))

    return list(map(lambda key: key['fingerprint'], request.json()['ssh_keys']))

def get_key_ids(token):
    """get a key to embed when making a new droplet."""

    request = requests.get('https://api.digitalocean.com/v2/account/keys', headers=headers(token))

    return list(map(lambda key: key['id'], request.json()['ssh_keys']))
