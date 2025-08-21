num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")
