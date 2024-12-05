import re
from functools import reduce
from pprint import pprint

def find_instructions(complete_input):
    instruction_regex = "mul\(\d+,\d+\)"
    regex = re.compile(instruction_regex)
    return regex.findall(complete_input)

def parse_instructions(instructions: list[str]):
    instruction_regex = '\d+,\d+'
    regex = re.compile(instruction_regex)
    csvs = regex.findall(" ".join(instructions))
    values = [ [ int(val) for val in x.split(",") ] for x in csvs]
    return values

def part_one(complete_input:str):
    complete_input = complete_input.strip().replace("\n", "")

    instructions = find_instructions(complete_input)
    results = parse_instructions(instructions)
    products = list(map(lambda lst: reduce(lambda x, y: x * y, lst), results))
    return sum(products)

def part_two(complete_input:str):
    complete_input = complete_input.strip().replace("\n", "")
    complete_input = complete_input.split("do()")
    complete_input = ([ x[ : x.find("don't()") if x.find("don't()") > 0 else len(x)] for x in complete_input])
    complete_input = (''.join(complete_input)).strip().replace("\n", "")
    instructions = find_instructions(complete_input)
    results = parse_instructions(instructions)
    products = list(map(lambda lst: reduce(lambda x, y: x * y, lst), results))
    return sum(products)

if __name__ == "__main__":
    file = open("day3.txt", "r")
    complete_input = ""
    for r in file:
        complete_input += r
    file.close()
    result = part_one(complete_input)
    print(result)
    result = part_two(complete_input)
    print(result)