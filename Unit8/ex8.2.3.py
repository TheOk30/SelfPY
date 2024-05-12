def mult_tuple(tuple1, tuple2): 
    return combinations(tuple1, tuple2)

def combinations(t1, t2):
        # create a list of tuples with all combinations of elements from t1 and t2
        comb = []
        for x in t1:
             for y in t2:
                  comb.append((x, y))
        # add all combinations of elements from t2 and t1
        for x in t1:
             for y in t2:
                  comb.append((y, x)) 
        return comb

def main():
    first_tuple = (1, 2, 3)
    second_tuple = (4, 5, 6)
    print(mult_tuple(first_tuple, second_tuple))
    #((1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), 
    #(3, 6), (4, 1), (5, 1), (6, 1), (4, 2), (5, 2), (6, 2), (4, 3), (5, 3), (6, 3))

if __name__ == "__main__":
    main()