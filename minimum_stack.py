class MinStack:

    def __init__(self):
        self.store = []
        self.min_store = []


    def push(self, val: int) -> None:
        self.store.append(val)
        x = self.min_store[-1]if self.min_store else val
        min_val = min(val,x)
        self.min_store.append(min_val)



    def pop(self) -> None:
        self.store.pop()
        self.min_store.pop()

    def top(self) -> int:
        val =  self.store[-1]
        return val

    def getMin(self) -> int:
        # l = 0;
        # r = len(self.store)-1
        # small_val = self.store
        # while l<r:
        return self.min_store[-1]
