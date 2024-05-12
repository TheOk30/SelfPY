def sequence_del(str):
    new_str = str[0]
    for i in range(1, len(str)):
        if str[i] != new_str[-1]:
            new_str += str[i]
    return new_str

def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn")) #python
    print(sequence_del("SSSSsssshhhh")) #Ssh
    print(sequence_del("Heeyyy   yyouuuu!!!")) #Hey you!


if __name__ == "__main__":
    main()