def flatten(my_list):

    result = []

    for item in my_list:
        if isinstance(item, list):
            print(f"Reading item: {item}")
            print("\nList found!")
            print("Checking elements...\n")
            flat_list = flatten(item)
            result += flat_list
        else:
            print(f"Reading item: {item}")
            print(f"Appending item: {item}\n")
            result.append(item)
    return result


planets = [
    "mercury",
    "venus",
    ["earth"],
    "mars",
    [["jupiter", ["saturn"]]],
    "uranus",
    ["neptune", "pluto"],
]

print(flatten(planets))
