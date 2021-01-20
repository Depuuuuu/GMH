from stackclass import *
his=SStack()
sih=SStack()
choice=0
while (choice!=6):
    choice = int(input("1.goto a new site\n2.goto the last site\n"
                       "3.print the history\n"
                       "4.delete the current history\n"
                       "5.go to the latter page\n"
                       "6.end\n"))
    if choice==1:
        his.push(input("the site is:\n"))
    if choice==2:
        sih.push(his.top())
        his.pop()
        print("Now at:"+his.top())
    if choice==3:
        for i in range(len(his)):
            print("History:%d "%(i+1)+his._data[i])
        for i in range(len(sih)):
            print("History:%d "%(i+1)+sih._data[i])
    if choice==4:
        his.pop()
        print("Now at:"+his.top())
    if choice==5:
        his.push(sih.top())
        sih.pop()
        print("Now at:"+his.top())
    if choice==6:
        break