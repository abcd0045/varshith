list = []
def inset(name, reg):
    list.append(name)
    list.append(reg)
    print("record added successful")
def remove(register):
    if list == []:
        print("empty record")
    else:
        for i in range(len(list)):
            if i in list[i]:
                if i == register.item.list.pop():
                    print('item removed successfully')
def calculate_marks(register):
    for j in range(len(list)):
        if j == register:
            m1 = int(input("enter the marks of python:"))
            m2 = int(input('enter the marks of cn:'))
            m3 = int(input("enter the marks of dbms:"))
            avg = (m1 + m2 + m3) // 3
        if avg<=100 and avg>80:
            print("distinction")
        elif avg<79 and avg>50:
            print("first class")
        elif avg<35 and avg>40:
            print("fail")
def search(register):
    if list==[]:
        print("empty record")
    else:
        for i in range(len(list)):
            for j in list[i]:
                if j == register:
                    print('record found')
                    break
                else:
                    print("record not found")
def display():
    if list == []:
        print("empty record")
    else:
        for i in list:
            print(i)
    print('''/n student data management
    1.insert
    2.remove
    3.calculate result
    4.search
    5.display
    6.exit''')
ch = int(input("enter your choise:"))
if ch == 1:
    name = input("enter the nam of the student:")
    reg = int(input("enter the register number:"))
    insert (name, reg)
elif ch==2:
    remove()
elif ch==3:
    register=int(input("enter the register number to search:"))
    calculate_marks(register)
elif ch==4:
    register = int(input("enter the register number to search:"))
    search(register)
elif ch==5:
    display()
elif ch==6:
    breakpoint()
else:
    print("enter valid choice")