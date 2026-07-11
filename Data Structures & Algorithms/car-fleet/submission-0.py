class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        count = 1
        for i in range(len(cars)-2, -1, -1):
            if ((target-cars[i][0])/cars[i][1])>((target-cars[i+1][0])/cars[i+1][1]):
                count += 1
            else:
                cars[i] = cars[i+1]
        return count
