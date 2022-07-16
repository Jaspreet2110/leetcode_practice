#User function Template for python3
class Solution: 
    def firstAndLast(self, arr, n, x): 
        first = self.firstOccurrence(arr, n, x)
        last = self.lastOccurrence(arr, n, x)
        if first != -1 and last != -1:
            return first, last
        else:
            return [-1]
    
    def firstOccurrence(self, arr, n, x):
        start = 0
        end = n - 1
        first_occurrence = -1
        while start <= end:
            mid = start + (end - start) // 2
            if x == arr[mid]:
                first_occurrence = mid
                end = mid - 1
            elif x < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return first_occurrence
    
    def lastOccurrence(self, arr, n, x):
        start = 0
        end = n - 1
        last_occurrence = -1
        while start <= end:
            mid = start + (end - start) // 2
            if x == arr[mid]:
                last_occurrence = mid
                start = mid + 1
            elif x < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return last_occurrence
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input()) 
    for _ in range(t):
        n,x = [int(i) for i in input().split()] 
        arr = [int(i) for i in input().split()] 
        ob=Solution() 
        ans=ob.firstAndLast(arr,n,x) 
        s=(" ").join(map(str,ans))
        print(s)

# } Driver Code Ends