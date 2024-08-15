import pandas as pd
df = pd.read_csv("/Users/supasunkhumpraphan/Desktop/mickey_work/qsworld2024/qs_world2024.csv")
df_choose_feature = df[["2024 RANK","2023 RANK","Institution Name","Country"]]
df_choose_location = df_choose_feature[(df_choose_feature["Country"] != "Canada") & (df_choose_feature["Country"] != "United States") & (df_choose_feature["Country"] != "United Kingdom") & (df_choose_feature["Country"] != "Australia")]

print(df_choose_location)
# df_choose_location['2024 RANK'] = df_choose_location['2024 RANK'].map(lambda x : int(x))
# print(df_choose_location)


df_choose_location.to_csv("/Users/supasunkhumpraphan/Desktop/mickey_work/qsworld2024/qs_world2024_othercountry.csv")