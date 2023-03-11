# listaloca = [1,2,3,4]
# print(str(listaloca[1:]))
def sumaRecur(arr):
    if arr == []:
        return 0
    return arr[0] + sumaRecur(arr[1:])

print(sumaRecur([1,2,3]))
