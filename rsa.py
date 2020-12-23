def relatively_prime(a, b):
    answer = True
    if a == b:
        answer =  False
    else:
        for i in range(2, min(a, b) + 1):
            if (a % i == 0) and (b % i == 0):
                answer = False
    return answer


if __name__ == '__main__':

    # Man nehme zwei große Primzahlen p und q
    p = 5
    q = 17

    # Man bilde deren Produkt n=p*q, welches Modul genannt wird
    n = p * q

    # Man wähle eine Zahl e die kleiner als n und teilerfremd (relativ prim) zu p-1 und q-1 ist
    e = 1
    while True:
        e += 1
        if relatively_prime(e, p-1) and relatively_prime(e, p-1):
                break

    # Finde eine Zahl d, so dass (e*d)-1 durch (p-1)*(q-1) ohne Rest teilbar ist
    d = 0
    while True:
        d += 1
        if ((e * d) - 1) % ((p - 1)*(q - 1)) == 0:
            break

    # Der öffentliche Schlüssel ist das Paar (n,e),
    public_key = [n, e]

    # der private Schlüssel ist das Paar (n,d).
    private_key = [n, d]

    # Die Verschlüsselungsfunktion lautet f(m) = c = (m hoch e) mod n
    # wobei c der Chiffretext und m die Nachricht ist.
    m = 10
    cipher = (m ** e) % n

    # Die Entschlüsslungsfunktion lautet: g(c) = (c hoch d) mod n
    decipher = (cipher ** d) % n



    print('first prime p = ', p)
    print('second prime q = ', q)
    print('module n = ', n)
    print('public exponent e = ', e)
    print('private exponent d = ', d)
    print('public key [n, e] = ', public_key)
    print('private key [n, d] = ', private_key)
    print('message m =', m)
    print('cipher =', cipher)
    print('decipher =', decipher)



