class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(zip(position, speed), reverse=True)
        position, speed = zip(*combined)
        stack=[]
        for i in range(len(position)):
            time=(target-position[i])*1.0/speed[i]
            if not stack or stack[-1]<time:
                stack.append(time)
        return len(stack)
        