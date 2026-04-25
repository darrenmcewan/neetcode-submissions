class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        if 0 <= i < self.length:
            return self.arr[i]
        raise IndexError("Index out of bounds")


    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.length:
            self.arr[i] = n
        else:
            raise IndexError("Index out of bounds")

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        self.arr[self.length] = n
        self.length += 1
        
    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
            return self.arr[self.length]
        raise IndexError("Cannot pop from empty array")

    def resize(self) -> None:
        self.capacity = max(1, 2 * self.capacity)
        new_arr = [0] * self.capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity