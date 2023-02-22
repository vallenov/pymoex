import logging
import requests

from requests.models import Response

logger = logging.getLogger('moex.helpers')


def regular_request(
        url: str,
        method: str = 'GET',
        data: dict = None,
        cookies: dict = None,
) -> Response:
    """
    Regular request to site
    """
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Connection': 'close',
    }
    try:
        logger.info(f'Try to get info from {url}')
        if method.upper() == 'GET':
            resp = requests.get(url, headers=headers, cookies=cookies)
        elif method.upper() == 'POST':
            resp = requests.post(url, headers=headers, data=data, cookies=cookies)
        else:
            raise TypeError
        return resp
    except Exception as ex:
        logger.exception(f'{ex}')
        raise