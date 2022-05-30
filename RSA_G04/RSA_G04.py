# pip install pycryptodome
from Crypto.Util.number import inverse
import math

def getModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
class RSA:
    def __init__(self, n, e, d):
        self.n = n
        self.e = e
        self.d = d
        pass

    def encrypt_int(self, m):
        c = pow(m, self.e, self.n)
        return c

    def decrypt_int(self, c):
        m = pow(c, self.d, self.n)
        return m

    def encrypt_text(self, m_plaintext):
        m_ciphertext = [pow(ord(c), self.e, self.n) for c in m_plaintext]
        return m_ciphertext #list

    def decrypt_text(self, m_ciphertext):
        m_plaintext = [chr(pow(c, self.d, self.n)) for c in m_ciphertext]
        return (''.join(m_plaintext))
        # return m_plaintext


def menu():
    print("********************")
    print("1. Mã hóa số nguyên.")
    print("2. Mã hóa đoạn text.")
    print("********************")
    k = int (input("Moi lua chon: "))
    return k

def main():
    k = menu()
    print("Bat dau sinh khoa... ")
    # p = 752708788837165590355094155871
    # q = 986369682585281993933185289261
    p =13
    q= 31
    n = p * q
    phi = (p - 1) * (q - 1)
    print("p: " + str(p))
    print("q: " + str(q))
    print("n: " + str(n))
    print("phi:" + str(phi))
    # Tao Public_Key
    e = int(input("Nhap e thoa man 0 < e < phi: "))
    while (True):
        if (e > phi or e < 1 or math.gcd(e,phi) != 1):
            e = int(input("Nhap lai e: "))
        else:
            break
    # Tinh Private_Key
    d = inverse(e,phi)
    # d = getModInverse(e, phi)
    print("d:  " + str(d))

    rsa = RSA(n,e,d)
    if (k==1):
        m = int(input("Nhap so nguyen m (m<n): "))
        c = rsa.encrypt_int(m)
        print(f"Ban ma {c}")
        print(f"Ban ro: {rsa.decrypt_int(c)}")
    else:
        m = input("Nhap doan text m: ")
        c = rsa.encrypt_text(m)
        print("Ban ma: " + ''.join(map(lambda x: str(x), c)))
        print(f"Ban ro: {rsa.decrypt_text(c)}")

if __name__ == "__main__":
    main()
