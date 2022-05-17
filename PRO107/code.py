import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())
fig = go.Figure(go.Scatter(
            x=df.groupby("student_id", as_index=False)["attempt"].mean(),
            y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
            size="attempt",
            color="attempt"
            ))

fig.show()