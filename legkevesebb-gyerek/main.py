import sys


def count_children(input_lines):
    parents = {}  # key: id of parent; value: number of children they have
    for i in range(1, len(input_lines)):
        parent_id, child_id = input_lines[i].split(" ")
        parent_id = int(parent_id)
        if parent_id in parents:
            parents[parent_id] += 1
        else:
            parents[parent_id] = 1
    parents_ordered = list(parents.items())
    return sorted(parents_ordered)


def find_parent_with_least_amount_of_children(parents):
    parent_with_least_amount_of_children = ""
    min_number_of_children = 1001
    for parent_id, count in parents:
        if count < min_number_of_children:
            min_number_of_children = count
            parent_with_least_amount_of_children = parent_id
    return parent_with_least_amount_of_children


def main():
    input_lines = sys.stdin.readlines()
    parents = count_children(input_lines)
    parent_id = find_parent_with_least_amount_of_children(parents)
    sys.stdout.write(str(parent_id))


if __name__ == '__main__':
    main()
