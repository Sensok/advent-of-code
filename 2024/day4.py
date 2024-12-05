def part_one(complete_input: list[list[str]]):
    find_count = 0
    search_letter = 'X' 
    search_word = 'XMAS' 
    number_rows = len(complete_input)
    for r in range(number_rows):
        row_length = len(complete_input[r])
        for c in range(row_length):
            if complete_input[r][c] == search_letter:
                # Search Forward
                if  c < row_length - 3:
                    if "".join(complete_input[r][c:c+4]) == search_word:
                        print(r,c, "Found Forward")
                        find_count += 1
                # Search Backward
                if c - 3 >= 0:
                    if "".join(complete_input[r][c-3:c + 1]) == search_word[::-1]:
                        find_count += 1
                        print(r,c, "Found Backward")
                # Search Up
                if r >= 3:
                    up_word = complete_input[r][c] + complete_input[r - 1][c] + complete_input[r - 2][c] + complete_input[r - 3][c]
                    print("looking up", r, c)
                    if up_word == search_word:
                        find_count += 1
                        print(r,c, "Found Up")
                    if c - 3 >= 0:
                        # Search Diagonally Up Left
                        dul_word = complete_input[r][c] + complete_input[r - 1][c - 1] + complete_input[r - 2][c - 2] + complete_input[r - 3][c - 3]
                        if dul_word == search_word:
                            find_count += 1
                            print(r,c, "Found DUL")
                    if c < row_length - 4:
                        # Search Diagonally Up Right
                        dur_word = complete_input[r][c] + complete_input[r - 1][c + 1] + complete_input[r - 2][c + 2] + complete_input[r - 3][c + 3]
                        if dur_word == search_word:
                            find_count += 1
                            print(r,c, "Found DUR")
                # Search Down
                if r < number_rows - 3:
                    down_word = complete_input[r][c] + complete_input[r + 1][c] + complete_input[r + 2][c] + complete_input[r + 3][c]
                    if down_word == search_word:
                        find_count += 1
                        print(r,c, "Found Down")
                    if c - 3 >= 0:           
                        # Search Diagonally Down Left
                        ddl_word = complete_input[r][c] + complete_input[r + 1][c - 1] + complete_input[r + 2][c - 2] + complete_input[r + 3][c - 3]
                        if ddl_word == search_word:
                            find_count += 1
                            print(r,c, "Found DDL")
                    if c < row_length - 4:
                        # Search Diagonally Down Right
                        ddr_word = complete_input[r][c] + complete_input[r + 1][c + 1] + complete_input[r + 2][c + 2] + complete_input[r + 3][c + 3]
                        if ddr_word == search_word:
                            find_count += 1
                            print(r,c, "Found DDR")
    return find_count

def part_two(complete_input: list[list[str]]):
    find_count = 0
    search_letter = 'A'
    search_word = 'MAS'
    number_rows = len(complete_input)
    for r in range(number_rows):
        row_length = len(complete_input[r])
        for c in range(row_length):
            if complete_input[r][c] == search_letter:
                found_count = 0
                # Search Up
                if r >= 1 and r < number_rows - 1:
                    if c - 1 >= 0 :
                        # Search Diagonally Up Left To Down Right
                        dul_word = complete_input[r - 1][c - 1] + complete_input[r][c]  + complete_input[r + 1][c + 1]
                        if dul_word == search_word:
                            found_count += 1
                            if found_count == 2:
                                found_count = 0
                                find_count += 1
                            print(r,c, "Found Up Left Down Right")
                    if c < row_length - 1:
                        # Search Diagonally Up Right To Down left
                        dur_word = complete_input[r - 1][c + 1] + complete_input[r][c]  + complete_input[r + 1][c - 1]
                        if dur_word == search_word:
                            found_count += 1
                            if found_count == 2:
                                found_count = 0
                                find_count += 1
                            print(r,c, "Found Up Right Down Left")
                # Search Down
                if r < number_rows - 1:
                    if c - 1 >= 0:           
                        # Search Diagonally Down Left to up Right
                        ddl_word = complete_input[r + 1][c - 1] + complete_input[r][c] + complete_input[r - 1][c + 1]
                        if ddl_word == search_word:
                            found_count += 1
                            if found_count == 2:
                                found_count = 0
                                find_count += 1
                            print(r,c, "Found Down Left Up Right")
                    if c < row_length - 1:
                        # Search Diagonally Down Right to Up Left
                        ddr_word = complete_input[r + 1][c + 1] + complete_input[r][c] + complete_input[r - 1][c - 1]
                        if ddr_word == search_word:
                            found_count += 1
                            if found_count == 2:
                                found_count = 0
                                find_count += 1
                            print(r,c, "Found Down Right Up Left")
    return find_count

if __name__ == "__main__":
    file = open("day4_test.txt", "r")
    complete_input = []
    for r in file:
        complete_input.append([x.upper() for x in r])
    file.close()
    result = part_one(complete_input)
    print(result)
    result = part_two(complete_input)
    print(result)
