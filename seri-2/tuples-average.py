def average_tuple(two_dimentional_tuple):
    '''write an appropriate docstring here'''
    return tuple(map(lambda x : sum(x)/len(x), tuple(zip(*two_dimentional_tuple))))
    # write the rest of definition bellow


# your submission must include following lines of codes
if __name__ == '__main__':
    expression_to_evaluate = input()
    print(eval(expression_to_evaluate))
