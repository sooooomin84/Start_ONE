import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm

#1144000000 마포구

def get_estate(page):
    url = 'https://new.land.naver.com/api/articles'

    params = {'page': page,
              "cortarNo": 1144000000 }  # 마포구
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NTY2NTA3OTgsImV4cCI6MTY1NjY2MTU5OH0.zp9pWC_Glyk_T6MElmZytijcvFLbI9qbL7N0PPq4_ao",
        "Connection": "keep-alive",
        "Host": "new.land.naver.com",
        "Referer": "https://new.land.naver.com/offices?ms=37.5751146,126.8983807,15",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, params=params, headers=headers)
    art_list = resp.json()['articleList']
    return art_list