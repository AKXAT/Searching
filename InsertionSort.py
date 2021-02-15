def insertion_sort(mylist):
    for i in range(1,len(mylist)):
        pointer = mylist[i]
        j = i - 1
        while j>=0 and pointer < mylist[j]:
            mylist[j+1] = mylist[j]
            j-=1 
        mylist[j+1]=pointer
    return mylist
if __name__ == '__main__':
    mylist = [90,56,21,54,78,23,67]
    print(insertion_sort(mylist))

