arr_of_x = [2]
n = int(input("Pls enter n: "))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def func_of_method(x):
    return int((pow(x,2) + x +1) % n)

def pollard(n):
    arr_of_x.append(func_of_method(arr_of_x[-1]))
    print(arr_of_x)
    if arr_of_x[-1] == arr_of_x[-2]:
        print("Sorry,its neudacha(c)")
        return 0
    for i in range(0,len(arr_of_x)-1):
        gcd_now = gcd(arr_of_x[-1] - arr_of_x[i],n)
        print("Gcd of (x{0} = {1} - x{2} = {3}, {4}) = {5}".format(len(arr_of_x),arr_of_x[-1], i , arr_of_x[i], n, gcd_now))
        if int(gcd_now) == 1:
            print("sry, gcd = 1,continue")
        else:
            print(gcd_now)
            print("n = "+str(gcd_now)+"*"+str(int(n/gcd_now)))
            return gcd_now
    pollard(n)

pollard(n)