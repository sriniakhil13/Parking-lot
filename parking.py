import os

import unicodedata
def initalize(slot,a=0):


    print("done")
    for i in range(0,a):
        slot.append(' ')

    return slot


def entry(slot,str,color,dict):
    """

    :rtype:
    """
    flag=0
    for k in dict.keys():
        flag=0
        if dict[k][0]==' ' :
            print("car added to slot")
            # unicodedata.normalize('NFKD', str).encode('ascii', 'ignore')
            # unicodedata.normalize('NFKD', color).encode('ascii', 'ignore')

            o=[str,color]
            dict[k]=o
            flag=1
            break

    if flag==0:
        return 'Parking Full'
    return dict

def leave(slot,str,dict):

    for k in dict.keys():
        list=dict[k]
        if list[0]==str:
            dict[k][0]=" "
            dict[k][1]=" "

    print("slot freed!")




def get_cars_with_color(col,dict1):
    ans=dict()

    for k in dict1.keys():

        if dict1[k][1]==col:
            ans[k]=dict1[k]

    return  ans

def get_slot_with_number(str,dict1):
    ans2=dict()
    for k in dict1.keys():

        if dict1[k][0]==str:
            ans2[k]=dict1[k]
    return ans2

def get_all():
    print(dict)




# initalize()
#
# print(slot)
# print("")
# while 1:
#     print("press 1 for entry 2 for leave 3 for cars with colour 4 for get slot no of car 5 for get all 6 for exit")
#     a=int(raw_input())
#     if a==6:
#         break
#     if a== 1:
#         c = (raw_input("enter car no "))
#         d = raw_input("color ")
#         entry(d, c)
#     if a==2:
#         c = (raw_input("enter car no "))
#         leave(c)
#     if a==3:
#         c = (raw_input("enter car color "))
#         print(get_cars_with_color(c))
#     if a==4:
#         c = (raw_input("enter car no "))
#         print(get_slot_with_number(c))
#     if a==5:
#         get_all()
#
#





