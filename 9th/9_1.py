my_list = [1,2,3]

def get_min_avg_max(sequence):
    max_val = max(sequence) 
    min_val = min(sequence) 
    avg = sum(sequence)/len(sequence)
    return min_val, avg, max_val

res = get_min_avg_max(my_list)
print(res, type(res))