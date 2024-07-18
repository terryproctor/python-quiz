from data import question_data

class Question:
    def __init__(self, question, answer):
        self.text = question
        self.answer = answer
 
    def get_question(self):
        return self.text

    def get_answer(self):
        return self.answer
    
class QuizBrain:
    score = 0

    def __init__(self):
        question_bank = []

        for qa in question_data:
            #print(qa["text"])
            new_question = Question(qa["text"], qa["answer"])
            question_bank.append(new_question)

        self.question_number = 0
        self.question_list = question_bank

    def next_question(self):
        self.question_number += 1
        return input(f"Q.{self.question_number}. {self.question_list[self.question_number - 1].get_question()}. True/False): ").upper()

    def still_has_questions(self):
        return self.question_number < (len(self.question_list))
    
    def start(self):
        while self.still_has_questions():
            user_answer = self.next_question()
            self.check_answer(user_answer, self.question_list[self.question_number - 1].get_answer())
        print("You've completed the quiz.")
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print("The correct answer was: ", correct_answer)
        print(f"Your current score is: {self.score}/{self.question_number}")


        

# print(question_bank[-1].text)
# print(question_bank[-1].answer)
quiz = QuizBrain()
quiz.start()