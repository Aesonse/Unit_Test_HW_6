class ListComporation:
    def __init__(self, list1, list2):
        self.list1, self.list2 = list1, list2

    def find_averages(self):
        if len(self.list1) == 0:
            self.avg1 = 0
        else: self.avg1 = sum(self.list1) / len(self.list1)

        if len(self.list2) == 0:
            self.avg2 = 0
        else: self.avg2 = sum(self.list2) / len(self.list2)

    def compare(self):
        if 'self.avg1' not in locals():
            self.find_averages()
        if self.avg1 > self.avg2:
            print("Первый список имеет большее среднее значение")
        elif self.avg2 > self.avg1:
            print("Второй список имеет большее среднее значение")
        else:
            print("Средние значения равны")