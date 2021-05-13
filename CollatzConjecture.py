from matplotlib import pyplot as plt

def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    if n % 2 != 0:
        return int(3*n + 1)
    else:
        return 'Error'


n = int(input("n = "))
d = []
steps = 0
while True:
    if n != 1:
        #print(n)
        n = collatz(n)
        steps += 1
        d.append(n)
    else:
        #print("1\n")
        print(f"It Took {steps} steps")
        break

Purple = '#9D2EC5'

plt.plot(d[::-1], d, Purple, linewidth=3)
plt.show()