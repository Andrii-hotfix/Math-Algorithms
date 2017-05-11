import random
import math
import ctypes as c
import os


'''
getPrime() returns probably prime 64-bit length number
'''
def getPrime():
    random.seed()
    prime = 0
    while not primeTest(prime, 100):
        odd = 0
        while odd % 2 == 0:
            prime = random.getrandbits(64)
            odd = int(str(prime)[-1])
    return prime


'''
primeTest() returns True if prime, otherwise - False
uses Miller-Rabin primality test
k - times repeat
'''
def primeTest(prime, k):
    # initial conditions
    if prime == 0:
        return False
    elif prime == 1:
        return True
    else:
        # get prime - 1 as (2^s)*t (t is odd)
        t = prime - 1
        s = 0
        while t % 2 == 0:
            t = int(t / 2)
            s += 1
        for i in range(0, k):
            a = random.randint(2, prime - 2)
            x = pow(a, t, prime)
            if x == 1 or x == prime - 1:
                continue
            else:
                for j in range(0, s - 1):
                    x = pow(x, 2, prime)
                    if x == 1:
                        return False
                    elif x == prime - 1:
                        break
                return False
        return True


'''
gcd(a,b) returns the greatest common divisor (a,b) and a list of quotients
uses Euqlid algorithm
'''
def gcd(a, b):
    q_list = []
    q = 0
    while b != 0:
        new_a = b
        q = math.floor(a / b)
        q_list.append(q)
        b = a % b
        a = new_a
    return a, q_list


'''
inverse(a,m) returns inverse element to a modulo m
'''
def inverse(a, m):
    gd, q_list = gcd(a, m)
    if gd == 1:
        p_list = [1, q_list[1]]
        i = 2
        for item in q_list[2:]:
            p_list.append(item * p_list[i - 1] + p_list[i - 2])
            i += 1
        return (((-1) ** (len(q_list[1:]) - 1)) * p_list[-2]) % m


'''
modPow(a,b,m) returns a^b mod m
uses Montgomery modular multiplication
'''
def modPow(a, b, m):
    b_iter = 1
    while b != 0:
        if b % 2 == 0:
            b = math.floor(b / 2)
            a = (a * a) % m
        else:
            b -= 1
            b_iter = (b_iter * a) % m
    return b_iter


'''
rsaKeys generates private & public keys tuples
'''
def rsaKeys():
    p = getPrime()
    q = getPrime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = getPrime()
    d = inverse(e, phi)
    private_key = (d, n)
    public_key = (e, n)
    return private_key, public_key


'''
rsaEncrypt(pub_e, n, str) encrypts string text with public key (pub_e,n)
'''
def rsaEncrypt(pub_e, n, text):
    txt_l = list(text)
    i = 0
    for item in txt_l:
        txt_l[i] = bin(ord(item))[2:]
        # padding for space
        if len(txt_l[i]) == 6:
            txt_l[i] = '0' + txt_l[i]
        i += 1
    txt_b = "".join(txt_l)
    words = []
    start = 0
    end = 63
    while end <= len(txt_b):
        words.append(txt_b[start:end])
        start = end
        end += 63
    words.append(txt_b[start:])
    i = 0
    for item in words:
        words[i] = pow(int(item, 2), pub_e, n)
        i += 1
    return words


'''
rsaDecrypt() decrypts list enc_txt with private key (priv_d,n)
'''
def rsaDecrypt(priv_d, n, enc_txt):
    i = 0
    for item in enc_txt:
        enc_txt[i] = pow(item, priv_d, n)
        i += 1
    i = 0
    for item in enc_txt:
        enc_txt[i] = bin(item)[2:]
        i += 1
    bin_str = ""
    for item in enc_txt:
        bin_str += item
    start = 0
    end = 7
    char_l = []
    while end <= len(bin_str):
        char_l.append(bin_str[start:end])
        start = end
        end += 7
    i = 0
    for item in char_l:
        char_l[i] = int(item, 2)
        i += 1
    i = 0
    for item in char_l:
        char_l[i] = chr(int(item))
        i += 1
    return "".join(char_l)

print("generating keys pair")
private, public = rsaKeys()
print("done!")
print("private key is: ", private)
print("public key is: ", public)
text = ""
while(True):
    text = input("enter string to encrypt ")
    if text == 'q':
        break
    encrypted = rsaEncrypt(public[0], public[1], text)
    print("encrypted message: ", encrypted)
    decrypted = rsaDecrypt(private[0], private[1], encrypted)
    print("decrypted message: ", decrypted)
