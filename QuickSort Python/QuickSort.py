def partition(arr,baslangıc,bitis):
    i = (baslangıc - 1)
    pivot = arr[bitis]
    for j in range(baslangıc, bitis):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] =  arr[j], arr[i]
    arr[i+1],arr[bitis] = arr[bitis],arr[i+1]
    return (i+1)
    
def quickSort(arr, baslagıc, bitis):
    if baslagıc < bitis:
        parcalamaindex = partition(arr,baslagıc,bitis)
        quickSort(arr, baslagıc, parcalamaindex - 1)
        quickSort(arr, parcalamaindex + 1, bitis)

girdi = [9, -3, 5, 2, 6, 8, -6, 1, 3]
girdiuzunluk = len(girdi)
quickSort(girdi, 0,girdiuzunluk -1)
print(girdi)
