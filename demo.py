import pandas as pd


def preprocess(df):
    return df.drop([0, 6, 12, 18, 24, 30, 36])

df_list = [
    preprocess(pd.read_excel('https://www.city.utsunomiya.tochigi.jp/_res/common/opendata/1020122/jinkou0303.xls', skiprows=[0,1,2,4], usecols=range(0+i, 4+i))) for i in [0, 5, 10]
]
