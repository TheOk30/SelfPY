def main():
        list1 = [1, 2, 3, 4]
        list2 = [5, 6, 7]
        list3 = list1 + list2
        list4 = [list1 + list2]

        print(len(list3)) # 7
        print(len(list4)) # [[1,2,3,4,5,6,7]] -- 1
        print(list1[2]+list3[4]) # 3 + 5 = 8
        print(list4[3]) # error code
        print(list4[0][3]) # 4
        print(len(list2*list1[1])) # 6
if __name__ == "__main__":
        main()