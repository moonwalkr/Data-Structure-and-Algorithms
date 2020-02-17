def  Ordered_Seq_Search(array, ele):

    pos = 0
    found = False
    stopped = False
    while pos < len(arry) and not found and not stopped:
        if array[pos] == ele:
            found = True
        else:
            if array[pos] > ele:
                stopped = True
            else:
                pos += 1

    return found



