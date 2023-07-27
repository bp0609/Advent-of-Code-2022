with open("input_day_11.txt","r") as file:
    content=file.read()
lst=content.split("\n\n")

items=[]
operations=[]
operation_nums=[]
tests=[]
t_case=[]
f_case=[]
iterations=[0]*len(lst)

def addition(old , num):
    return old+num
def multiply(old,num):
    return old*num
def square(old):
    return old*old

for i in lst:
    lst1=i.split("\n ")
    divisible_num=int(lst1[3].split("by ")[1])
    t_monkey=int(lst1[4].split("monkey ")[1])
    f_monkey=int(lst1[5].split("monkey ")[1])
    item=list(map(int,lst1[1].split(": ")[1].split(",")))    # it is a list
    
    if lst1[2].split("old ")[1].split(" ")[1]=="old":
        operation_num=0
        operation="sq"
    else:    
        operation_num=int(lst1[2].split("old ")[1].split(" ")[1])
        operation=lst1[2].split("old ")[1].split(" ")[0]
    
#--------------Storing Data------------------------------------->>>>    
    items.append(item)
    operations.append(operation)
    operation_nums.append(operation_num)    
    tests.append(divisible_num)
    t_case.append(t_monkey)
    f_case.append(f_monkey)
# ------------Data Stored--------------------------------------->>>>
for i in range(20):
    for j in range(len(lst)):
        iterations[j]=len(items[j])+iterations[j]
        for item in range(len(items[j])):
            if not items[j]:
                break
            k=items[j].pop(0)
            if operations[j]=="*":
                new=multiply(k,operation_nums[j])//3
            elif operations[j]=="sq":
                new=square(k)//3
            else:
                new = addition(k,operation_nums[j])//3
                
            
            if (new%tests[j])==0:
                items[t_case[j]].append(new)
                
            else:
                items[f_case[j]].append(new)
            
print(iterations)
