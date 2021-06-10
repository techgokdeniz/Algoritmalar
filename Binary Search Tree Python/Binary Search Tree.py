
#Method1 Recursive Method ile BinarySearchTree
def binarySearchRecursive(A,kucuk,buyuk,aranan):
    if kucuk<=buyuk:
        orta=kucuk+(buyuk-kucuk)//2
        if A[orta]==aranan:
            return print("Aranan Eleman "+format(orta)+".Indexte")
        elif A[orta]>aranan:
            return binarySearchRecursive(A,kucuk,buyuk-1,aranan)
        elif A[orta]<aranan:
            return binarySearchRecursive(A,kucuk+1,buyuk,aranan)
    return print("Eleman Bulunamadı")






#Method2 While Döngüsü Method ile BinarySearchTree

def binarySearchWhile(A,kucuk,buyuk,aranan):
    while kucuk<=buyuk:

        orta=kucuk+(buyuk-kucuk)//2
        if A[orta]==aranan:
            return print("Aranan Eleman "+format(orta)+".Indexte")
        elif A[orta]>aranan:
            buyuk=orta-1
        elif A[orta]<aranan:
            kucuk=orta+1
    return print("Eleman Bulunamadı")



sayilar=[1,2,3,4,5,6]
binarySearchRecursive(sayilar,0,len(sayilar)-1,3)
binarySearchWhile(sayilar,0,len(sayilar)-1,4)
binarySearchWhile(sayilar,0,len(sayilar)-1,35)
