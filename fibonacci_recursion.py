def fibonacci(n):

    if n == 1:
        print(f"Callstack: fibonacci({n})")
        print(f"Execution Context: fibonacci({n}), fibonacci({n-1})\n")
        return 1
    if n == 0:
        print(f"Callstack: fibonacci({n})")
        print(f"Execution Context: fibonacci({n})\n")
        return 0
    print(f"Callstack: fibonacci({n})")
    print(f"Execution Context: fibonacci({n-2}), fibonacci({n-1})\n")
    return fibonacci(n - 2) + fibonacci(n - 1)
