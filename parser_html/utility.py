import requests as rq
from fake_useragent import UserAgent


def get_html(url: str) -> rq.models.Response:
    try:
        response = rq.get(url, headers={'User-Agent': UserAgent().chrome}, timeout=15)
        return response
    except:
        return None