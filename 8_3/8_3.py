def foo(**files):
    list_fi = {}
    for i in files.values():
        with open(i) as f:
            l = 0
            for line in f:
                l += 1
        list_fi.update({i:l})

    list_dict = list(list_fi.items())
    list_dict.sort(key=lambda i: i[1])
    
    with open('4.txt', 'w') as docum:
        for i in list_dict:
            docum.write(i[0])
            docum.write('\n')
            docum.write(str(i[1]))
            docum.write('\n')
            with open(i[0]) as t:
                for i in t:
                    docum.write(i)
            docum.write('\n')

foo(f_1 = '2.txt', f_2 = '1.txt', f_3 = '3.txt')

