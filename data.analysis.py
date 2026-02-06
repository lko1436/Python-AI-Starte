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

import matplotlib.pyplot as plt

df.plot(kind='bar', x='name', y='return_rate', color='skyblue')
plt.title('Asset Return Rate Analysis')
plt.xlabel('Asset Name')
plt.ylabel('Return Rate (%)')

plt.show()

print("\n" + "="*30)
print("AI 自動化篩選報告")

high_return = df[df['return_rate'] > 40]

if not high_return.empty:
    print("偵測到高報酬資產!清單如下:")
    print(high_return[['name', 'return_rate']])
else:
    print("目前沒有資產達到預警標準。")
print("="*30)