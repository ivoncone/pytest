import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Emily'],
		'Age': [25, 30, 35, 40]}

df = pd.DataFrame(data)

df['Folio'] = range(1, len(df) + 1)

df.to_excel('output.xlsx', index=False)