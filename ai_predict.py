import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'size': [10, 20, 30, 40, 50],
    'price': [510, 980, 1550, 2020, 2450]
}
df = pd.DataFrame(data)

model = LinearRegression()

X = df[['size']]
y = df['price']
model.fit(X, y)

print("--- AI 模型訓練完成 ---")

new_size = [[35]]
prediction = model.predict(new_size)

print("AI 預測 35 坪的房子價格應該是:" + str(prediction[0]) + " 萬元")