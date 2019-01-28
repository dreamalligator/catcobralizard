"""setup Ghost"""

from refresh_info import get_droplet_ip

def setup_ghost():
    """set up admin ghost stuff"""

    droplet_ip = get_droplet_ip()
    print('!', droplet_ip)

if __name__ == '__main__':
    setup_ghost()
