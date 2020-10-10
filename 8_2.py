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

def get_shop_list_by_dishes(menu, persons = int):
    cook_book = new_cook_book()
    shop_list = {}

    for dishes in menu:
        for recepie in cook_book.keys():
            if recepie == dishes:
                for ingredient in cook_book[recepie]:
                    if ingredient['ingredient_name'] in shop_list.keys():
                        shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * persons
                    else:
                        shop_list.update({ingredient['ingredient_name']: {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * persons}})

    return(shop_list)

pp.pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))
