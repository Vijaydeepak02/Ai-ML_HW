##Create three star-pattern programs using nested loops. Focus on loop logic and clean formatting.##
n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()