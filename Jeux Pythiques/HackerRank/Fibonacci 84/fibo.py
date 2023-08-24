fibo = [0, 1]
n = int(input())
if n < 0:
    print("PositifSvp")
elif n == 0:
    print("0")
elif n == 1:
    print("0 1")
else:
    [fibo.append(fibo[-2]+fibo[-1]) for i in range(n-1)]
    print("  ".join(str(i) for i in fibo))