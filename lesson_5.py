#1
import math
def find_min_angle_point(X, Y, Z):
    def angle_to_x(point):
        x, y = point
        if x == 0:
            return math.inf
        return abs(y / x)
    points = [X, Y, Z]
    angles = [angle_to_x(p) for p in points]
    min_angle_idx = angles.index(min(angles))
    return points[min_angle_idx]
X = (3, 4)
Y = (-1, 2)
Z = (0, 5)
min_point = find_min_angle_point(X, Y, Z)
print(f"Координаты точки с минимальным углом: {min_point}")

#2
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def is_palindrome(s):
    return s == s[::-1]
def palindromic_primes(n):
    result = []
    for number in range(2, n+1):
        binary_representation = bin(number)[2:]
        if is_prime(number) and is_palindrome(binary_representation):
            result.append((number, binary_representation))
    return result
n = 50
palindromes = palindromic_primes(n)
for num, binary in palindromes:
    print(f"{num} (binary: {binary})")