# The tool used to get all the permutations
from more_itertools import distinct_permutations


def sort_paths(right_count: int, down_count: int):
    original = list()
    right_range = range(right_count)
    down_range = range(down_count)
    for i in right_range:
        original.append("R")
    for i in down_range:
        original.append("D")

    return distinct_permutations(original)


def get_sum(path):
    depth = 1
    sum_num = 1
    for i in range(len(path)):
        if path[i] == 'R':
            sum_num += depth
        else:
            depth += 1
            sum_num += depth
    return sum_num


def main():
    m = 90000
    n = 100000
    target_sum = [87127231192,5994891682]
    file = open('output_question_1_2.txt', 'w')

    for path in sort_paths(n-1,m-1):
        sum_num = get_sum(path)
        for target in target_sum:
            if sum_num == target:
                print(target,''.join(path))
                s = str(target).replace("'", '') + ' ' + ''.join(path) + '\n'
                file.write(s)
    file.close()


if __name__ == '__main__':
    main()