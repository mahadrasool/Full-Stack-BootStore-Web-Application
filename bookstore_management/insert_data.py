from bookstore_management.models import Course, Department

# Define the data
data = [
    ('ACCT2311', 'Fundamentals of Financial Accounting', 'ACCT'),
    ('MISY2311', 'Introduction to Management Information Systems', 'MISY'),
    ('BUSI2311', 'Principles of Management', 'BUSI'),
    ('MISY2312', 'Introduction to Programming for MIS', 'MISY'),
    ('MISY2313', 'Intermediate Programming for MIS', 'MISY'),
    ('MISY3312', 'Introduction to Telecommunications', 'MISY'),
    ('BUSI3311', 'Legal Environment of Business', 'BUSI'),
    ('BUSI3312', 'Organizational Behavior', 'BUSI'),
    ('BUSI3313', 'Marketing Principles', 'BUSI'),
    ('BUSI3321', 'Operation Management', 'BUSI'),
    ('MISY3311', 'Database Management', 'MISY'),
    ('MISY3322', 'Systems Analysis and Design', 'MISY'),
    ('ACCT2321', 'Managerial Accounting', 'ACCT'),
    ('MISY4331', 'Building Electronic Commerce', 'MISY'),
    ('MISY4333', 'Introduction to Information Assurance', 'MISY'),
    ('MISY3331', 'Advanced Database Concepts', 'MISY'),
    ('MISY4341', 'Object Oriented Analysis and Design', 'MISY'),
    ('FINA3311', 'Financial Management Principles', 'FINA'),
    ('BUSI4361', 'Entrepreneurship', 'BUSI'),
    ('BUSI4362', 'Strategic Management', 'BUSI'),
    ('SOEN2312', 'Web Programming', 'SOEN'),
    ('SOEN2332', 'Discrete Structure and Combinatorial Analysis', 'SOEN'),
    ('SOEN3351', 'Algorithms', 'SOEN'),
    ('SOEN3311', 'Requirements Engineering', 'SOEN'),
    ('SOEN4361', 'Operating System', 'SOEN'),
    ('SOEN4371', 'E-Commerce', 'SOEN'),
    ('SOEN4311', 'Software Architecture and Design', 'SOEN'),
    ('SOEN4313', 'Software Project Management', 'SOEN'),
    ('ITAP2431', 'Network Management', 'ITAP'),
    ('ITAP2312', 'Web Programming', 'ITAP'),
    ('ITAP3431', 'Network Security', 'ITAP'),
    ('ITAP3313', 'User Interface Development', 'ITAP'),
    ('ITAP3471', 'Web Server Administration', 'ITAP'),
    ('ITAP3383', 'Enterprise Resource Planning Systems', 'ITAP'),
    ('ITAP3382', 'Business Intelligence', 'ITAP')
]

# Insert data into the Course model
for item in data:
    try:
        department_code = item[2]  # Fetch DepartmentCode from data
        department = Department.objects.get(DepartmentCode=department_code)  # Get the Department object
        course = Course.objects.create(
            CourseID=item[0],
            CourseName=item[1],
            DepartmentCode=department  # Assign the Department object to DepartmentCode
        )
        print(f"Course created: {course}")
    except Department.DoesNotExist:
        print(f"Department with DepartmentCode {department_code} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Data insertion complete.")
