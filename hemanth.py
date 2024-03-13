class employee:
    def __init__(self):
        self.items=[]
    def insert(self):
        n=int(input("enter the numberof records"))
        for i in range(n):
            ename=input("employee name:")
            eid=int(input("employee id:"))
            salary=float(input("employee salary:"))


    def delete(self):
        eid=int(input("enter employee ID to delete"))
        for row in self.items:
            for i in row:
                print(i)
    def display(self):
        for i in self.items:
            print(i)
s=employee()
s.insert()
s.display()
s.delete()
s.display()