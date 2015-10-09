#! /usr/bin/python
# coding:utf-8

def main():
    prime_digit = 10
    max_num = 10 ** (prime_digit) - 1
    primes = make_primes(max_num)

    with open('20-pi.txt', 'r') as fi:
        pi = fi.readline()

    for i in xrange(len(pi) - prime_digit + 1):
        num = int(pi[i:i + prime_digit])
        if check_prime(num, primes):
            print 'FLAG_Q20_' + str(num)
            break


def make_primes(max_num):
    prime_max = int(max_num**0.5)
    numlist = [2] + [i for i in xrange(3, prime_max + 1, 2)]
    i = 1

    while i < len(numlist):
        for p in numlist[:i]:
            if p**2 > numlist[i]:
                i += 1
                break
            if numlist[i] % p == 0:
                del(numlist[i])
                break
    return numlist


def check_prime(num, primes):
    for p in primes:
        if p**2 > num:
            return True
        if num % p == 0:
            return False
    return True


if __name__ == '__main__':
    main()
