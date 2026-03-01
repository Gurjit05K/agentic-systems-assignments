class StudentMarks:
    def __init__(self, marks_list):
        self.marks = marks_list
    
    def last_three_avg(self):
        try:
            if len(self.marks) < 3:
                raise ValueError("Not enough marks to calculate average")
            last_three = self.marks[-3:]
            average = sum(last_three) / len(last_three)
            print(f"Average of last 3 marks is: {average}")
        except ValueError as e:
            print(e)

# Test the class
if __name__ == "__main__":
    marks = [50, 60, 70, 80, 90]
    student = StudentMarks(marks)
    student.last_three_avg()