from Validation import *
class employee:
    empdict = {}
    def __init__(self,e_i,e_n,e_m,e_s,e_a,e_g,e_add,e_c,e_dob,e_doj,e_dn,e_d,e_pn,e_an):
        self.empid=e_i
        self.empname=e_n
        self.empmobile=e_m
        self.salary=e_s
        self.age=e_a
        self.gender=e_g
        self.address=e_add
        self.city=e_c
        self.dob=e_dob
        self.doj=e_doj
        self.deptname=e_dn
        self.designation=e_d
        self.pn=e_pn
        self.an=e_an
        if self.deptname in self.empdict.keys():
            self.empdict[self.deptname].append(self.empname)
        else:
            self.empdict[self.deptname]=[self.empname]

    def emp_display(self):
        print(self.empid," ",self.empname," ",self.empmobile," ",self.salary," ",self.age," ",self.gender," ",
              self.address," ",self.city," ",self.dob," ",self.doj," ",self.deptname," ",self.designation," ",self.pn," ",self.an)

    @classmethod
    def DisplayEmployee(self):
        for k,v in self.empdict.items():
            print("Department Name:",k)
            for e_name in v:
                print(e_name,end=" ")
            print("")


emplist = []
print("Employee Managemanet System")
print("")

while True:
    print("============================================")
    print("1:Add an employee")
    print("2:Display the employee details")
    print("3:Search the employee")
    print("4:Update the employee")
    print("5:Delete the employee")
    print("6:Display the details of employee with highest salary")
    print("7:Display the details of employee with lowest salary")
    print("8:Exit")
    print("")
    choice = int(input("Enter the choice"))
    if (choice == 1):
        while True:
            e_i=input("Enter Empolyee Id: ")
            if (isEmpidValid(e_i)):
                break
            else:
                print("Invalid EmpId ")
        while True:
            e_n=input("Enter Empolyee Name: ")
            if (isNameValid(e_n)):
                break
            else:
                print("Invalid Emp Name")
        while True:
            e_m=input("Enter Employee Mobile No: ")
            if (isMobileValid(e_m)):
                break
            else:
                print("Invalid Emp Mobile No")
        while True:
            e_s=input("Enter Empolyee Salary: ")
            if (isSalValid(e_s)):
                break
            else:
                print("Invalid Salary")
        while True:
            e_a=input("Enter Empolyee Age: ")
            if (isAgeValid(e_a)):
                break
            else:
                print("Invalid Age")
        e_g=input("Enter Empolyee Gender: ")
        e_add=input("Enter Empolyee Address: ")
        e_c=input("Enter Empolyee City: ")
        while True:
            e_dob=input("Enter Empolyee DOB: ")
            if (isDobValid(e_dob)):
                break
            else:
                print("Invalid Date Of Birth")
        e_doj=input("Enter Empolyee DOJ: ")
        e_dn=input("Enter Empolyee Department Name: ")
        e_d=input("Enter Empolyee Designation: ")
        while True:
            e_pn=input("Enter Empolyee Pan no: ")
            if (isPanValid(e_pn)):
                break
            else:
                print("Invalid Pan Number")
                
        while True:
            e_an=input("Enter Empolyee Adhaar no: ")
            if (isAdharValid(e_an)):
                break
            else:
                print("Invalid Aadhar Number")

        emp = employee(e_i,e_n,e_m,e_s,e_a,e_g,e_add,e_c,e_dob,e_doj,e_dn,e_d,e_pn,e_an)
        emplist.append(emp)
    elif choice == 2:
        for i in emplist:
            i.emp_display()
    elif choice == 3:
        print("==================================================")
        print("Press A to search the employee by Emp Id:")
        print("Press B to search the employee by Emp Name:")
        print("Press C to search the employee by Department Name:")
        print("")
        ch = input("Enter the choice:")
        if(ch == "A"):
            eid =input("Enter the Emp id to be searched: ")
            for i in emplist:
                if i.empid == eid:
                    i.emp_display()
                    ##print(i.empid,i.empname)
                    
        elif ch == "B":
            ename = input("Enter the Emp Name to be searched: ")
            for i in emplist:   
                if i.empname == ename:
                    i.emp_display()
        elif ch == "C":
            nm = input("enter the name to be searched: ")
            for i in emplist:
                if i.empname == nm:
                    i.DisplayEmployee()
                    ##employee.DisplayEmployee()

    elif choice == 4:
        print("=================================================")
        print("1:Update the Name of Emplyee")
        print("2:Update the Address of Emplyee")
        print("3:Update the DOB of Emplyee")
        print("4:Update the Salary of Emplyee")
        ch = input("Enter the choice")
        if (ch == "1") :
            eid = input("Enter the EID : ")
            for i in emplist:
                if i.empid==eid:
                   nm=input("Enter the name to be updated :")
                   i.empname=nm
                   i.emp_display()

        elif (ch=="2"):
            eid = input("Enter the EID : ")
            for i in emplist:
                if i.empid==eid:
                   ad=input("Enter the Address to be updated :")
                   i.address=ad

        elif (ch=="3"):
            eid = input("Enter the EID : ")
            for i in emplist:
                if i.empid==eid:
                   db=input("Enter the DOB to be updated :")
                   i.dob=db
                
        elif (ch=="4"):
            print("")
            print("A: Update the salary of specific Employee by Employee id")
            print("B: Update the salary of all Employees working in specific department")
            print("C: Update the salary of all Employees.")
            ch = input("Enter your choice : ")
            if ch == "A" :
                eid=input("Enter the EID : ")
                for i in emplist:
                    if i.empid==eid:
                        new_sal=input("Enter the Salary: ")
                        i.salary=new_sal
                    
            elif ch=="B":
                dnm=input("Enter the Department Name : ")
                for i in emplist:
                    if i.deptname==dnm:
                        a=input("Enter the Salary: ")
                        i.salary=a

            elif ch == "C":
                a=input("Enter the New Salary: ")
                i.salary=new_sal
                i.emp_display()

    elif choice == 5:
        eid = input("Enter the Employee Id to be deleted: ")
        for i in emplist:
            if i.empid==eid:
                emplist.remove(i)
                print("Record Deleted ")


    elif choice == 6:
        maxi=0
        print("Empoyee with Highest salary  is:")
        for i in emplist:
            a=int(i.salary)
            if a > maxi:
                maxi = int(i.salary)
                i.emp_display()


    elif choice == 7:
        min_salary = 999999
        print("Emplyee with Lowest salary is: ")
        for i in emplist:
            b=int(i.salary)
        if b < min_salary:
            i.emp_display()
            
    
    elif choice == 8:
        break




                
                    
            









        
        



















        
