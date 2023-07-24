#x--create
##a=open(example.txt","x")
##a.close()
#File Create Specfic Folder, r --raw data
##a=open(r"C:\Users\Y MANIKANTA SWAMY\Desktop\example.txt","x")#xlsx .csv, .docx
##a.close()
#w--write and Create
##a=open("example.txt","w")
##a.write("File Handling Class")
##a.write("\tFile Handling Class2")
##s=['\nhii\n','Bye\n','dr 2025']
##a.writelines(s)
##a.close()
#append -->add new data
##a=open("example.txt","a")
###a.write("File Handling Class")
##s=['\nhii\n','Bye\n','dr 2025']
##a.writelines(s)
##a.close()
#Reading The Data In File
##a=open("example.txt","r")
###f=a.read()
##z=[]
##f=a.readlines()
##for i in f:
##    z.append(i)
##print(z)
##print(f)
##a.close()
##############
##a=open("D:\AIML-CODING\data.csv","r")
##f=a.readlines()
##a.close()
##c=0
##c1=0
##c2=0
##for i in f:
##    if i[2:4] in ['mh','MH']  and  i[6:8]=='05' :
##        print(i)
##        c+=1 
##for i in f:
##    if 'p3' in i or 'P3' in i:
##        c=c+1;
##        #print(i)
##    elif 'mh' in i or 'MH' in i:
##        c1+=1
##    else:
##        c2+=1   
##print(c)
##print(c1)
##print(c2)




