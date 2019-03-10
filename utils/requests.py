"""
Request related utils.
"""

def headers(token):
    """so far all headers are same. DRYs that up slightly."""

    headers_obj = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    return headers_obj
