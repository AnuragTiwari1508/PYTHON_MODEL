def fibonacci(n:int):
    if(n<=2):
        if (n==1):
            return 0
        else:
            return 1
    else:
        series=fibonacci(n-1)+fibonacci(n-2)
        return series
n=int(input("Enter the number of terms: "))
for i in range(1,n+1):
    print(fibonacci(i))
