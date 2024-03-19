def fibonacci_sequence(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        next_term = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_term)
    return fibonacci[:n]

def main():
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        sequence = fibonacci_sequence(n)
        print("Fibonacci sequence:", sequence)

if __name__ == "__main__":
    main()
