def main():
    programming_languages = ['Python', 'Perl', 'R', 'Ruby']

    #which lines would output 'R'

    programming_languages[2][0] # correct
    programming_languages[3][0] # correct
    programming_languages[4][0] # error
    programming_languages[-2][0] # correct
    programming_languages[-1][-4] # correct
    programming_languages[-4][-1] # wrong
    programming_languages[2] # correct
    programming_languages[3] # wrong
    programming_languages[-2] # correct
    programming_languages[-3] # wrong
    programming_languages[-4] # wrong
    
if __name__ == "__main__":
    main()