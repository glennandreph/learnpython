mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: {}".format(mystring))

if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: {}".format(myfloat))

if isinstance(myint, int) and myint == 20:
    print("Integer: {}".format(myint))
