# Fibonacci - Victor Freire(devbuda)

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
if __name__ == "__main__":
    n = int(input("Informe quantos termos deseja mostrar: "))
    print("\nSEQUÊNCIA FIBONACCI: ")
    for i in range(n):
        print(f"{fibonacci(i)}", end=" - ")
print("FIM\n")
