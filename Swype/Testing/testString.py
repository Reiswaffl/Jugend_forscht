def splitXY(str1):
    xy = str1.split(",")
    return xy

strInput = "100,100"
x,y = splitXY(strInput)

print(x + "  -  " + y)