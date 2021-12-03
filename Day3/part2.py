#!/bin/python
import copy


def split(word):
    return [char for char in word]


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_file = [split(row.strip()) for row in file.readlines()]

        tmp = copy.deepcopy(input_file)
        bit = 0
        while len(tmp) > 1:
            total = len(tmp)
            ones = sum([1 for line in tmp if line[bit] == '1'])
            most_bit = 1 if ones > (
                total - ones) or ones == (total - ones) else 0
            tmp = [row for row in tmp if int(row[bit], base=2) == most_bit]
            bit += 1
        oxy = tmp

        tmp = copy.deepcopy(input_file)
        bit = 0
        while len(tmp) > 1:
            total = len(tmp)
            ones = sum([1 for line in tmp if line[bit] == '1'])
            most_bit = 1 if ones < (total - ones) else 0
            tmp = [row for row in tmp if int(row[bit], base=2) == most_bit]
            bit += 1

        co2 = tmp

        oxy = ''.join([str(value) for value in oxy[0]])
        co2 = ''.join([str(value) for value in co2[0]])

        print(int(oxy, base=2) * int(co2, base=2))
