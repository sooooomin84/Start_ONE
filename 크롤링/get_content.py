import requests
import pandas as pd
import numpy as np
import time
from multiprocessing import Pool

df=pd.read_csv('연남동 부동산.csv')
urls = []
for i in range(len(df)):
    row = df.loc[i]
    y_axis = row['latitude']
    x_axis = row['longitude']
    url = f'https://www.nicebizmap.co.kr/util/readData.jsp?LF=nice.Analyse&LID=getMapControl&sql_type=flowpop&x_axis={x_axis}&y_axis={y_axis}&radius=250&readType=json'
    urls.append(url)
def get_content(url: str):
        response=requests.get(url)
        data=response.json()['flowpop']
        return data
df=pd.read_csv('연남동 부동산.csv')
urls = []
for i in range(len(df)):
    row = df.loc[i]
    y_axis = row['latitude']
    x_axis = row['longitude']
    url = f'https://www.nicebizmap.co.kr/util/readData.jsp?LF=nice.Analyse&LID=getMapControl&sql_type=flowpop&x_axis={x_axis}&y_axis={y_axis}&radius=250&readType=json'
    urls.append(url)
