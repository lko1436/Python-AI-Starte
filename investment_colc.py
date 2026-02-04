buy_price = float(input("請輸入買入價格:"))
current_price = float(input("請輸入目前價格"))
return_rate = ((current_price - buy_price) / buy_price) * 100
print("目前的報酬率是 :" + str(round(return_rate, 2)) + "%")
if return_rate > 0:
    print("賺錢了")
else:
    print("虧錢了")
