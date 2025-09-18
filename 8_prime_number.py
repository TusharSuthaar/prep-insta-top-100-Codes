num = input(int("Enter a number: "))
is_prime = True
for i in range(2, int(num)):
    if int(num) % i == 0:
        is_prime = False
        break
if is_prime:
    print("Prime")
else:
    print("Not Prime")
