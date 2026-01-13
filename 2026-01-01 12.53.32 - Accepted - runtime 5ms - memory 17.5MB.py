class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = logs[0][1]
        result = logs[0][0]
        prev_end = logs[0][1]
        for i in range(1, len(logs)):
            duration = logs[i][1] - prev_end
            if duration > max_time or (duration == max_time and logs[i][0] < result):
                max_time = duration
                result = logs[i][0]
            prev_end = logs[i][1]
        return result