import pandas as pd
df = pd.read_csv('assets.csv')
print("--- 這是我的資產清單 ---")
print(df)
print("\n --- 所有的買入價格 ---")
print(df['buy_price'])
print(df['buy_price'] * 1.1)
df['current_price'] = df['buy_price'] * 1.5
df['return_rate'] = ((df['current_price'] - df['buy_price']) / df['buy_price']) * 100
print(df)