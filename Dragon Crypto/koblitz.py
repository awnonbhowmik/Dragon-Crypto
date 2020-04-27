import math
from random import randint
#import matplotlib.pyplot as plt


def sq_root_mod_n(n, p):
    n = n % p
    for x in range(2, p):
        if ((x*x) % p == n):
            return x
    return 0


def koblitz_encoder(plainText, elliptic_a, elliptic_b):
    ord_lst = [ord(ch) for ch in plainText]
    k = 20
    p = 751

    x_coords = []
    y_coords = []
    encoded_points = []

    for m in ord_lst:
        for j in range(1, k):
            x_m = m*k+j
            n = pow(x_m, 3) + elliptic_a * x_m + elliptic_b
            y_m = sq_root_mod_n(n, p)
            if (y_m != 0):
                x_coords.append(x_m)
                y_coords.append(y_m)
                encoded_points.append((x_m, y_m))
                break

    encoded = []
    for i in range(len(x_coords)):
        encoded.append((x_coords[i], y_coords[i]))
        #print('{},{}'.format(x_coords[i], y_coords[i]))
    return encoded


def koblitz_decoder(encoded_points):
    decoded_Msg = []
    k = 20
    for x, y in encoded_points:
        d = math.floor((x-1)/k)
        decoded_Msg.append(chr(d))

    # print(''.join(decoded_Msg))
    return ''.join(decoded_Msg)

# plt.plot(x_coords,y_coords,'s')
# plt.show()


def pyth(x, y):
    return x**2+y**2


decoded_points = []


def primitive_start_point(N):
    for i in range(-math.ceil(math.sqrt(N)), math.ceil(math.sqrt(N))):
        for j in range(-math.ceil(math.sqrt(N)), math.ceil(math.sqrt(N))):
            if i**2+j**2 == N:
                decoded_points.append([j, i])

    return decoded_points


"""
def dec_ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return nums[::-1]

print(dec_ternary(11))

def ternary_dec(t):
    n = 0
    t = t[::-1]
    for i in range(len(t)):
        n += (3**i)*t[i]
    return n

print(ternary_dec([1,0,2]))

for i in range(len(encoded_points)):
    x = x_coords[i]
    y = y_coords[i]
    print(dec_ternary(pyth(x,y)))
"""

if __name__ == "__main__":
    plainText = input("Enter Message: ")

    print('Curve Parameters')
    elliptic_a = int(input("Enter A: "))
    elliptic_b = int(input("Enter B: "))

    encrypt = koblitz_encoder(plainText, elliptic_a, elliptic_b)

    print("Encrypted points: ", encrypt)

    decrypt = koblitz_decoder(encrypt)
    #decrypt = koblitz_decoder([(1856,292)])

    print("Decrypted message: ", decrypt)
