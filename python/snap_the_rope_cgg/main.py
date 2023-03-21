import random

def snap_the_ropes(big_weights, newtons):
    # Output: [[2], [-1], [0]]
    if big_weights == 0:
        total_drop = newtons
        list_result_big_drop = [-1]
        list_result_small_drop = [0]
    else:
        list_sort_newton = sorted(newtons)
        big_drop = list_sort_newton[-4:]
        small_drop = list_sort_newton[:-4]

        total_drop = [len(big_drop) + sum(small_drop)]
        # print(result)
        list_result_big_drop = []
        list_result_small_drop = []
        for i in range(len(newtons)):
            check_drop = newtons[i]

            if check_drop in big_drop:
                list_result_big_drop.append(newtons.index(check_drop))
            elif check_drop in small_drop:
                list_result_small_drop.append(newtons.index(check_drop))
    result = [total_drop, list_result_big_drop, list_result_small_drop]
    return result

big_weights = 0
newtons = [2]
print(snap_the_ropes(big_weights, newtons)) # Output: [[2], [-1], [0]]

big_weights = 4
newtons = [3, 2, 5, 4, 6, 7, 9]
print(snap_the_ropes(big_weights, newtons)) # Output: [[13], [2, 4, 5, 6], [0, 1, 3]]


big_weights = random.randint(0, 210)
newtons = random.sample(range(0, 218), 210)
print(snap_the_ropes(big_weights, newtons))

    # Constraints
    # •	1 <= n <= 2*105
    # •	0 <= bigWeights <= 2*105
    # •	1 <= newtons[i] <= 2*109
    # •	Elements in newtons[n] are distinct



