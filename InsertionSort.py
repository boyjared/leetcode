arr = [2,1]


def insertionsort(arr):
    length_arr = len(arr)
    for p in range(1,length_arr):
        for i in range(p-1, -1, -1):
            num = arr[p]
            while(num <= arr[i] and i >= 0):
                arr[i+1] = arr[i]
                i = i-1
            arr[i+1] =num
            break

insertionsort(arr)

print(arr)