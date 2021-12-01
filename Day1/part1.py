if __name__ == '__main__':
    with open('input.txt') as f:
        last = -1
        count = 0
        for row in f.readlines():
            if last > -1 and (int(row) > last):
                count = count + 1
            last = int(row)
        print(count)
