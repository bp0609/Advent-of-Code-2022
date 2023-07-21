with open("input_day_10.txt","r") as file:
    content=file.read().split("\n")
x=1
i=0
clk=0
sum=0
addclk=0
j=0
while i<len(content):
    if clk==(19+j*40):
        num=20+(j*40)
        sum= sum + (x*num)
        j=j+1
        if j==6:
            exit
    
    if content[i].startswith('noop'):
        clk+=1
        i+=1
        continue
    else :
        num=int(content[i].split(" ")[1])
        addclk=addclk+1
        if addclk==1:
            clk=clk+1
            continue
        if addclk==2:
            i=i+1
            addclk=0
            x=x+ num
            clk=clk+1
print(sum)