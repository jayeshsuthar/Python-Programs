def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Maths', 'Arts', 'CompCS']
info = {'name':'Jayesh', 'age': 21 }

student_info(*courses, **info)
