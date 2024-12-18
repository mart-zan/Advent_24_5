

# Advent of Code 2024
# --- Day 5: Print Queue ---


def read_input_by_rows(filename: str):

    with open(filename, "r") as my_file:
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
        # If X or Y is not in the list
        return False


if __name__ == '__main__':

    # Read input
    rules_updates = read_input_by_rows('input.txt')

    # Separate rules and updates
    idx_separate = rules_updates.index('')
    print(idx_separate)
    rules = rules_updates[:idx_separate]
    updates = rules_updates[(idx_separate+1):]

    # valid_updates = []
    middle_sum = 0
    for update in updates:
        # print(update)
        update = update.split(',')
        update = list(map(int, update))
        correct = True

        for rule in rules:
            X = int(rule[0:2])
            Y = int(rule[3:5])

            if X in update and Y in update:
                if not is_before(update, X, Y):
                    correct = False
                    # End cycle if at least one mistake
                    break
        if correct:
            # valid_updates.append(update)
            middle_index = len(update) // 2
            middle_sum += update[middle_index]

    # print(valid_updates)

    print('The final middle sum is', middle_sum, '.')
