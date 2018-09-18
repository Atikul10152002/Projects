last_num = 4
lucas_num = [last_num]
for i in range(10):
    calc = last_num ** 2 - 2
    lucas_num.append(calc)
    last_num = calc

def check(n):
    var = 2**n-1
    new_lucas_num = []
    for i in range(n-2):
        if i >= n:
            pass
    if new_lucas_num[n-2] % var == 0:
        print(var, "is prime")

def main():
    for i in range(2,10):
        check(i)


main()
