number_of_groups = eval(input())
group_sizes = input().split(" ")

# Turn all into numbers
group_sizes = [int(x) for x in group_sizes]

number_of_taxis = 0
group_sizes.sort()

# add up until the groups are 4
for index, size in enumerate(group_sizes):
    for another_index, another_size in enumerate(group_sizes):
        if size == 1 and another_size == 3:
            group_sizes[another_index] = 4
            group_sizes[index] = 5
            break
        if size == 2 and another_size == 2 and another_index != index:
            group_sizes[another_index] = 4
            group_sizes[index] = 5
            break
        elif size == 1 and another_size == 2:
            group_sizes[another_index] = 3
            group_sizes[index] = 5
            break
        # TODO: figure this out

# put each group of 4 in a taxi
for group in group_sizes:
    if group <= 4:
        number_of_taxis += 1

print(number_of_taxis)

# This is harder than I thought
