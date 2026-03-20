# def sum_all(*args):
#   # print(args)
#   return sum(args)


# print(sum_all(1,2,3))
# print(sum_all(1,2,3,5,6))
# print(sum_all(1,2,3,6,2,5,7))


def sum_numbers(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sum_numbers(2, 3)) 
