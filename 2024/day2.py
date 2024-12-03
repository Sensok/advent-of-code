
def part_one(row):
    len_row = len(row)
    is_increasing = False
    for idx, number in enumerate(row):
        if idx < len_row - 1:
            current_diff_value = (int(number) - int(row[idx + 1]))
            current_is_increasing = current_diff_value < 0
            if idx == 0:
                is_increasing = current_is_increasing
            elif current_is_increasing != is_increasing:
                return False
            if current_diff_value == 0:
                return False
            if abs(current_diff_value) > 3:
                return False
    return True

if __name__ == "__main__":
    file = open("day2.txt", "r")
    safe_count = 0
    for r in file:
        r = r.strip().split(" ")
        is_safe = part_one(r)
        if is_safe:
            safe_count += 1
        else:
            row = r.copy()
            count = len(r)
            for i in range(count):
                row = r.copy()
                row.pop(i)
                is_safe = part_one(row)
                if is_safe:
                    safe_count += 1
                    break
                
    print(safe_count)
    file.close()