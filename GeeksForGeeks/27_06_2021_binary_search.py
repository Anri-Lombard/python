class Solution:
    def searchInSorted (self, arr, N, k, start=0): 
      
        # Check base case 
        if N >= 1: 
            # calculate mid
            mid = int((start + N)/2)
      
            # If element is present at the middle itself 
            if arr[mid] == k: 
                return 1 
              
            # If element is smaller than mid, then it  
            # can only be present in left subarray 
            elif arr[mid] > k: 
                return self.searchInSorted(arr, mid-1, k, start=0) 
      
            # Else the element can only be present  
            # in right subarray 
            else: 
                return self.searchInSorted(arr, N, k, start=mid+1) 
      
        else: 
            # Element is not in array
            return -1