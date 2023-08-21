import pandas as pd
import os

cd = 11
def bcb(codigo):
  link = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json"
  df = pd.read_json(link)
  df.index = pd.to_datetime(df["data"], dayfirst=True)
  df = df["valor"]
  return df

selic = bcb(11)
file_path = os.path.join("C:\\Users\\Cliente\\Desktop", "selic.xlsx")
selic.to_excel(file_path)