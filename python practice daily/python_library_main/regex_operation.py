import pandas as pd

# Sample DataFrame
data = {'Text': ['Hello 123', 'World 456', 'Python 789']}
df = pd.DataFrame(data)

# Replace digits with 'X' in the 'Text' column using regex
df['Text'] = df['Text'].str.replace(r'\d+', 'X')

print(df)



import pandas as pd

# Sample DataFrame
data = {'Text': ['Product ID: 1234', 'Product ID: 5678', 'Product ID: 9876']}
df = pd.DataFrame(data)

# Extract numbers following 'Product ID:' into a new column using regex
df['Product_ID'] = df['Text'].str.extract(r'Product ID: (\d+)')

print(df)
