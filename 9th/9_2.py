def get_common_elements(seq1,seq2,seq3):
    s1 = set(seq1)
    s2 = set(seq2)
    s3 = set(seq3)

    res_1 = s1.intersection(s2)
    result = res_1.intersection(s3)

    return tuple(result)


final_result = get_common_elements("abc",['a','b'],('b','c'))
print(final_result, type(final_result))
