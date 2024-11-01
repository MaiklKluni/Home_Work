def calculate_structure_sum(*elements, sum = 0):
    for element in elements:
        if isinstance(element, list):
            sum += calculate_structure_sum(*element)
        elif isinstance(element, dict):
            sum += calculate_structure_sum(*list(element.items()))
        elif isinstance(element, tuple):
            if not element:
                continue
            else:
                sum += calculate_structure_sum(*list(element))
        elif isinstance(element, set):
            sum += calculate_structure_sum(*list(element))
        elif isinstance(element, str):
            sum += len(element)
        elif isinstance(element, int):
            sum += element
    return sum



data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(*data_structure)
print(result)
