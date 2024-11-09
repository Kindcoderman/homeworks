data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    sumator = 0
    bank = []
    for item in data_structure:
        if isinstance(item, (list, set, tuple)):
            bank.extend(item)
        elif isinstance(item, (int, str)):
            bank.append(item)
        elif isinstance(item, dict):
            for key in item:
                bank.append(key)
                bank.append(item[key])
    if all(isinstance(i, (int, str)) for i in data_structure):
        for element in bank:
            if isinstance(element, str):
                sumator += len(element)
            elif isinstance(element, int):
                sumator += element
        print(sumator)
    else:
        calculate_structure_sum(bank)
    return sumator


calculate_structure_sum(data_structure)
