import ListComporation

if __name__ == '__main__':
    my_lists = ListComporation.ListComporation([1,2,4,8,6], [6,4,8,1,5,9])
    my_lists.find_averages()
    print(my_lists.avg1, my_lists.avg2, sep="\n")
    my_lists.compare()



