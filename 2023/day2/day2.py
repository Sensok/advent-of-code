import re


valid_digits = {"oneight":"18","sevenine": "79","threeight": "38", "eightwo":"82","eighthree": "83", "twone": "21", "nineight": "98","fiveight": "58","one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
valid_letters_for_digits = set(''.join(valid_digits.keys()))

def read_line_into_array(line: str, red_cubes, green_cubes, blue_cubes):
    # ['Game 1' ,  '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']
    first_split = line.split(':')
    game_id = first_split[0]
    _, id = game_id.split(' ')
    # ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']
    game_sets_list = first_split[1].strip().split(';')
    is_valid = True
    for individual_sets in game_sets_list:
        # ['3 blue', '4 red']
        if is_valid:
            num_color_cubes = individual_sets.split(',')
            for num_color in num_color_cubes:
                num, color = num_color.strip().split(' ')
                num = int(num)
                if not is_valid:
                    break;
                if color == 'blue':
                    is_valid = num <= blue_cubes
                elif color == 'green':
                    is_valid = num <= green_cubes
                elif color == 'red':
                    is_valid = num <= red_cubes
        else: 
            break
    return int(id), is_valid

def get_power(line: str,):
    red_cubes = 0
    green_cubes = 0
    blue_cubes = 0
    # ['Game 1' ,  '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']
    first_split = line.split(':')
    game_id = first_split[0]
    _, id = game_id.split(' ')
    # ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']
    game_sets_list = first_split[1].strip().split(';')
    for individual_sets in game_sets_list:
        # ['3 blue', '4 red']
        num_color_cubes = individual_sets.split(',')
        for num_color in num_color_cubes:
            num, color = num_color.strip().split(' ')
            num = int(num)
            if color == 'blue':
                if num >= blue_cubes:
                    blue_cubes = num
            elif color == 'green':
                if num >= green_cubes:
                    green_cubes = num
            elif color == 'red':
                if num >= red_cubes:
                    red_cubes = num

    return red_cubes * blue_cubes * green_cubes
def part_one(red_cubes, green_cubes, blue_cubes):
    id_sum = 0
    num_invalid = 0
    with open('input.txt', 'r') as f:
        for line in f:
            id, is_valid = read_line_into_array(line, red_cubes= red_cubes, green_cubes=green_cubes, blue_cubes=blue_cubes)
            if is_valid:
                id_sum += id
            else: 
                num_invalid += 1
    print(id_sum, num_invalid)

def part_two():
    id_sum = 0
    with open('input.txt', 'r') as f:
        for line in f:
            power = get_power(line)
            id_sum += power
    print(id_sum)
    
if __name__ == "__main__":
    part_one(red_cubes=12, green_cubes=13, blue_cubes=14)
    part_two()
    