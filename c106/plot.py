import pandas as pd
import plotly.express as px
import csv

with open("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Temperature", y="Ice-cream Sales")
    fig.show()
# df = pd.read_csv("Teacher refrence\data.csv")
# fig = px.scatter(df, x="Population", y="Per capita",
# 	          size="Percentage",color="Country",
#                    size_max=60)
# fig.show()
