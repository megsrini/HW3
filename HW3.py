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
    def most_common(self,n):
        self.fortunes_history_list = []
        count_yes = 0 
        count_no = 0 
        count_askagain = 0 
        count_maybe = 0
        count_notclear = 0 
        for i in range(n):
            self.get_fortune()
        for i in range(len(self.fortunes_history_list)):
            if self.fortunes_history_list[i] == 0: 
                count_yes+= 1
            elif self.fortunes_history_list[i] == 1: 
                count_no+=1
            elif self.fortunes_history_list[i] == 2: 
                count_askagain+=1
            elif self.fortunes_history_list[i] == 3: 
                count_maybe+=1
            elif self.fortunes_history_list[i] == 4: 
                count_notclear+=1
        count = 0 
        num = self.fortunes_history_list[0]
        for i in self.fortunes_history_list:
            current = self.fortunes_history_list.count(i)
            if current > count:
                count = current 
                num = i
        if num == 0: 
            output = "Yes"
        if num == 1: 
            output = "No"
        if num == 2: 
            output = "Ask again"
        if num == 3: 
            output = "Maybe"
        if num == 4: 
            output = "Not clear"
        print("Yes: "+ str(count_yes))
        print("No: "+str(count_no))
        print("Ask again: "+str(count_askagain))
        print("Maybe: "+str(count_maybe))
        print("Not clear: "+ str(count_notclear))
        print("The most frequent answer after " +str(n)+ " was "+ output)

def main():
    fortunes_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]
    bot = Fortune_Teller(fortunes_list)
    while True: 
        question = input("Ask a question or type quit : ")
        if question == 'quit':
            break
        else:
            #bot.question_check(question)
            print(question + " - " + bot.question_check(question))
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
    print("Testing most_common method with 200 responses")
    bot2.most_common(200)


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    test() #TODO: Uncomment when you are ready to test your Fortune_Teller class