import re


valid_digits = {"oneight":"18","sevenine": "79","threeight": "38", "eightwo":"82","eighthree": "83", "twone": "21", "nineight": "98","fiveight": "58","one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}

def part_one():
    with open('input.txt', 'r') as f:
        numbers = [[c for c in l if c.isnumeric()]for l in f]
        numbers = [int(f'{l[0]}{l[-1]}') if len(l) > 1 else int(f'{l[0]}{l[0]}') for l in numbers]
        print(sum(numbers))

def part_two(filename):
    with open(filename, 'r') as f:
        numbers = [get_numbers_from_line(l)for l in f]
        print(sum(numbers))

def get_numbers_from_line(line):
    line_ret = ""
    for key, value in valid_digits.items():
        line = re.sub(key, value, line)

    for c in line:
        if c.isnumeric():
            line_ret += c
    line_ret = int(f'{line_ret[0]}{line_ret[-1]}') if len(line_ret) > 1 else int(f'{line_ret[0]}{line_ret[0]}')
    return line_ret

if __name__ == "__main__":
    part_one('input.txt')
    part_two('input.txt')
    # part_two('smaller_test.txt')
    