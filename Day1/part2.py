if __name__ == '__main__':
    with open('input.txt') as f:
        last = -1
        count = 0
        current = 0
        rows = f.readlines()
        for i in range(0,len(rows)):
            try:
                current = int(rows[i]) + int(rows[i+1]) + int(rows[i+2])
            except Exception:
                break
            if last > -1 and (current > last):
                 count = count + 1
            last = current
        print(count)
        