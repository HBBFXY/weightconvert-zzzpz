def weight_conversion():
    weight_input = input().strip().lower()
    if weight_input.endswith('kg'):
        value = float(weight_input[:-2])
        pounds = value * 2.2046
        print(f"对应的英制重量为{pounds:.3f}磅")
    elif weight_input.endswith('pd'):
        value = float(weight_input[:-2])
        kilograms = value / 2.2046
        print(f"对应的公制重量为{kilograms:.3f}公斤")
