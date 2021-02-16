def selection_sort(mylist):
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            if mylist[i]>mylist[j]:
                mylist[i],mylist[j] = mylist[j],mylist[i]

    return mylist
if __name__ == '__main__':
    mylist = [78,65,90,54,65,21,43]
    print(selection_sort(mylist))
