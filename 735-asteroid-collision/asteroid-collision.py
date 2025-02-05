class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and (stack[-1] > 0 and asteroid < 0):
                if abs(stack[-1]) > abs(asteroid):
                    # the new asteroid is destroyed
                    print(f"the new asteroid, {asteroid} is destroyed")
                    break
                elif abs(stack[-1]) < abs(asteroid):
                    print(f"the new asteroid, {asteroid} destroys the 'defender'")
                    stack.pop()
                    # the new asteroid destroys the 'defender'
                elif abs(stack[-1]) == abs(asteroid):
                    print(f"they collide, with asteroid {asteroid} but both blow up")
                    stack.pop()
                    break
                    # they collide but both blow up
            else:
                # if same sign, append asteroid (no collision)
                print(f"append asteroid, {asteroid}")
                stack.append(asteroid)
        
        return stack