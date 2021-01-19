from itertools import chain, combinations

def number_of_subsets(subsets):
    if len(subsets)==1:
        return subsets[0]
    return subsets

def remove_duplicate (final_list):
    answer=[]
    for i in final_list:
        if i not in answer:
            answer.append(i)
    for i in answer:
        i.sort(reverse=True)
    return number_of_subsets(answer)

def sub_list(iterable) :
    input_list=list(iterable)
    return chain.from_iterable(combinations(input_list, r) for r in range(len(input_list)+1))

def get_subset_for_sum(arr, k):
    if k == 0:
        return []
    elif len(arr) == 0:
        return 'None'
    subset_list=[]
    for i in sub_list(arr):
        if sum(i) == k:
            subset_list.append(list(i))
    if len(subset_list) == 0:
        return 'None'
    return remove_duplicate (subset_list)

print(get_subset_for_sum([1,2,3,4], 4))