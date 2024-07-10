import random
import time

def selectionsort(arr):
    n = len(arr)
    for i in range(n-1):
        minindex = i
        for j in range(i+1, n):
            if arr[j] < arr[minindex]:
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]

def display(arr):
    for i in arr:
        print(i, end=' ')
    print()

def main():
    n = int(input("Enter number: "))
    arr = [random.randint(0, 9999) for _ in range(n)]
    
    print("Before sorting:")
    display(arr)
    
    start = time.time()
    selectionsort(arr)
    end = time.time()
    
    print("After sorting:")
    display(arr)
    
    time_taken = (end - start) * 1000
    print(f"Time taken: {time_taken:.2f} milliseconds")

if __name__ == "__main__":
    main()
