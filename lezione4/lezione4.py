#8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.


# Questa funzione implementa il bubble sort

def naive_bubble_sort(a:list[2,5,1,4,8,3,7,6]):
    for i in range(len(a)):
        for j in range(len(a-1)):
            if (a[j]) > a[j+1]:
                temp:int=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a
print(naive_bubble_sort())

def naive_bubble_sort(a:list[2,5,1,4,8,3,7,6]):
    for i in range(len(a) -i -1):
        for j in range(len(a-1)):
            if (a[j]) > a[j+1]:
                temp:int=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a
print(naive_bubble_sort())


import time
start: int= time.time()
print(time.time( - start))


