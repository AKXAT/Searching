def merge_two_list(array_one,array_two):
    sorted_list = []
    length_array_one = len(array_one)
    length_array_two = len(array_two)
    i=j=0
    while i<length_array_one and j<length_array_two:
        if array_one[i] <= array_two[j]:
            sorted_list.append(array_one[i])
            i+=1
        else:
            sorted_list.append(array_two[j])
            j+=1
    while i<length_array_one:
        sorted_list.append(array_one[i])
        i+=1
    while j<length_array_two:
        sorted_list.append(array_two[j])
        j+=1

    return sorted_list

def merge_sort(mylist):
    if  len(mylist) <= 1:
        return mylist
    mid = len(mylist) // 2 
    left = mylist[:mid]
    right = mylist[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_list(left,right)
if __name__ == '__main__':
    a = [34,5,3,5,34,45,56,67,78,1,2]
    print(merge_sort(a))
