with open('text file.txt','r') as file:
    content=file.read().split('\n')
# print(content)
x=1
i=0
clk=0
sum=0
addclk=0
j=0
while i<len(content):
    
    if (clk-x-j) in {-1,0,1}:
        print('#',end='')
    else:
        print('.',end='')
    # -----------------------------------------------------------
    if (clk%40)==39:
        j=40*((clk+1)//40)
        print(' ')
        if clk==239:
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
            