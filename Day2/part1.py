
if __name__ == '__main__':
    horizontal = 0
    vertical = 0
    with open('input.txt','r') as file:
        for row in file.readlines():
            row = row.strip().split(' ')
            row[1] = int(row[1])

            if row[0] == 'forward':
                horizontal += row[1]
            if row[0] == 'down':
                vertical += row[1]
            if row[0] == 'up':
                vertical -= row[1]
    print(vertical*horizontal)