import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}
print("hehe:)")
a = input("Enter the first value: ")
b = input("Enter the second value: ")
arithmetic = input("Enter a arithmetic: ")
print(ops[arithmetic](int(a), int(b)))