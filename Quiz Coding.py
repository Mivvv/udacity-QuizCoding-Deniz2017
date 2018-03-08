#######################################
#          Deniz Alp Atun             #
#            07.10.2017               #
#Udacity // Code Your Own Quiz Project#
#######################################



### Quizes ###

EASY_quiz = """A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.""" #given as an example from IPDN resources

MEDIUM_quiz = """Duke Nukem 3D is a game which is released in ___1___ and developped by 3D Realms.
Among with Wolfeinstein 3D and Doom, Duke Nukem 3D is considered to be one of the games that popularized ___2___ genre.
The game starts in ___3___, where aliens have invaded the city and mutated the LAPD. After going through ___3___,
Duke journeys through the space, to save all the captured women. After killing an Alien Overlord, he finds out that all the
kidnapping was a ruse to distract him from protecting the Earth. Thus in his final act, he returns to ___3___ to defeat the
alien invasion and their leader!

Duke Nukem has been voiced by ___4___ and his character persona is
a collection of cult cinema classics, such as ___5___ from Die Hard, Harry Callahan from ___6___.
These examples could be listed further, but instead watch the episode of Game Theory on youtube."""

HARD_quiz = """Wade Wilson's early life is mostly unknown.
His mother died of cancer while he was young and his father (who was in the military) was physically abusive.
Wade was a deliquent in his teenage years, possibly to spite his father.
However one night while drinking with his friends his father attempt to take him out of the club
one of his friends stole Wade's Fathers handgun and killed him. Following a brief stint of military service,
Wade began his ___1___ career while still in his late teens. Accepting assassination jobs only against
those whom he felt deserved death, he made a habit of using plastic surgery and technology to take on a new identity
whenever he failed an assignment. Many years later ___2___'s nemesis T-Ray accused ___2___ of killing his wife
and stealing his identity after a failed mission, but ___2___'s restored memories revealed this to be a lie;
in T-Ray's account Wade was wearing his ___2___ costume, which he didn't have in till after he joined Weapon X.\n

During one mission, Wilson killed his teammate ___3___. As a result, he was rejected from the Weapon X Program and sent to the Hospice,
allegedly a government facility where failed superhuman operatives were treated.
However, unknown to the Canadian government, the Hospice's patients served as experimental subjects for
Doctor ___4___ and his sadistic assistant Ajax, with the patients placing bets in a "___2___"
as to how long each subject would live. ___4___ subjected Wilson to various torturous experiments
for his own deranged satisfaction. In due course, Wilson formed a semi-romantic relationship with the cosmic entity ___5___,
who regarded him as a kindred spirit. Wilson's emotional strength during his trials earned him the respect of his fellow
Hospice patients. Then Ajax, angered by Wilson's taunts, lobotomized one of Wilson's friends. At ___5___'s prompting,
Wilson killed his friend to end his suffering. However, under ___4___'s rules any patient who killed
another was to be executed; Ajax subsequently tore out Wilson's heart and left him for dead, but
Wilson's thirst for vengeance was so strong that it jumpstarted his healing factor, regenerating
his heart, although not curing his scarred body. Wilson then attacked Ajax, leaving him for dead in turn, and,
taking the name ___2___, escaped from the Hospice with his fellow patients""" #deadpool from marvel wiki

### List of blanks and answers to quizes ###

blanks = ["___1___","___2___","___3___","___4___","___5___","___6___"]

answer_list = [["function","parameters","nothing","list"],
               ["1996","fps","los angeles","jon st. john","john mcclane","dirty harry"],
               ["mercenary","deadpool","slayback","killebrew","death"]]

### Functions ###


def difficulty_input():
        # returns lowered input for comparison with difficulties. #
        # function input => none
        # function prompts user to type in an input
        # function output => lower cased input
        selection_input = raw_input("Type in your selection:")
        selection = selection_input.lower()
        return selection


def difficulty_selection(selection):
        # compares input with difficulty index. #
        # function input => string
        # function compares input with difficulty index
        # if input is found in difficulty index
        # function output => corresponding difficulty
        # if not found
        # function output => error message and returns "error"
        index = 0
        while selection != difficulty[index]:
                if index == 3:
                        print "INVALID INPUT, try again\n"
                        return "error"

                index = index + 1
        return difficulty[index]


def word_in_pos(word,blanks):
        # determines wheter the word contains a blank or not. #
        # returns blank if it is, else returns none. #
        # function input => (string,string)
        # if word contains blank
        # function output => corresponding blank
        # if word does not contain blank
        # function output => None
        if blanks in word:
                return blanks
        
        return None


def answer_filler(quiz,blanks,answer_quiz):
        # main function, it fills in the blanks and prints out the results. #
        # function input => (string,list1,list2)
        # first function splits the string(quiz) (turns it into a list, quiz_split)
        #1 then checks each entitiy from quiz_split whether they are blank or not
        # it does that by checking blanks in their list order.
        # if the current blank is found, prompts user to input an answer
        # answer is then checked with list2(answer_quiz)
        # if input answer is true, current blank is replaced by corresponding answer
        # and prints out "correct answer" and on a new line, prints the new quiz
        # with corresponding blanks replaced with the answer
        #8 if input is false, user is prompted to try again
        # then  #1-#8 repeats until there are no more blanks (which is satisfied by length of answers
        inc1 = 0
        glue = " "
        quiz_split = quiz.split(" ")
        for word in quiz_split:
                if inc1 < len(answer_quiz):
                        dummy = word_in_pos(word,blanks[inc1])
                        if dummy != None:
                                inc2 = False
                                while inc2 == False:
                                        answer_in = raw_input("What is the answer for" +dummy +": ")
                                        answer_check = answer_in.lower()
                                        if answer_check == answer_quiz[inc1]:
                                                inc2 = True
                                                quiz_split = [w.replace(dummy,answer_check) for w in quiz_split]
                                                #found above nice code from stackoverflow, it replaces all blanks in a simpler coding.
                                                print "Correct Answer!\n"
                                                print glue.join(quiz_split)+"\n"
                                                inc1 = inc1 + 1
                                        
                                        else:
                                                print "Wrong Answer, try again!\n"



### Main Code ###

print "Select a difficulty:"
print "EASY - MEDIUM - HARD\n"

difficulty = ["easy","medium","hard","error"]
select = "error"


while select == "error":
        select = difficulty_input()
        select = difficulty_selection(select)

if select == "easy":
        quiz = EASY_quiz
        answer_quiz = answer_list[0]
        print EASY_quiz +"\n"
        answer_filler(quiz,blanks,answer_quiz)
        
if select == "medium":
        quiz = MEDIUM_quiz
        answer_quiz = answer_list[1]
        print MEDIUM_quiz +"\n"
        answer_filler(quiz,blanks,answer_quiz)

if select == "hard":
        quiz = HARD_quiz
        answer_quiz = answer_list[2]
        print HARD_quiz +"\n"
        answer_filler(quiz,blanks,answer_quiz)


