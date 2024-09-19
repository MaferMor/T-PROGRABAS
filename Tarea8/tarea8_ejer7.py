def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        
        print(f"Dividiendo {arr} en {left} (<= {pivot}) y {right} (> {pivot})")
        
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)
        
        result = sorted_left + [pivot] + sorted_right
        
        print(f"Combinando {sorted_left} + [{pivot}] + {sorted_right} = {result}")
        
        return result

arr = [38, 27, 43, 3, 9, 82, 10]
print(f"Lista original: {arr}")
sorted_arr = quick_sort(arr)
print(f"Lista ordenada: {sorted_arr}")
