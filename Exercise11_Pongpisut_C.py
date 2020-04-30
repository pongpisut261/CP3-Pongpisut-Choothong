height = int(input("enter height of pyramid :"))
for i in range(height):
    print(" " * (height - i), "*" * (i*2+1))