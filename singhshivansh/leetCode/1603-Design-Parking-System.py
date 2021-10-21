# Author: @Iresharma
# https://leetcode.com/problems/design-parking-system/submissions/

"""
Runtime: 128 ms, faster than 97.42% of Python3 online submissions for Design Parking System.
Memory Usage: 14.5 MB, less than 93.43% of Python3 online submissions for Design Parking System.
"""

class ParkingSystem:
    parkSpace = {}
    def __init__(self, big: int, medium: int, small: int):
        self.parkSpace[1] = big
        self.parkSpace[2] = medium
        self.parkSpace[3] = small

    def addCar(self, carType: int) -> bool:
        if self.parkSpace[carType] > 0:
            self.parkSpace[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)