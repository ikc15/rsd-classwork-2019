from times import *

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:45:00")
    short = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    print(overlap_time(large, short))
    result = overlap_time(large, short) 
    expected = large
    assert result == expected

def test_class_time():
    large = time_range("2019-10-31 10:00:00", "2019-10-31 13:00:00")
    short = time_range("2019-10-31 10:05:00", "2019-10-31 12:55:00", 3, 600)
    print(overlap_time(large, short))
    result = overlap_time(large, short) 
    assert result == short
    
def test_time_interval():
    large = time_range("2019-10-31 00:00:00", "2019-10-31 23:50:00",24,10 * 60)
    short = time_range("2019-10-31 00:30:00", "2019-10-31 23:55:00",24,35 * 60)
    result = overlap_time(large, short)
    assert all([time_interval(t1,t2) == 20 * 60 for t1, t2 in result]) # check interval is 20mins = 1200s
 
# other tests
    # no overlap
    # break longer than short
    # large shorter than short
    # when both time ranges are same