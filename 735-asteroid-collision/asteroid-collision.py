class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        '''
        [5,10,-5]

        stack = [5, 10]

        [10, 2, -5]
        stack = [10]
        '''

        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if -a > stack[-1]:
                    stack.pop()
                    continue
                elif -a == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(a)

        return stack