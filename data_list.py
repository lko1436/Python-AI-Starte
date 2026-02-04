prices = [100, 200, 300, 400]

print(prices[2])
print(prices[3])

print("--- 開始自動跑迴圈 ---")
for p in prices:
    print("這檔資產的價格是:" + str(p))

print("\n--- 批量報酬率計算結果 ---")

current_price = 500 

for buy_price in prices:
    rate = ((current_price - buy_price) / buy_price) * 100
    
    if rate > 100:
        print(" 發現飆股 ! 買價" + str(buy_price) + " 報酬率高達:" + str(round(rate, 2)) + "%")
    else:
        print("平穩成長中:買價 " + str(buy_price))