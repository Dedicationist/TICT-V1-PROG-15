lst=[4, 0, 1, -2]
def swap(lst):
    if len(lst) >= 2:
        lst[0], lst[1] = lst(1), lst[0]
        return(lst)

res = swap(lst)
print(res)

