# Write your solution here
n = int(input("Layers: "))
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

left = ""
right = ""

k = n-1
m = 2 * n - 1

while k >= 1:
    left += alphabet[k]
    right = alphabet[k] + right
    m -= 2
    print(left + alphabet[k] * m + right)
    k -= 1

while k <= n-1: 
    print(left + alphabet[k] * m + right)
    left = left[:-1]
    right = right[1:]
    m += 2
    k += 1