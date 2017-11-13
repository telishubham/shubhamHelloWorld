stud=["Raj","Shaista","Sheetal","Pooja","Ramesh"]
print(stud)
name=input("enter student name:")
stud.append(name)
print(stud)
idx=int(input("enter a number"))
l=len(stud)
if idx<=(l-1):
    print(stud[idx])
else:
    print("wrong index")
stud1=["Rahul","Aman"]
stud=stud1+stud
print(stud)
nm=input("enter the name you want to search")
if nm in stud:
    i=stud.index(nm)
    del stud[i]
    print(stud)
    print(nm,"has deleted")
else:
    stud.append(nm)
    print(stud)
    print(nm,"is appended to list")
rev_stud=list(reversed(stud))
print("original list",stud)
print("reversed list ",rev_stud)
del stud[-1]
print(stud)
print("last element is deleted")
