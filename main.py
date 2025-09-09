# WeightConvert.py
WeightStr = input("请输入带有符号的重量值：")
if WeightStr[-2:] in ['kg','KG']:
    P = eval(WeightStr[0:-2]) * 2.2046
    print("转换后的重量是{:.3f}pd".format(P))
elif WeightStr[-2:] in ['pd','PD']:
    K = eval(WeightStr[0:-2]) / 2.2046
    print("转换后的重量是{:.3f}kg".format(K))
