# Occurance of each element in given list

def count_occurrences(elements):
    occurrence_dict = {}
    for element in elements:
        if element in occurrence_dict:
            occurrence_dict[element] += 1
        else:
            occurrence_dict[element] = 1
    return occurrence_dict

elements = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,5,4,9,0]

occurrences = count_occurrences(elements)

for element, count in occurrences.items():
    print(f"Element {element} occurs {count} times")

            
            