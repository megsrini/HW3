# Your name: Meghana Srinivasa
# Your student id: 8023 9297
# Your email: megsrini@umich.edu
# List who you have worked with on this homework:

# import the random module for use in this program
import random
class Fortune_Teller:
    def __init__ (self, fortunes_list):
        self.fortunes_list = fortunes_list
        questions_list= []
        self.questions_list = questions_list
        fortunes_history_list = []
        self.fortunes_history_list = fortunes_history_list
    def __str__(self):
        return str(self.fortunes_list)
    def get_fortune(self):
        random_picks = random.randint(0,(len(self.fortunes_list)-1))
        self.fortunes_history_list.append(random_picks)
        return self.fortunes_list[random_picks]
    def question_check(self, question):
        if question in self.questions_list:
            return "I've already answered that question"
        else:
            self.questions_list.append(question)
            return self.get_fortune()
    def print_questions_history(self):
        if len(self.fortunes_history_list) == 0:
            print("None yet")
        else: 
            for i in range(len(self.fortunes_history_list)):             
                print("["+str(self.fortunes_history_list[i])+"] " + self.questions_list[i]+ " - "+ self.fortunes_list[self.fortunes_history_list[i]])

# Create the class Fortune_Teller

    # EXTRA POINTS
    # create the most_frequent method
    # it takes as input:
    #   a number, n. Ex: 200
    # it generates a random response n times by calling get_fortune
    # It prints the counts for each answer and
    # prints the most frequently occurring answer (Do not use a dictionary in this solution):
    #   Yes: 36
    #   No: 36
    #   Ask again: 48
    #   Maybe: 38
    #   Not clear: 47
    #   The most frequent answer after 200 was Not clear

def main():
    fortunes_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]
    bot = Fortune_Teller(fortunes_list)
    while True: 
        question = input("Ask a question or type quit : ")
        if question == 'quit':
            break
        else:
            bot.question_check(question)
            print(question + " - " + bot.get_fortune())
            continue

def test():

    fortunes_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]

    print()
    print("Testing Fortune Teller:")
    bot2 = Fortune_Teller(fortunes_list)

    print("Testing the __str__ method")
    print(bot2)
    print()

    print("Printing the history when no answers have been generated yet")
    bot2.print_questions_history()
    print()

    print("Asking the Question: Will I pass this semester?")
    print(bot2.question_check("Will I pass this semester?"))
    print()

    print("Asking the Question: Should I study today?")
    print(bot2.question_check("Should I study today?"))
    print()

    print("Asking the Question: Should I study today? (again)")
    print(bot2.question_check("Should I study today?"))
    print()

    print("Asking the Question: Is SI 206 the best class ever?")
    print(bot2.question_check("Is SI 206 the best class ever?"))
    print()

    print("Printing the history")
    bot2.print_questions_history()
    print()

    #EXTRA POINTS
    #Uncomment the lines below if you attempt the extra credit!
    # print("Testing most_common method with 200 responses")
    # bot2.most_common(200)


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    test() #TODO: Uncomment when you are ready to test your Fortune_Teller class