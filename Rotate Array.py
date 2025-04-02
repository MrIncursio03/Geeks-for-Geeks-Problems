class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d %= n
        
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
                
        reverse(arr, 0, d-1)
        
        reverse(arr, d, n-1)
        
        reverse(arr, 0, n-1)
