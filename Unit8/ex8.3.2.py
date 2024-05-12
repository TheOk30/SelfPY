def main():
    mariah = {
        'first_name': 'Mariah',
        'last_name': 'Carey',
        'birth_date': '27.03.1970',
        'hobbies': ['Sing', 'Compose', 'Act']
    }

    user_input = int(input("Enter a number between 1 and 7: "))

    match user_input:
        case 1:
            print(mariah['last_name'])
        case 2:
            month = mariah['birth_date'].split('.')[1]
            print(month)
        case 3:
            print(len(mariah['hobbies']))
        case 4:
            print(mariah['hobbies'][-1])
        case 5:
            mariah['hobbies'].append('Cooking')
            print(mariah['hobbies'])
        case 6:
            birth_date = tuple(mariah['birth_date'].split('.'))
            print(birth_date)
        case 7:
            mariah['age'] = 2023 - int(mariah['birth_date'].split('.')[2])
            print(mariah['age'])


if __name__ == "__main__":
    main()