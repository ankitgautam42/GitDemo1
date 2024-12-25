str = "RahulShettyAcademy.com"
str1 = "consulting firm"
str3 = "RahulShetty"
str4 = "RahulddddShetty"
print(str[1])
print(str[0:5])
print(str+str1)
print(str3 in str)
print(str4 in str)

var = str.split(".")
print(var)
print(var[0])
print(var[1])

str5 = "    great           "
print(str5.strip())
print(str5.lstrip())
print(str5.rstrip())
