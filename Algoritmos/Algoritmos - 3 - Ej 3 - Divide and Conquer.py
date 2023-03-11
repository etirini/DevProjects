#Find the biggest number recursively

def max(list):
    if len(list) == 2:
       return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(str(max([46,20,2,32,45,2,3,7,8,5])))



