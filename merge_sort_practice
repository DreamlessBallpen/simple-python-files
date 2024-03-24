import random
def give_ul(lb, ub, item_count):
    ul = [random.randint(lb, ub+1) for x in range(item_count)]
    return ul


def merge_sort(ul) -> []:
    if len(ul) == 1:
        return ul

    def merge(list_one, list_two)->[]:
        first_pointer = 0
        second_pointer = 0
        new_list = []
        while first_pointer < len(list_one) and second_pointer < len(list_two):
            if list_one[first_pointer] <= list_two[second_pointer]:
                new_list.append(list_one[first_pointer])
                first_pointer += 1
            else:
                new_list.append(list_two[second_pointer])
                second_pointer += 1
        while first_pointer < len(list_one):
            new_list.append(list_one[first_pointer])
            first_pointer += 1
        while second_pointer < len(list_two):
            new_list.append(list_two[second_pointer])
            second_pointer += 1
        return new_list
    
    midpoint = int(len(ul) / 2)
    left_list = ul[:midpoint]
    right_list = ul[midpoint:]

    return merge(merge_sort(left_list), merge_sort(right_list))

a = give_ul(0, 100, 20)
print(a)
b = merge_sort(a)
print(b)
