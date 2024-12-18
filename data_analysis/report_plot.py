import pandas as pd
import matplotlib.pyplot as plt

# File path and sheet details
file_path = './data_set/EZ_Jharkhand_RAN_KPI_Phase_2_daily_06_12_2024.xlsx'
sheet_name = 'RAN KPI Report Phase2'
header_column = 'LOCATION'

# Load the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)
numeric_cols = df.select_dtypes(include=['number']).columns
# print(numeric_cols)

# Group Data by LOCATION Sum numeric columns grouped by LOCATION to get aggregated metrics:
data_group = df.groupby(header_column)[numeric_cols].sum()

# Plot total data volume per location
data_group['Data Volume - Total (GB)'].plot(kind='bar', figsize=(12, 6))
plt.title('Total Data Volume by Location')
plt.xlabel('Location')
plt.ylabel('Data Volume (GB)')
plt.show()
