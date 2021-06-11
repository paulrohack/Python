<<<<<<< HEAD

def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    if n % 2 != 0:
        return int(3*n + 1)
    else:
        return 'Error'


n = int(input("n = "))
d = [n]
steps = 0

while True:
    if n != 1:
        #print(n)
        n = collatz(n)
        steps += 1
        d.append(n)
    else:
        #print("1\n")
        print(d)
        print(f"It Took {steps} steps")
        break
=======

def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    if n % 2 != 0:
        return int(3*n + 1)
    else:
        return 'Error'


n = int(input("n = "))
d = [n]
steps = 0

while True:
    if n != 1:
        #print(n)
        n = collatz(n)
        steps += 1
        d.append(n)
    else:
        #print("1\n")
        print(d)
        print(f"It Took {steps} steps")
        break
>>>>>>> 1716e3ac153e6b6805d02dd7397be643a7ac4293
