for i in range(1, 21, 2):
    print(i, end=' ')
print()

for a in range(0, 101, 10):
    print(a, end=' ')
print()

for b in range(20, 0, -1):
    print(b, end=' ')
print()

stars = int(input("Enter stars: "))
for c in range(0, stars):
    print("*", end=' ')
print()

for d in range(0, stars):
    for e in range(0, d+1):
        print("*", end="")
    print("\r")
print()