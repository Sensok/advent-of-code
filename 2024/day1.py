
def part_one(left_list, right_list):
    distance = 0
    for i in range(len(left_list)):
        distance += abs(left_list[i] - right_list[i])

    print(distance)

def part_two(left_list, right_list):
    similarity_score = 0
    for n in left_list:
        # number * number of times in right list
        number = n * right_list.count(n)
        # Add number to similarity score
        similarity_score += number

    print(similarity_score)

if __name__ == "__main__":
    left_list = []
    right_list = []
    file = open("day1.txt", "r")
    for r in file:
        ll, rl = r.replace("   ", ",").split(",")
        left_list.append(int(ll))
        right_list.append(int(rl))
    left_list.sort()
    right_list.sort()
    file.close()
    part_one(left_list, right_list)
    part_two(left_list, right_list)
