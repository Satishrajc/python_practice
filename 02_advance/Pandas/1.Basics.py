import pandas as pd

data = {
    'name': ['Satish', 'Niteen', 'Rakesh'],
    'marks': [20, 30, 40],
    'city': ['Shinal', 'Tangadi', 'Katral'],
}

df = pd.DataFrame(data)

print(df)

df.to_csv('test.csv')
