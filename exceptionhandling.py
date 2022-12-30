def Div():
    try:
        input_1 = int(input("enter input_1"))
        input_2 = int(input("enter input_2"))
    except ValueError:                                               #bank custname ifsc code    methods
        print("value should be integer")
    finally:
        res = input_1 / input_2
        print(res)
abs=Div()


