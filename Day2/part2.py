
if __name__ == '__main__':
    horizontal = 0
    depth = 0
    aim = 0 
    with open('input.txt','r') as file:
        for row in file.readlines():
            row = row.strip().split()
            row[1] = int(row[1])

            if row[0] == 'forward':
                horizontal += row[1]
                if aim > 0:
                    depth += row[1] * aim

            if row[0] == 'down':
                aim += row[1]
            if row[0] == 'up':
                aim -= row[1]
    # print result
    print(depth*horizontal)