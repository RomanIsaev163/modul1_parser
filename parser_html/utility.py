import requests as rq
from fake_useragent import UserAgent


def get_html(url: str) -> bytes:
    return rq.get(url, headers={'User-Agent': UserAgent().chrome}, timeout=15)