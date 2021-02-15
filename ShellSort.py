def shell_sort(mylist):
    size = len(mylist)
    gap = size//2
    while gap>0:
        for i in range(gap,size):
            pointer = mylist[i]
            j = i
            while j >= gap and mylist[j-gap]>pointer:
                mylist[j] = mylist[j-gap]
                j -= gap
            mylist[j]=pointer
        gap = gap // 2
    return mylist
if __name__ == '__main__':
    mylist = [90,56,21,54,78,23,67]
    print(shell_sort(mylist)) 