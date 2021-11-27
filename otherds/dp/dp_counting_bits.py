"""
Caching approach here

from numbers till 2^16, we build a cache where number --> count of 1.

for numbers above than that, we divide the number into 16 bits of peices.

for a 16 bit number, we already have calculated number of 1s.
so we fetch from there and shift the number by 16 more bits to right.

So we do it in O(n) time.

"""

def count(x):
    c = 0
    while x:
        if x & 1:
            c = c + 1
        x = x >> 1
    return c


def dp_count_bit(nums):
    """

    """
    max_val = 1 << 16  # power of pow(2, 16)

    number_bits_hash = {}
    for i in range(max_val):
        number_bits_hash[i] = count(i)

    mask = int('0xffff', 16)
    answer = []
    for i in range(nums + 1):
        if i in number_bits_hash:
            answer.append(number_bits_hash[i])
        else:
            n = i
            c = 0
            while n:
                last_16_bit = n & mask
                c = c + number_bits_hash[last_16_bit]
                n = n >> 16
            if i == 524288:
                print(c)
            answer.append(c)

    return answer


# nums = 1 << 20
# nums = 2
nums = 1 << 19
dp_count_bit(nums)

