name="Sriram"
age=25
salary=50000
print(name,age,salary)

a=10
b=20
a,b =b,a
print(a,b)

print(type(10))
print(type(10.5))
print(type("Python"))
print(type(True))

x=10.9
print(int(x))
s="100"
print(int(s))
n=50
print(str(n))

a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a**b)

a = int(input())
b = int(input())
if a > b:
    print("a is larger")
elif b > a:
    print("b is larger")
else:
    print("Both equal")

a = int(input())
b = int(input())
c = int(input())
if a > 0 and b > 0 and c > 0:
    print("All positive")
elif a < 0 or b < 0 or c < 0:
    print("At least one negative")

