import pandas as pd
from ..models import Company

def csv2db():
    df = pd.read_csv('data-set/6000_Largest_Companies_ranked_by_Market_Cap.csv') 
    
    records = df.to_records()  

    for record in records:
        company = Company(
            name=record[2],
            symbol=record[3],
            market_cap=record[4],
            price=record[5],
            country=record[6],
        )
        # print(company.country)
        # break
        company.save()