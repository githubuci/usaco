# -1 3

# 1 3 -2 -7 5
# 1 x decrease 5
# 0 1 -5 -11 0
# 1 x decrease 4
#   0 -7 -14 -4
# 7 x increase 3
#     0 0 17
#

def balance(arr):
    if not arr:
        return 0

    for i in range(1, len(arr)):
        arr[i] += -arr[0] * (i + 1)

    return abs(arr[0]) + balance(arr[1:])


# arr = [-1, 3]
arr = [1, 3, -2, -7, 5]
print(balance(arr))
