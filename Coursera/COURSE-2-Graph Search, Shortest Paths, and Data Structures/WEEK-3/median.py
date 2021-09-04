import heapq

class Heap:
    def __init__(self, initial=None, key=lambda x:x):
        self.key = key
        if initial:
            self.data = [(key(item), item) for item in initial]
            heapq.heapify(self.data)
        else:
            self.data = []

    def push(self, item):
        heapq.heappush(self.data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self.data)[1]

    def peek(self):
        return self.data[0][1]

    def __len__(self):
        return len(self.data)

    
class Median:
    def __init__(self, input_file):
        self.heap_low = Heap(key=lambda x: -x)
        self.heap_high = Heap()
        self.median_sum = 0
        self.input_file = input_file

    def sum_median(self):
        if self.input_file is not None:
            with open(self.input_file) as file:
                for number in file.read().splitlines():
                    self.add_number(int(number))

        return self.median_sum % (len(self.heap_high) + len(self.heap_low))


    def add_number(self, num):
        if not self.heap_low:
            self.heap_low.push(num)
            self.median_sum += num
            return 
        if num <= self.heap_low.peek():
            self.heap_low.push(num)
        else:
            self.heap_high.push(num)
        if len(self.heap_low) - len(self.heap_high) > 1:
            self.heap_high.push(self.heap_low.pop())
        elif len(self.heap_high) - len(self.heap_low) > 1:
            self.heap_low.push(self.heap_high.pop())
        self.median_sum += self.heap_low.peek() if len(self.heap_low) >= len(self.heap_high) else self.heap_high.peek()


if __name__ == '__main__':
    median = Median(input_file='Median.txt')
    sum_medians = median.sum_median()
    print(sum_medians)
        