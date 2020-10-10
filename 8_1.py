import pprint as pp

def new_cook_book():
    all_in_list = []
    cook_book = {}
    n = 0

    with open('recipes.txt', 'r') as r:
        for line in r:
            if line.strip():
                all_in_list.append(line.strip())

    while n < len(all_in_list):

        dish = all_in_list[n]
        ingr_list = []
        m = 0
        while m < int(all_in_list[n + 1]):
            ingr = all_in_list[n + 2 + m].split('|')
            ingr_list.append({'ingredient_name': ingr[0].strip(), 'quantity': int(ingr[1]), 'measure': ingr[2].strip()})
            m += 1

        cook_book.update({dish: ingr_list})
        n += (2 + m)

    return cook_book

pp.pprint(new_cook_book())
