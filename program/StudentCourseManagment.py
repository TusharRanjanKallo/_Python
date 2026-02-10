class Student:
    def __init__(self,student_id,name):
        self.student_id=student_id
        self.name=name
        self.courses=[]
        self.marks={}
        self.avg=int()
    
    def enroll(self,course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            pass
    
    def add_marks(self,course,mark):
        if course in self.courses:
            self.marks[course]=mark
        
    def average(self):
        if not self.marks:
            return 0
        sum=0
        for v in self.marks.values():
            sum+=v
        avg=sum/len(self.marks)
        return avg
    def __str__(self):
        return f"{self.student_id} | {self.name} | {self.marks}"
    

class CourseManager:
    def __init__(self):
        self.students=[]
    
    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)
    def find_student(self,id):
        for s in self.students:
            
            if id == s.student_id:
                return s
        return None
    def topper(self):
        if not self.students:
            return None
        top_student=None
        top_avg=-1
        for s in self.students:
            avg = s.average()
            if avg > top_avg:
                top_avg=avg
                top_student=s

        return top_student
    def summary(self):
        
        total_students=len(self.students)
        #students per course
        spc={}             
        for s in self.students:
            for course in s.courses:
                if course in s.marks.keys():
                    spc[course]=spc.get(course,0)+1
                else:
                    pass
        top=self.topper()
        print("Summary of Students")
        print("-------------------")
        print(f"\nTotal Students:{total_students}")
        print("Students in each course:")
        for k,v in spc.items():
            print(f"{k}:{v}")
        if not top :
            print("No topper")
        else:
            print(f"Class topper: {top.name} ({top.average():.2f})")

        












s1 = Student(1, "Aman")
s2 = Student(2, "Riya")

s1.enroll("Python")
s1.enroll("DSA")
s1.add_marks("Python", 85)
s1.add_marks("DSA", 90)

s2.enroll("Python")
s2.add_marks("Python", 95)

cm = CourseManager()
cm.add_student(s1)
cm.add_student(s2)



cm.summary()
print(cm.find_student(1))
print(cm.find_student(99))