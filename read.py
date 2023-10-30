import pandas as pd

# Specify the file path
file_path = r'C:\Users\R_w_e_m_a\Desktop\bdominiq\ebola.xls'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Now, you can work with the DataFrame 'df' as needed
print(df.head())  # This will print the first few rows of the DataFrame
