#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		first = self.occurrence(arr, n, x, first = True, last = False)
		last = self.occurrence(arr, n, x, first = False, last = True)
		if first != -1 and last != -1:
		    return (last - first + 1)
		else:
		    return 0
		
	def occurrence(self, arr, n, x, first, last):
	    start = 0
	    end = n - 1
	    occurrence = -1
	    while start <= end:
	        mid = start + (end - start) // 2
	        if x == arr[mid]:
	            occurrence = mid
	            if first:
	                end = mid - 1
	            if last:
	                start = mid + 1
	        elif x < arr[mid]:
	           end = mid - 1
	        else:
	           start = mid + 1
	    return occurrence
		        
		    

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends