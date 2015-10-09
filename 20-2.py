#! /usr/bin/python
# coding:utf-8

def main():
    prime_digit = 10
    max_num = 10 ** (prime_digit) - 1
    primes = make_primes(max_num)

    with open('pi.txt', 'r') as fi:
        pi = fi.readline()

    for i in xrange(len(pi) - prime_digit + 1):
        num = int(pi[i:i + prime_digit])
        if check_prime(num, primes):
            print 'FLAG_Q20_' + str(num)
            break


def make_primes(max_num):
    prime_max = int(float(max_num)**0.5)
    nums = {2 : True}
    nums.update({i : True for i in xrange(3, prime_max + 1, 2)})
    i = 1
    for num in sorted(nums):
        if num in nums:
            continue
        mulmax = max_num/num
        for mulnum in (num * m for m in xrange(3, mulmax, 2)):
            if num in nums:
                del(nums[mulnum])

    return [num for num in nums.keys()]


def check_prime(num, primes):
    for p in primes:
        if p**2 > num:
            return True
        if num % p == 0:
            return False
    return True


if __name__ == '__main__':
    main()
