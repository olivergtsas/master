import random

list_size = 10  # Adjust this value as needed
min_value = 1   # Minimum value for the integers
max_value = 100 # Maximum value for the integers

random_list = random.sample(range(min_value, max_value + 1), list_size)

print("Random list of unique integers:", random_list)

random_list.sort()

arr = random_list
def find_max(arr, low, high):
    
    
    if low == high:
        return arr[low]
    
    
    
    mid = (low + high) // 2
    
    
    
    
    max_left  = find_max(arr,low, mid)
    max_right = find_max(arr, mid +1, high)
    
    return(max(max_left, max_right))

  
    

def binary_search(arr, target, low, high):
    
    
    if low <= high:
        mid = (low + high) // 2
        cand = arr[mid]

        if cand == target:
            return mid
        elif cand < target:
            return binary_search(arr, target, mid + 1, high)
        else:  # cand > target
            return binary_search(arr, target, low, mid - 1)
    else:
        return "Not found"  
    
    
    
print(binary_search(arr, 15, 0, len(arr)-1)) 
           
    
    
    
    
