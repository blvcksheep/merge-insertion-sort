import time
import random
import matplotlib.pyplot as plt


def merge(left, right):

    result = []
    a, b = 0, 0
    while a < len(left) and b < len(right):
        if(left[a] <= right[b]):
            result.append(left[a])
            a += 1
        else:
            result.append(right[b])
            b += 1
    result += left[a:]
    result += right[b:]
    return result


def mergeSort(listing):

    if (len(listing) <= 1):
        return listing
    middle = int(len(listing)/2)
    left = mergeSort(listing[:middle])
    right = mergeSort(listing[middle:])
    return merge(left, right)


def insertionSort(listing):
    for indx in range(len(listing)):
        num = listing[indx]
        i = indx - 1
        while i >= 0:
            if num < listing[i]:
                listing[i + 1] = listing[i]
                listing[i] = num
                i -= 1
            else:
                break
    for i in range(len(listing)):
        print(listing[i])


# def ploTest(time,number):


number = []
runTime = []
output = []
runTimeTwo = []

num = int(input("Number of element you want to sort:")) 
for i in range(0, num):
    starTime = time.time()
    x = (int(input("Enter number of list :")))
    number.append(x)
    starTime = time.time()
    output = [random.randint(1, x)for iter in range(x)]
    print('Insertion sort')
    print(insertionSort(output))
    runTime.append(time.time() - starTime)
    starTimeTwo = time.time()
    print('Merge sort - {}'.format(mergeSort(output)))
    runTimeTwo.append(time.time() - starTimeTwo)

print('Number of list - {}'.format(number))
print('Runtime of insertion sort - {}'.format(runTime))
print('Runtime of merge sort - {}'.format(runTimeTwo))

plt.plot(number, runTime, label="Insertion sort")
plt.plot(number, runTimeTwo, label="Merge sort")

plt.xlabel('Number')
plt.ylabel('Running time')
plt.title('Running time comparison of merge and insertion sort')
plt.legend()
plt.show()
