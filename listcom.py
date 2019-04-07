my_list = [1,2,3,4,5,6,7,8,9]
square = [num * num for num in my_list]
print(square)




def Reverse(lst):
    return [ele for ele in reversed(lst)]
print(Reverse(my_list))





def ReverseMore(lst):
    lst.reverse()
    return lst
print(ReverseMore(my_list))
