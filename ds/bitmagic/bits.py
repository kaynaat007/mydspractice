from datetime import datetime


def measure_time(input_function):

    def inner(*args, **kwargs):
        t = datetime.now()
        x = input_function(*args, **kwargs)
        print('took %.5f mili seconds'%((datetime.now() - t).total_seconds() * 1000))
        return x
    return inner


class Parity:
    """
    Parity of a number.
    """

    @staticmethod
    @measure_time
    def parity(x):
        """
        O(n)
        desc: counts one in bit representation of  x. O(n) time
        """
        c = 0
        while x:
            if x & 1:
                c += 1
            x = x >> 1
        return c % 2

    @staticmethod
    @measure_time
    def parity_1(x):
        """
        O(number of set bits).
        desc: use x & (x - 1) to set last set bit to zero.
        """
        c = 0
        while x:
            x = x&(x-1)
            c += 1
        return c % 2

    def prepare_cache(self, L):
        """
        prepare cache.
        """
        cache = {}
        for i in range(2 << L):
            cache[i] = self.parity_1(i)
        return cache

    @staticmethod
    @measure_time
    def parity_2(x, cache, L):
        """
        O(N/L): in a number x of N bits, L is size by which you divide N equally.
        desc: use caching strategy. if N=8 bits, use 2 bits cache. pre compute parity of all numbers possible of 2 bits
        and use it to calculate parity of N bits.
        parity(N) = parity(first L bits) ^ parity(next L bits) ^ parity( next L bits ) ... N/L times.
        """
        par = 0
        mask = 15  # number having last 4 bits as 1. we want to extract last 4 bits each time.
        while x:
            index = x & mask
            par = par ^ cache[index]
            x = x >> L
        return par

    @staticmethod
    @measure_time
    def generate_number(bit):
        """
        generate number
        """
        x = 1 << bit
        x = x | 2
        x = x | 4
        return x


    @staticmethod
    @measure_time
    def parity_3(x):
        """
        assuming x is of 64 bits
        """
        assert x.bit_length() == 64, 'must be 64 bits'
        x = x ^ (x >> 32)
        x = x ^(x >> 16)
        x = x ^(x >> 8)
        x = x ^(x >> 4)
        x = x ^(x >> 2)
        x = x ^ (x >> 1)
        return x & 1


class Swap:
    """
    Swaps the ith and jth bit in x.
    """

    @staticmethod
    @measure_time
    def swap_1(x, i, j):
        """
        O(1)
        desc: swap is only necessary when ith and jth bits are different. XOR of any bit with a 1, flips the bit.
        """
        if (x >> i & 1) != (x >> j & 1):
            mask = 1 << i | 1 << j
            return x ^ mask
        return x


class Reverse:
    """
    Reverses bits in x
    """

    @staticmethod
    @measure_time
    def reverse_brute_force(x):
        """
        O(n/2)
        desc : traverse from right to left, swap ith bit with n-i-1th bit till num_bits/2.
        """
        y = x.bit_length()
        print ("bit length: {0}".format(y))
        i = 0
        while i < y/2:
            x = Swap.swap_1(x, i, y-i-1)
            i += 1
        return x


def multiply(x, y):
    """

    """
    print ('multiplying: {0}, {1}'.format(x, y))
    i = 0
    result = 0
    while x:
        if x & 1:
            result = sum_binary(result, y << i)
            # result += (y << i)
        i =  i + 1
        x = x >> 1
    return result


def sum_binary(x_, y_):
    """
    do bitwise thinking.
    adding 1 bit to 1 bit.
    """

    x = x_
    y = y_
    r = 0
    i = 0
    c = 0
    if x == 0:
        return y
    if y == 0:
        return x

    while x or y:
        a = x & 1
        b = y & 1
        if c == 0:
            bit_result = a ^ b
        else:
            bit_result = a ^ b ^ c
        if (a == 1 and b == 1) or ( a == 1 and c == 1) or ( b == 1 and c == 1):
            c = 1
        else:
            c = 0
        x = x >> 1
        y = y >> 1
        if bit_result == 1:
            r = r | 1 << i
        i = i + 1
    if c == 1:
        r = r | 1 << i
    print ("sum of {0} and {1} is {2}".format(x_, y_, r))
    return r


def sum_binary_v2(x, y):
    """

    """
    result = 0
    i = 0
    carry = 0

    while x or y:
        bit_x = x & 1
        bit_y = y & 1
        output = bit_x ^ bit_y ^ carry
        if output == 1:
            result = result | 1 << i
        i = i + 1
        if (bit_x & bit_y & carry) or (bit_x & bit_y) or  (bit_x & carry) or (bit_y & carry):
            carry = 1
        else:
            carry = 0
        x = x >> 1
        y = y >> 1
    if carry == 1:
        result = result | 1 << i
    print("result: {0}".format(result))
    return result




def qutoint(x, y):
    """

    """
    k = 0
    q = 0

    while (y << k) <= x:
        k = k + 1

    k = k - 1
    x = x - (y << k)
    q += (1 << k)

    print ('initial k: {0}'.format(k))
    print ("x: {0}, y: {1}, q: {2}".format(x, y, q))

    k = k - 1
    print ("k1: {0}".format(k))

    while k >= 0:

        if (y << k) <= x:
            break
        k = k - 1

    if k >= 0:
        q = q + (1 << (k))

    return q


def extract_bit(x, i):
    """

    """
    if x < 0:
        return 0
    if i <= 0:
        return 0
    return (x >> (i-1)) & 1


def find_max_k(x, y):
    """
    find max k such that y << k >= x
    """
    k = 0
    while (y << k) <= x:
        k = k + 1
    return k-1


def divide(x, y):
    """
    divide x and y.
    """
    if x < y:
        return 0
    k_max = find_max_k(x, y)
    quo = 1 << k_max
    x = x - (y << k_max)
    k = k_max - 1
    while k >= 0:
        if (y << k) <= x:
            x = x - y << k
            quo = quo + 1 << k
        k -= 1
    return quo


def exp(x, y):

    result = 1.0
    power = y
    import pdb
    pdb.set_trace()
    while power:
        if power & 1:
            result = result * x
        x = x * x
        power = power >> 1
    return result


if __name__ == '__main__':
    """
    """
    x = 5
    # print(Swap.swap_1(x, 0, 1))
    # print(Reverse.reverse_brute_force(12))n

    # print(multiply(13, 9))
    # print (qutoint(27, 5))
    # print(sum_binary(1000, 2000))
    # bits = []
    # for i in range(1, 16):
    #     bits.append(str((extract_bit(12, i))))
    # b = ""
    # while bits:n
    #     b += bits.pop()
    # print (b)

    # print(sum_binary_v2(89, 11))

    # print(divide(20, 500))
    print(exp(2, 4))

