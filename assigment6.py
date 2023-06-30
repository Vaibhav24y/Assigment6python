def ds(roll_no,name):
    lst = [roll_no,name]
    tp = (roll_no,name)
    st = {roll_no,name}
    dict = {"roll no":roll_no,"name":name}
    print("list",lst)
    print("tuple",tp)
    print("set",st)
    print("dictionary",dict)
    roll = int(input("Enter roll no: "))
    name = input("Enter name: ")
    lst[0] = roll
    lst[1] = name
    tp = (roll,name)
    st = {roll,name}
    dict["roll no"]= roll
    dict["name"]=name
    del lst
    del tp
    del st
    del dict
roll = int(input("enter roll no.: "))
name = input("Enter name: ")
ds(roll,name)