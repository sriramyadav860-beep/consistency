str1 = "sri"
str2 = "ram"
result = str1 + str2
print(result)

a = "hello"
b = "world"
print(a+b)

a = "abc"
print(a*3)

s = "python"
a = s[0]
b = s[-1]
print("frist latter:",a)
print("last latter:",b)

s = "hello"
a = s[::-1]
print(a)

s = "PyThoN"
print(s.lower())  
print(s.upper())  

s="Python"
print(len(s))

str1 = input()
str2 = input()
print(str1 + str2)

text = input()
print(len(text))

s = input()
print(s[0])
print(s[-1])

s = input()
print(s[::-1])

s = input()
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(count)

s = "Python"
print("thon" in s)

s = "Python"
print(s.replace("P", "J"))

s = "Python"
for ch in s:
    print(ch)

s = "Python"
print(s + " Programming")

s = "Python"
print(s[1], s[-2])

s = "Python"
print(s[:3])

s = "Python"
print(s[-3:])



