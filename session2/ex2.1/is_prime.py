def is_prime():
    number = int(input())
    counter = 0
    if number < 2:
        print("not prime")
    else:
        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1
        if counter > 2:
            print("not prime")
        else:
            print("prime")


is_prime()
