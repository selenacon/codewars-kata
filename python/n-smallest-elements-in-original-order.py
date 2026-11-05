'''Your task is to write a function that does just what the title suggests (so, fair warning, be aware that you are not 
getting out of it just throwing a lame basic sorting method there) with a list of integers and the expected number n 
of smallest elements to return.

Also:

the number of elements to be returned cannot be higher than the list length;
elements can be duplicated;
in case of duplicates, just return them according to the original order (see third example for more clarity).
Same examples and more in the test cases:'''

def first_n_smallest(arr, n):
    if n == len(arr): return arr
    else: difference = sorted(arr)[n-len(arr):]
    nSmallestNumbers = [number for number in arr if number not in difference or arr.count(number) >1]
    while len(nSmallestNumbers) !=n and nSmallestNumbers !=[]:
        nSmallestNumbers.pop()
    return nSmallestNumbers

if __name__ == '__main__':
    assert first_n_smallest([1,2,3,4,5],3) == [1,2,3]
    assert first_n_smallest([1,2,3,4,5],3) == [1,2,3]
    assert first_n_smallest([5,4,3,2,1],3) == [3,2,1]
    assert first_n_smallest([1,2,3,1,2],3) == [1,2,1]
    assert first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
    assert first_n_smallest([1,2,3,4,5],0) == []
    assert first_n_smallest([1,2,3,4,5],5) == [1,2,3,4,5]
    assert first_n_smallest([1,2,3,4,2],4) == [1,2,3,2]
    assert first_n_smallest([2,1,2,3,4,2],2) == [2,1]
    assert first_n_smallest([2,1,2,3,4,2],3) == [2,1,2]
    assert first_n_smallest([2,1,2,3,4,2],4) == [2,1,2,2]