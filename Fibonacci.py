# Fibonacci - Victor Freire(devbuda)

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
if __name__ == "__main__":
    n = int(input("Enter how many terms you want to show: "))
    print("\nFIBONACCI SEQUENCE: ")
    for i in range(n):
        print(f"{fibonacci(i)}", end=" - ")
print("END\n")
