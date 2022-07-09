#Challan Management System
class Challan:
    def __init__(self,veh_no,veh_name,owner_name,owner_phone,challan):
        self.veh_no=veh_no
        self.veh_name=veh_name
        self.owner_name=owner_name
        self.owner_phone=owner_phone
        self.challan=challan
    def enter(self,veh_no,veh_name,owner_name,owner_phone,challan):
        sandeep=Challan(veh_no,veh_name,owner_name,owner_phone,challan)
        list1.append(sandeep)
        print("details entered")
    def display(self,sandeep):
        print("the details are.....")
        print("Vehicle Number:",sandeep.veh_no)
        
        print("Vehicle Name:",sandeep.veh_name)
        print("Owner Name:",sandeep.owner_name)
        print("Owner Contact Number:",sandeep.owner_phone)
        print("Total Challan:",sandeep.challan)
    def delete(self,y):
        del list1[y-1]
        print("details are deleted")
    def update(self,no,veh_no_new):
        id=veh_no_new
        list1[no-1]=id
        print("details are updated....")
        
list1=[]
v=Challan('','','','','')
while(1):
    print(""" 1.enter  2.display  3.update  4.delete  5.exit""")
    print("enter the choice plz")
    x=int(input())
    if(x==1):
        print("please enter the details")
        veh_no=input("Vehicle Number:")
        veh_name=input("Vehicle Name:")
        owner_name=input("Owner Name:")
        owner_phone=input("Owner Contact Number:")
        challan=input("Total Challan:")
        v.enter(veh_no,veh_name,owner_name,owner_phone,challan)
    elif(x==2):
        for i in range(len(list1)):
            v.display(list1[i])
    elif(x==3):
        a=int(input("enter the owner number:"))
        b=input("enter new veh number:")
        v.update(a,b)
    elif(x==4):
        z=int(input())
        v.delete(z)
    else:
        exit()