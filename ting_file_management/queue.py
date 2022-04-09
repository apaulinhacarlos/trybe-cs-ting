class Queue:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        if self.__len__ == 0:
            return None
        return self.data.pop(0)

    def search(self, index):
        length = len(self.data)
        if length == 0 or index < 0 or index >= length:
            raise IndexError
        else:
            return self.data[index]
