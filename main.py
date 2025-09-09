# WeightConvert.py
WeightStr = input().strip().lower()

if WeightStr.endswith('kg'):
    # 千克转换为磅
    value = float(WeightStr[:-2])
    pounds = value * 2.2046
    print("{:.3f}pd".format(pounds))
elif WeightStr.endswith('pd'):
    # 磅转换为千克
    value = float(WeightStr[:-2])
    kilograms = value / 2.2046
    print("{:.3f}kg".format(kilograms))
else:
    print("输入格式错误")
