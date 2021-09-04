from bisect import bisect_left, bisect_right

class Sum:
    def __init__(self, input_file):
        self._array = []
        array = set()
        with open(input_file) as file:
            for num in file:
                array.add(int(num))
        self._array = sorted(array)

    def two_sum(self):
        target_values = set()
        # count = 0
        for num in self._array:
            left = bisect_left(self._array, -10000 - num)
            right = bisect_right(self._array, 10000 - num)
            for pair in self._array[left:right]:
                if pair != num:
                    # count += 1
                    target_values.add(num + pair)
        return len(target_values)


Two_sum = Sum("two_sum.txt")
print(Two_sum.two_sum())
