import ListComporation
import pytest

@pytest.mark.parametrize("list1,list2,avg_exp1,avg_exp2",
                         [([1,2,3,4,5,6],  [-1,-2,-3,-4,-5,-6], 3.5, -3.5),
                          ([],[],0,0),
                          ([4.56],[-6000000],4.56,-6000000)])
def test_averages(list1, list2, avg_exp1, avg_exp2):
    test_lists = ListComporation.ListComporation(list1, list2)
    test_lists.find_averages()
    assert test_lists.avg1 == avg_exp1
    assert test_lists.avg2 == avg_exp2

@pytest.mark.parametrize("list1,list2,comp_exp",
                         [([1,2,3,4,5,6],  [-1,-2,-3,-4,-5,-6], "Первый список имеет большее среднее значение\n"),
                          ([],[],"Средние значения равны\n"),
                          ([-4.56],[6000000],"Второй список имеет большее среднее значение\n")])
def test_compare(list1, list2, comp_exp, capsys):
    test_lists = ListComporation.ListComporation(list1, list2)
    test_lists.compare()
    assert capsys.readouterr().out == comp_exp

def test_not_numbers():
    test_lists = ListComporation.ListComporation(['ab'], ["cd"])
    with pytest.raises(TypeError):
        test_lists.compare()
    with pytest.raises(TypeError):
        test_lists.find_averages()

