class StudentPerformance:
    def __init__(self, scores_list):
        self.scores = scores_list
    
    def score_difference(self):
        try:
            if len(self.scores) == 0:
                raise ValueError("No scores available to calculate difference")
            first_score = self.scores[0]
            last_score = self.scores[-1]
            difference = last_score - first_score
            print(f"Difference between last and first score is: {difference}")
        except ValueError as e:
            print(e)

# Test the class
if __name__ == "__main__":
    scores = [55, 65, 75, 85]
    student = StudentPerformance(scores)
    student.score_difference()