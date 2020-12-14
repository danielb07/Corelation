import plotly.express as px
import csv

with open("cups of coffee vs hours of sleep.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
    fig.show()
# df = pd.read_csv("Teacher refrence\data.csv")
# fig = px.scatter(df, x="Population", y="Per capita",
# 	          size="Percentage",color="Country",
#                    size_max=60)
# fig.show()
