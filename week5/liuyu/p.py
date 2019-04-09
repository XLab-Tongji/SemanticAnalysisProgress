with open('input.txt','r')as f1:
    list1=f1.readlines()


f2=open('output.txt','w')
f2.writelines(list(set(list1)))
f2.close()
