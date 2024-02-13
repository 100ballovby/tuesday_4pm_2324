def union_str(str_list):
    string = ""
    for i in range(len(str_list)):
        string += str_list[i] + ', '
    return string


def task2(numlist):
    generated = []
    middle = 0
    summ = 0

    for i in range(len(numlist)):
        summ += numlist[i]
    middle = summ / len(numlist)
    for i in range(len(numlist)):
        if numlist[i] > middle:
            generated.append(numlist[i])
    return generated


def task2_v2(numlist):
    generated = []
    middle = sum(numlist) / len(numlist)
    for i in range(len(numlist)):
        if numlist[i] > middle:
            generated.append(numlist[i])
    return generated


list_s = ['Hello world', 'Lorem ipsum',
          'Some text', 'Another text',
          'One more long text']
new_str = union_str(list_s)
print(new_str)

list_n = [4, 6, 12, 8, -4, 3, 1, 7, 13]
gen = task2(list_n)
gen2 = task2_v2(list_n)
print(gen)
print(gen2)
