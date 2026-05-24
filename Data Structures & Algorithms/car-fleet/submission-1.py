class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        fleets = []
        for car in cars:
            time = (target - car[0]) / car[1]
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return len(fleets)