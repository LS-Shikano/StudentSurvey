import pandas as pd
import json 


df_w1 = pd.read_csv("W1_AllAppsWide_2024-11-13-4.csv")
df_w1 = df_w1.query('`session.code` == "3m87qmko" | `session.code` == "wt9ndgb1"')

df_w2 = pd.read_csv("W2_all_apps_wide_2024-12-10-2.csv")
df_w2 = df_w2.query('`session.code` == "2n8orvug"')
df_w2["participant.label"][244] = "nan" # fixing the missing label

df_w3 = pd.read_csv("W3_all_apps_wide_2025-01-29.csv")
df_w3 = df_w3.query('`session.code` == "7uy8unkt"')
df_w2["participant.label"][46] = "nan" # fixing the missing label

df_w1['R1'] = 1
df_w2['R2'] = 1
df_w3['R3'] = 1

df = pd.merge(df_w1, df_w2, how = "outer")
df = pd.merge(df, df_w3, how = "outer")

df = df[["participant.label", "R1", "R2", "R3", "end_app.1.player.rnumber"]]