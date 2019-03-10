"""
Droplet related utils
"""

import json

def get_droplet_id():
    """get droplet id from cached info, prevents unnecessary requests."""

    cached_droplet_info_file = 'droplet_info.json'

    with open(cached_droplet_info_file, 'r') as info_f:
        droplet_info = json.load(info_f)
        return droplet_info['id']

def get_droplet_ip():
    """get droplet ip from cache."""

    cached_droplet_info_file = 'droplet_info.json'

    with open(cached_droplet_info_file, 'r') as info_f:
        droplet_info = json.load(info_f)
        return droplet_info['networks']['v4'][0]['ip_address']
