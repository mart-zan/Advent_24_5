

# Advent of Code 2024
# --- Day 5: Print Queue ---


def read_input_by_rows(filename: str):

    my_file = open(filename, "r")
    data = my_file.read()
    # Split text into each row
    rows = data.strip().split('\n')
    return rows

def is_before(lst, X, Y):
    try:
        # Find the index of X and Y
        index_X = lst.index(X)
        index_Y = lst.index(Y)
        # Check if X is before Y
        return index_X < index_Y
    except ValueError:
        # If X or Y is not in the list, return False
        return False


if __name__ == '__main__':
    print('PyCharm')

    # Read input
    rules_updates = read_input_by_rows('input.txt')

    # Separate rules and updates
    bool_separate = [len(ele) == 0 for ele in rules_updates]
    idx_separate = [i for i, x in enumerate(bool_separate) if x]
    rules = rules_updates[:(idx_separate[0])]
    updates = rules_updates[(idx_separate[0]+1):]
    # print(len(rules))
    # print(len(updates))
    # print(rules[0], ', ', rules[-1])
    # print(updates[0], ', ', updates[-1])

    for update in updates:
        print(update)
        update = update.split(r',')
        update = list(map(int, update))
        for u in range(0, len(update)):
            print(update)
            number = update[u]
            print(number)
            for rule in rules:
                # print(rule)
                X = int(rule[0:2])
                Y = int(rule[3:5])
                # print(X)
                # print(Y)
                # print()
                if X == number:
                    # index_X = update.index(X)
                    # index_Y = update.index(Y)
                    # index_X < index_Y
                    # check = is_before(update, update, )

                    print('update')
