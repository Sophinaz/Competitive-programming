class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime = sorted(processorTime)
        tasks = sorted(tasks,reverse = True)
        result = 0
        idx = 0
        for i in processorTime:
            result = max(result,i + tasks[idx])
            idx+=4

        return result


        
        