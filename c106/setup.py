import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Temperature"]))
            cold_drink_sales.append(float(row["Ice-cream Sales"]))

    return{"x":ice_cream_sales,"y":cold_drink_sales}        
def FindCoRelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("corelation between temperature and icecream",corelation[0,1])

def setup():
    data_path = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    dataSource = getDataSource(data_path)
    FindCoRelation(dataSource)

setup()   