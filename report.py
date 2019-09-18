import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first = first
        self.last = last
        self.slack = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first} {self.last} is in {self.cohort}'

class Instructors():

    def __init__(self, first, last, handle, specialty):
        self.first = first
        self.last = last
        self.slack = handle
        self.specialty = specialty

    def __repr__(self):
        return f'{self.first} {self.last} teaches {self.specialty}'

class Cohort():
    
    def __init__(self, name):
        self.name = name
        

    def __repr__(self):
        return f'{self.name}'

class Exercises():
    
    def __init__(self, name, language):
        self.name = name
        self.language = language
        

    def __repr__(self):
        return f'{self.name} is a {self.language} exercise'

# class All_Students_And_Exercises():
    
#     def __init__(self, name, toyname):
#         self.name = name
#         self.toyname = toyname
        

    




class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/ackno/workspace/sql/student_exercises/student_exercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
           
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.First,
                s.Last,
                s.Slack,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)
    
    def all_instructors(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructors(row[1], row[2], row[3], row[4])
           
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.First,
                i.Last,
                i.Slack,
                i.Specialty
            from Instructor i
            
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor)
    
    def all_cohorts(self):

        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])
           
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name   
            from Cohort c """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)
    
    def all_exercises(self):

        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercises(row[1], row[2])
           
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.Language   
            from Exercise e """)

            all_exercises = db_cursor.fetchall()

            for exercises in all_exercises:
                print(exercises)
    
    def all_students_and_exercises(self):
        exercises = dict()

        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            # conn.row_factory = lambda cursor, row: All_Students_And_Exercises(row[1], row[2])
           
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
	        e.Id ExerciseId,
	        e.Name,
	        s.Id,
	        s.First,
	        s.Last
            from Exercise e
            join Assignment se on se.ExerciseId = e.Id
            join Student s on s.Id = se.StudentId """)

            all_students_and_exercises = db_cursor.fetchall()

            for row in all_students_and_exercises:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)
                    

            for exercise_name, students in  exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')
            
            for row in all_students_and_exercises:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if student_name not in exercises:
                    exercises[student_name] = [exercise_name]
                else:
                    exercises[student_name].append(exercise_name)
                    

            for student_name, exercises in  exercises.items():
                print(student_name)
                for exercise in exercises:
                    print(f'\t* {exercise}')

            

reports = StudentExerciseReports()
reports.all_cohorts()
reports.all_instructors()
reports.all_students()
reports.all_exercises()
reports.all_students_and_exercises()
        
    
    
