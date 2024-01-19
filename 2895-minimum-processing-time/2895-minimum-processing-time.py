class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime = sorted(processorTime,reverse=True)
        tasks = sorted(tasks)
        allocation = {}
        l,c = 0,0
        r=4
        result = []
        for i in range(len(processorTime)):
            allocation[processorTime[c]] = tasks[l:r]
            print(tasks[l:r])
            l+=4
            r+=4
            c+=1
            
        for i in allocation:
            result.append(i + max(allocation[i]))
        return max(result)


        
        