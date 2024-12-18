import pandas as pd

# File path and sheet details
file_path = './data_set/EZ_Jharkhand_RAN_KPI_Phase_2_daily_06_12_2024.xlsx'
sheet_name = 'RAN KPI Report Phase2'
header_column = 'LOCATION'

# Load the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Inspect column names and data
# print(df.columns)
# print(df.head())

# Handling Non-Numeric Data Before grouping, some columns might have non-numeric data (e.g., Date, 4G Cell Name). 
# Convert them into appropriate types or exclude them if they're not needed for aggregation:

numeric_cols = df.select_dtypes(include=['number']).columns
# print(numeric_cols)

# Group Data by LOCATION Sum numeric columns grouped by LOCATION to get aggregated metrics:
data_group = df.groupby(header_column)[numeric_cols].sum()
# print(data_group)

data_vol = df.groupby(header_column)[['Data Volume - Total (GB)','VOLTE Traffic (Erlang)']].sum()
# print(data_vol)

# data_group.to_excel('./aggregated_data.xlsx', index=True)





