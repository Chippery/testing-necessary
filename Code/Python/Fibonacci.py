fibonacci = [0, 1]
sequence = []


def generate_fibonacci(n):
    for i in range(0, n):

        result = fibonacci[0] + fibonacci[1]
        sequence.append(result)

        fibonacci.append(result)
        fibonacci.pop(0)
    print(sequence)

generate_fibonacci(100)
