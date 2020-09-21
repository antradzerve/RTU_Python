import math

def sum_prod_all(*seq_n):
    end_result = 0
    for x in seq_n:
        end_result += math.prod(x)
    
    return end_result

if __name__ == "__main__":
    sum_prod_all()