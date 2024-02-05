age_dict = {'Bob': 59, 'Aya': 36, 'Gus': 40, 'Mel': 75}

student_name.input()

student_age = age_dict.pop(student_name)

print(f'The age of {student_name} is {student_age}')
print('Remaining pairs:')
print(age_dict)