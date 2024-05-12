def inverse_dict(course_dict):
    new_dict = {}
    for key, value in course_dict.items():
        if value in new_dict:
            new_dict[value].append(key)
        else:
            new_dict[value] = [key]
    return new_dict

def main():
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    inverse_dict(course_dict)
    #{3: ['I', 'love'], 2: ['self.py!']}

if __name__ == "__main__":
    main()