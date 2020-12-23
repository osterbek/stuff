import math

def relatively_prime(a, b):
    answer = True
    if a == b:
        answer =  False
    else:
        for i in range(2, min(a, b) + 1):
            if (a % i == 0) and (b % i == 0):
                answer = False
    return answer


def prime_factors(number):
    finding = []
    for i in range(2, number // 2 + 1):
        while number % i == 0:
            finding.append(i)
            number = number // i
    return finding


if __name__ == '__main__':
    # take two large prime numbers  p and q
    p = 13
    print('first prime p = ', p)
    q = 53
    print('second prime q = ', q)

    # form the product n = p * q, called module
    n = p * q
    print('module n = p * q = ', n)

    # select a number e which is smaller than n and coprime resp. relative prim to p-1 and q-1
    e = n
    while True:
        e -= 1
        if relatively_prime(e, p-1) and relatively_prime(e, p-1):
                break
    print('public exponent e = ', e, ' ... is relative prim to p-1 and q-1')

    # select a number d, so that (e*d)-1 is divisible by (p-1)*(q-1) without remainder
    d = 0
    while True:
        d += 1
        if ((e * d) - 1) % ((p - 1)*(q - 1)) == 0:
            break
    print('private exponent d = ', d, '... corresponds to constraint (e*d)-1 is divisible by (p-1)*(q-1) without remainder')

    # public key is the pair (n,e),
    public_key = [n, e]
    print('public key [n, e] = ', public_key)

    # private key is the pair (n,d).
    private_key = [n, d]
    print('private key [n, d] = ', private_key)

    # The encryption function is f(m) = c = (m powered e) mod n
    # c is the ciphertext and m is the message.
    m = 123
    print('message m =', m)
    cipher = (m ** e) % n
    print('cipher = (m ** e) % n =', cipher)

    # the decipherment function is g(c) = (c powered d) mod n
    decipher = (cipher ** d) % n
    print('decipher = (cipher ** d) % n =', decipher)
