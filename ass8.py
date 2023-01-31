import pandas as pd

countries=['pak_inns1.txt','india_inns2.txt']
count=0
for country in countries:
 with open(country) as f:
     batter={}
     bowler={}   
     for line in f.readlines():
        a=line.strip()
        a=a.replace("!!",",")
        a=a.replace("by",",")
        a=a.replace("runs","run")
        a=a.replace("wides", "wide")
        if len(a)==0:
            continue
        s=a[4:]
        s=s.split(",")
        a=s[0]
        status=s[1]
        a=a.split("to")
        a[0]=a[0].strip()
        if not a[0] in bowler:
            bowler[a[0]]=[0 for i in range(7)]
        if not a[1] in batter:
            batter[a[1]]=["",0,0,0,0,0]
        if status.strip()=="out Caught":
            batter[a[1]][0]="c "+s[2]+" b "+a[0]
        if status.strip()=="out Bowled":
           batter[a[1]][0]="b "+a[0]
        x=s[1].split(" ")
        if x[1]=="FOUR":
            batter[a[1]][5]+=4
            batter[a[1]][2]+=1
            bowler[a[0]][2]+=4
        if x[1]=="SIX":
            batter[a[1]][5]+=6
            batter[a[1]][3]+=1
            bowler[a[0]][2]+=6
        if x[1]=='1' and x[2]=="run":
            batter[a[1]][5]+=1
            bowler[a[0]][2]+=1
        if x[1]=='2' and x[2]=="run":
            batter[a[1]][5]+=2
            bowler[a[0]][2]+=2
        if x[1]=='3' and x[2]=="run":
            batter[a[1]][5]+=3
            bowler[a[0]][2]+=3
        if x[1]=="out":
            bowler[a[0]][3]+=1 
        if  x[1]!="wide":
            batter[a[1]][1]+=1
            bowler[a[0]][0]+=1
        if x[1]=="wide":
            bowler[a[0]][2]+=1
            bowler[a[0]][5]+=1
        if len(x)>=3 and x[2]=="wide":
            batter[a[1]][1]-=1
            bowler[a[0]][0]-=1
            if x[1]=="1":
                bowler[a[0]][2]+=1
                bowler[a[0]][5]+=1
            if x[1]=="2":
                bowler[a[0]][2]+=2
                bowler[a[0]][5]+=2
            if x[1]=="3":
                bowler[a[0]][2]+=3
                bowler[a[0]][5]+=3
 for i in batter:
    x=batter[i][5]*100/batter[i][1]
    batter[i][4]=round(x,2)
    if len(batter[i][0])==0:
        batter[i][0]="not out"
   
 for j in bowler:
    bowler[j][6]=bowler[j][2]/((bowler[j][0]//6)+(bowler[j][0]%6)/6)
    bowler[j][6]=round(bowler[j][6],1)
    a=bowler[j][0]
    b=a//6
    if bowler[j][0]%6:
        a=b+0.1*(a%6)
    else :
        a=b
    bowler[j][0]=a
 header_bowler=["Bowler","   O","M","R","W","NB","WD", "ECO"]
 header_batter=[" Batter                     ","     R","  B "," 4s "," 6s "," SR "]   
 if count==0:
    mode="w"
    count=1
 else:
    mode='a'   
 with open ('scorecard.txt',mode) as file:
    file.write('\n') 
    if country=="pak_inns1.txt":
     file.write("Pakistan innings")
     file.write('\n') 
    else:
     file.write("India innings")
     file.write('\n') 
    file.write('\n') 
    for i in header_batter:
        i=str(i)
        file.write(i)
        file.write(" ")
    file.write("\n")
    for line_1 in batter: 
       # line_1=line_1.strip()
        file.write(line_1) 
        file.write(" ") 
       # print(line_1[1],end=" ")
        batter[line_1][0]=str(batter[line_1][0])
        file.write(batter[line_1][0])
        file.write(" ")
        batter[line_1][5]=str(batter[line_1][5])
        file.write(batter[line_1][5])
        file.write(" ")
        for j in range(1,5):
            j=batter[line_1][j]
            j=str(j)
            file.write(j)
            file.write(" ")
        file.write('\n') 
    file.write("\n")
    for i in header_bowler:
        i=str(i)
        file.write(i)
        file.write(" ")
    file.write("\n")
    for line_1 in bowler: 
        file.write(line_1) 
        file.write(" ") 
        for j in bowler[line_1]:
            j=str(j)
            file.write(j)
            file.write(" ")
        file.write('\n') 
    file.write("\n")
    






      

       