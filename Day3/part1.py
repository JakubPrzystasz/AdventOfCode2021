#!/bin/python

def split(word):
    return [char for char in word]

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_file = [split(row.strip()) for row in file.readlines()]
        gamma_rate = ''
        epsilon_rate = ''
        total_num = len(input_file)
        counter = [0] * len(input_file[0])

        for row in input_file:
            for bit_idx, bit in enumerate(row):
                counter[bit_idx] += int(bit)
        
        for value in counter:
            diff = total_num - value
            most_common_bit = 1 if value > diff else 0
            gamma_rate += '0' if most_common_bit == 0 else '1'
            epsilon_rate += '1' if most_common_bit == 0 else '0'

        print(int(gamma_rate,base=2) * int(epsilon_rate,base=2))
