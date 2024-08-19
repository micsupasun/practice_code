import pandas as pd
def export_country(name_country):
    df = pd.read_csv("/Users/supasunkhumpraphan/Desktop/car/qs_world_ranking/qs-world-rankings-2025.csv")
    df_choose_column = df[["2025 Rank","2024 Rank","Institution Name","Location Full"]][:500]
    df_choose_country = df_choose_column[df_choose_column["Location Full"] == f"{name_country}"].reset_index()
    df_choose_country = df_choose_country.drop(columns=['index', 'Location Full'])
    df_choose_country.to_csv(f"/Users/supasunkhumpraphan/Desktop/car/qs_world_ranking/{name_country}.csv")
    return df_choose_country

export_file = export_country("Australia")
print(export_file)

# import pandas as pd

# df = pd.read_csv("/Users/supasunkhumpraphan/Desktop/car/qs_world_ranking/qs-world-rankings-2025.csv")
# df_choose_column = df[["2025 Rank","2024 Rank","Institution Name","Location Full"]][:500]
# df_choose_country = df_choose_column[(df_choose_column["Location Full"] == "Australia") | (df_choose_column["Location Full"] == "United Kingdom") | (df_choose_column["Location Full"] == "United States")].reset_index()
# df_choose_country = df_choose_country.drop(columns=['index'])
# df_choose_country.to_csv(f"/Users/supasunkhumpraphan/Desktop/car/qs_world_ranking/all_country.csv")


#