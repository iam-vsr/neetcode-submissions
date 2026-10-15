class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            #nlogn is trivial, just append and sort and then merge intervals
            #another approach is to find the right position i.e. the 
            #correct place where interval should be and then merge intervals
            def merge(arr):
                    n=len(arr)
                    arr.sort()
                    ans=[]
                    l=arr[0][0]
                    r=arr[0][1]

                    for i in range(1,n):
                            if r>=arr[i][0]:
                                    l=min(arr[i][0],l)
                                    r=max(arr[i][1],r)
                            else:
                                    ans.append([l,r])
                                    l=arr[i][0]
                                    r=arr[i][1]
        
                    ans.append([l,r])
                    return ans  

            #could use binary search for searching appropriate place  
            n=len(intervals)
            target=newInterval[0]
            l,r=0,n-1

            while l<=r:
                m=(l+r)//2
                if intervals[m][0]<target:
                    l=m+1
                else:
                    r=m-1
    
            intervals.insert(l,newInterval) #O(N) operation

            return merge(intervals)


