pin="1234"
entered=""
attempts=3

while entered!=pin and attempts>0:
    entered=input("Enter your pin:")

    if entered==pin:
        print("Access granted")

    else:
        attempts-=1
        print("wrong pin")
        print("attempts left",attempts)

if attempts==0:
    print("Your Card Is blocked")


