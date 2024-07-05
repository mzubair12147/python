def printIter(iterable):
    for i in iterable:
        print(i)

'''
    a set is a collection whih is unordered and unindexed
    they do not allow duplicate values

    faster then a list to compare and see if something is in the list
'''

unique_responses = {1,2,1,1,1,1,1,5,200,5,6,6,74}
another_set = {1,2,'value 1', 'value 2', 'value 3'}
# set methods
unique_responses.add('another element')
unique_responses.remove('another element')
# unique_responses.clear()

# add elements of one set to another set
# note: "There will no order between the previous and new elements"
unique_responses.update(another_set)

# create an interly new set by using join
new_set = unique_responses.union(another_set)

# getting common elements by comparing the sets
common_elements = unique_responses.intersection(another_set)

has_unique_responses = unique_responses.difference(another_set)

printed = has_unique_responses

# the looped elements of the  sets may not be in the same order becaues the elements of the set are unordered
printIter(printed)