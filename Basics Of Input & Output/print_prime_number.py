n = int(input())

def check_prime(n):
    counter = 0
    for i in range(1,n+1):
        if n%i == 0:
            counter += 1
        if counter > 2 and i < n:
            return(None)
    if counter == 2:
        return(n)
        
for i in range(n):
    if check_prime(i) == None:
        continue
    else:
        print(check_prime(i), end = " ")
