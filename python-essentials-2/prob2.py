class StudentScores:
    def __init__(self, scores_list):
        self.scores = scores_list
    
    def highest_last_two(self):
        try:
            if len(self.scores) < 2:
                raise ValueError("Not enough scores to find highest value")
            last_two = self.scores[-2:]
            highest = max(last_two)
            print(f"Highest score among last two is: {highest}")
        except ValueError as e:
            print(e)

# Test the class
if __name__ == "__main__":
    scores = [45, 67, 89, 72]
    student = StudentScores(scores)
    student.highest_last_two()