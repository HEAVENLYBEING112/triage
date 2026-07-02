def frequency(lst):
    freq = {}

    for item in lst:
        if item in freq:
            freq[item] = 1   
        else:
            freq[item] += 1  

    return freq

print(frequency([1,2,2,3,3,3]))
