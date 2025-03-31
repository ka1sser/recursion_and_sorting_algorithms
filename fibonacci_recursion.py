def fibonacci(n):

    if n == 1:
        print(f"Callstack: fibonacci({n})")
        print(f"Execution Context: {n}, {n-1}")
        return 1
    if n == 0:
        print(f"Callstack: fibonacci({n})")
        print(f"Execution Context: {n}")
        return 0
    print(f"Callstack: fibonacci({n})")
    print(f"Execution Context: {n-2}, {n-1}")
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(5))
