from pprint import pprint
def check_if_symbol(character: str):
    if character and character != "\n" and not character.isnumeric() and character != "." and character != "" and character != " ":
        return True
    return False

def scan_for_symbol(l_idx, start_c_idx, end_c_idx, file):
    # Check to the left, right
    if (start_c_idx > 0 and check_if_symbol(file[l_idx][start_c_idx - 1])) \
        or (end_c_idx < len(file[l_idx]) and check_if_symbol(file[l_idx][end_c_idx])):
        return True
    range_to_check = [i for i in range(start_c_idx, end_c_idx)]
    if range_to_check == []:
        range_to_check = [ start_c_idx ]
    for i in range_to_check:
        # Check above and above diagonally
        if start_c_idx == 0 and (check_if_symbol(file[l_idx - 1][i]) or \
            check_if_symbol(file[l_idx -1][i+1]) or \
            check_if_symbol(file[l_idx -1][i])):
            return True
        if l_idx > 0 and (check_if_symbol(file[l_idx - 1][i]) or \
            check_if_symbol(file[l_idx -1][i+1]) or \
            check_if_symbol(file[l_idx -1][i-1])) :
            return True
        # Check below and below diagonally 
        if l_idx + 1 < len(file) and (check_if_symbol(file[l_idx + 1][i-1]) or \
            check_if_symbol(file[l_idx + 1][i + 1]) or \
            check_if_symbol(file[l_idx + 1][i])):
            return True
    return False

def part_one():
    total = 0
    parts = []
    with open('input.txt', 'r') as f:
        file = [line for line in f]
        for l_idx, line in enumerate(file):
            number = ""
            is_valid = False
            number_start = -1
            for c_idx, c in enumerate(line):
                if c.isnumeric():
                    if number_start == -1:
                        number_start = c_idx
                    number += c
                    if c_idx == len(line) - 1 and number != "":
                        # print("found a number", number)
                        # print(number_start, c_idx)
                        is_valid = scan_for_symbol(l_idx, number_start, c_idx, file)
                        # print("is number valid", is_valid)
                        if is_valid:
                            parts.append(int(number))
                else:
                    if number != "" and number_start != -1:
                        is_valid = scan_for_symbol(l_idx, number_start, c_idx, file)
                        if is_valid:
                            parts.append(int(number))
                        number = ""
                        number_start = -1
    total += sum(parts)
    pprint(parts)
    print(total)

def chunkitize(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def find_the_number_back(end, line):
    found_number = False
    number = ""

    if line[end].isnumeric():
        next = end
        while(not found_number):
            next = next - 1
            if line[next].isnumeric():
                number = line[next:end]
                found_number = True
    if found_number:
        return True, number
    return False, ""

def find_the_number_forward(start, line):
    found_number = False
    number = ""

    if line[start].isnumeric():
        next = start
        while(not found_number):
            next = next + 1
            if line[next].isnumeric():
                number = line[start:next]
                found_number = True
    if found_number:
        return True, number
    return False, ""

def part_two():
    total = 0
    parts = []
    with open('input.txt', 'r') as f:
        file = [line for line in f]
        for l_idx, line in enumerate(file):
            for c_idx, c in enumerate(line):
                if c == "*":
                    left_number = ""
                    right_number = ""
                    # Look to the left directly
                    found, left_number = find_the_number_back(c_idx - 1, line)
                    # Look up to the left
                    if not found:
                        t_line = file[l_idx -1]
                        t_c_idx = c_idx
                        while(not found):
                            found, left_number = find_the_number_back(t_c_idx, t_line)
                            t_c_idx = t_c_idx - 1
                    # Look up to the right
                    found, right_number = find_the_number_forward(c_idx + 1, line)
                    if not found:
                        t_line = file[l_idx +1]
                        t_c_idx = c_idx
                        while(not found):
                            found, right_number = find_the_number_forward(t_c_idx, t_line)
                            t_c_idx = t_c_idx + 1
                    if left_number != "" and right_number != "":
                        print(left_number, right_number)
                        product = int(left_number) * int(right_number)
                        parts.append(product)


    print(len(parts))
    pprint(parts)
    # chunked_parts = list(chunkitize(parts, 2))
    # print(sum([ p[0] * p[1] for p in chunked_parts]))
    # print(total)
    
if __name__ == "__main__":
    # part_one()
    part_two()