
def output_html(content):
    output = '<pre class="tab">\n'
    for line in content:
        output += line + '\n'
    output += '</pre>\n'
    return output


def relatively_prime(a, b):
    answer = True
    if a == b:
        answer = False
    else:
        for i in range(2, min(a, b) + 1):
            if (a % i == 0) and (b % i == 0):
                answer = False
    return answer


def rsa(p, q, m):
    output = []
    # take two large prime numbers  p and q
    # p = 13
    output.append('first prime p = ' + str(p))
    # q = 53
    output.append('second prime q = ' + str(q))

    # form the product n = p * q, called module
    n = p * q
    output.append('module n = p * q = ' + str(n))

    # select a number e which is smaller than n and coprime resp. relative prim to p-1 and q-1
    e = n
    while True:
        e -= 1
        if relatively_prime(e, p-1) and relatively_prime(e, p-1):
                break
    output.append('public exponent e = ' + str(e) + ' ... is relative prim to p-1 and q-1')

    # select a number d, so that (e*d)-1 is divisible by (p-1)*(q-1) without remainder
    d = 0
    while True:
        d += 1
        if ((e * d) - 1) % ((p - 1)*(q - 1)) == 0:
            break
    output.append('private exponent d = ' + str(d) + ' ... corresponds to constraint (e*d)-1 is divisible by (p-1)*(q-1) without remainder')

    # public key is the pair (n,e),
    public_key = [n, e]
    output.append('public key [n, e] = ' + str(public_key))

    # private key is the pair (n,d).
    private_key = [n, d]
    output.append('private key [n, d] = ' + str(private_key))

    # The encryption function is f(m) = c = (m powered e) mod n
    # c is the ciphertext and m is the message.
    # m = 123
    output.append('message m = ' + str(m))
    cipher = (m ** e) % n
    output.append('cipher = (m ** e) % n = ' + str(cipher))

    # the decipherment function is g(c) = (c powered d) mod n
    decipher = (cipher ** d) % n
    output.append('decipher = (cipher ** d) % n = ' + str(decipher))
    return output_html(output)


def http_entry(request):
    request_args = request.args
    p, q, m = 13, 53, 123
    if request_args:
        if 'p' in request_args:
            p = request_args['p']
        if 'q' in request_args:
            q = request_args['q']
        if 'm' in request_args:
            m = request_args['m']
    return rsa(int(p), int(q), int(m))


def local_entry():
    p, q, m = 13, 53, 123
    return rsa(p, q, m)


if __name__ == '__main__':
    print(local_entry())
