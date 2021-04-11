#Alyssa McCurdy - COP 1500 - Integration Project 

#I will be writing my integration project over ADHD because I find it interesting and an important subject to talk about.
    #A lot of people will get distracted more than usual and then say they have ADHD/ADD wihtout actually going in for a proper test.
    #It puts out a bad stigma around ADHD and it makes people believe it is not as bad as it seems. For this project I want
    #to explain how ADHD affects the brain and society as a whole. I also picked this subject because no one has ever told me
    #to "embrace" my ADHD and that *really* stuck with me. So I decided to create a program that can educate others about ADHD. :)

#I broke up different sections of work with lines so it would be easier for me to read the code and not feel overwhelmed,
    #but I am making sure to include extra lines of code to make sure I meet the minimum. I just tend to overwhelm my eyeballs.

#I am going to be attaching a document to all the websites I used as well as labeling in the code.
    #All works cited comments will be in parentheses 


import random
randomNum = random.randint(7,332785651)

def populationRandom(randomNum):
    percentInput = int(input("Please enter an integer between 1 and 100 for the percentage: "))
    percentAsPercent = percentInput / 100
    print(" ")
    print("The number you picked was " + str(percentAsPercent))
    print("The number the machine choose was " + str(randomNum))
    print(" ")
    randomPeople = randomNum / percentAsPercent
    print("That means that " + str(format(randomPeople,'.0f')) + " people would have ADHD!")
    while True:
        if randomPeople > population05:
            print("Wow! That's even more than before!")
            break

            
#(BetterHelp) for the .txt file
def adhdFunctionList7():
    adhdList7 = open('SevenTypesOfADHD.txt')
    for index in range(1,8):
        adhdL7 = adhdList7.readline()
        print(str(index) + " ",adhdL7.rstrip())


#(HealthLine) for the .txt file
def adhdFunctionList3():
    adhdList3 = open('ThreeTypesOfADHD.txt')
    for index in range(1,4):
        adhdL3 = adhdList3.readline()
        print(str(index) + " ",adhdL3.rstrip())


print("Hello User!")
name = input("What is your name?: ")

#The next line is just to add a line between sections of work for a better look when the program is ran.
print(" ")
print("Hello, " + name + "! Welcome to Alyssa McCurdy's Integration Project for COP 1500! Please maximize the screen for a better experience!")
print("Today, we will be learning about ADHD, its effects, and how occuring it is in today's society.")
print(" ")
print("DISCLAIMER: The creator of this program is in no way, shape, or form a liscensed psychiatrist, but instead educates about ADHD from a personal experience and with in-depth research.")
print(" ")
print("Before we start off, it is important to note that ADHD and ADD are the same condition. The only difference is that one includes hyperactivity (adHd) while the other does not (add).") 
print("Now that we have that out of the way, let's talk about how many people in the USA are affected by ADHD!")
print(" ")

while True:
    YesNo = input("Are you ready to learn about ADHD/ADD? (Yes/No): ")
    if YesNo == "yes" or YesNo == "Yes":
        print("Awesome! Let's go!")
        break
    if YesNo == "no" or YesNo == "No":
        print("Too bad! The show must go on!")
        break
    else:
        print("What?")

print(" ")
#(Next line: Population USA = 332,785,650 / CBS News = 4-5%)
print("In the year 2020, the USA had a population of roughly 332,785,650 people. ADHD affects a MINIMUM of 4-5% of people in America.")

#(Population USA) 
population04 = 332785650 * .04
population05 = (332785650 * .05)
#The previous two lines are taking 4% and 5% of the 2020 USA population for the next lines of code to show how many in the USA have ADHD
population05 += 1
population05 = int(population05)
#Previous lines make it so the number can be 'rounded up' to the next number so that the 'int' function can act as a way of rounding it back down to what its supposed to be rounded to

population04_string = str(population04)
population05_string = str(population05)
print("That is a minimum of " + population04_string + " to " + population05_string + " people in the United States that have ADHD.")

population96 = 332785650 - population04
population95 = 332785650 - population05
population96_as_string = str(population96)
population95_as_string = str(population95)

print("That leaves roughly " + population95_as_string + " to " + population96_as_string + " people without ADHD.")

#(Next line: CBS News)
print("Of the adults out of the group who do have ADHD, 90% of them go undiagnosed and unmedicated.")
print("Many wonder how this is possible, but it is quite a simple answer, " + name + ". For starters, ADHD comes in different levels of intensity.")
print("Some may have low functioning ADHD and not even realized it.")
print("Another reason is because having ADHD does not mean you just get easily distracted.")
print("There are actually a couple different types of ADHD that all affect people differently.")
print(" ")

#(MedicalNewsToday & HealthLine) for the sources saying 3 types
#(CBS News & BetterHelp) for the sources saying 7 types
print("ADHD and ADD are often referred to as having 'types', 'forms', or 'subtypes'. This is debated amongst scientist because while some may say ADHD/ADD does have types, others say referring to ADHD/ADD as having 'types' is just a way to group symptoms that appear together.")
print("There is also a debate on the number of types of ADHD/ADD. Some say 3 while others say - well, why dont you guess!")
print(" ")

while True:
    adhdGuess = input("Can you guess how many types some say there are? (I'll give you a hint!: " + "ADHD " * 7 + "): ")
    if adhdGuess == "7" or adhdGuess == "seven" or adhdGuess == "Seven":
        break
    if not adhdGuess == "7" or adhdGuess == "seven" or adhdGuess == "Seven":
        print("No, that's not right! Try again! :)")
#The previous lines are to add a little bit of 'fun' to the project experience!
print(" ")

#(BetterHelp & ADDitideMag)
print("Correct, Some say there are 7 types of ADHD!")
print("This includes Classic ADHD, Inattentive ADD, Overfocused ADHD, Temporal Lobe ADHD, Limbic ADHD, Ring of Fire ADHD, and lastly, Anxious ADHD.")
print(" ")

#calling back to def adhdFunctionList(): funtion to displaythe list of ADHD types
adhdFunctionList7()
print(" ")
      
print("One single person can have only one type of these ADHDs, but it is also possible to have multiple (or all) types of ADHD.")
print(" ")

#The upcoming lines are for some math fun just to see what the numbers would look like if each type of ADHD could only affect a certain amount of people.
print("Now let's have some fun with these numbers!")

while True:
    continueON = input("Type GO to do some fun math!: ")
    if continueON == "go" or continueON == "Go" or continueON == "GO":
        break
    if continueON != "go" or continueON != "Go" or continueON != "GO":
        print("That's not how you spell GO, " + name + "! Try again!")
print(" ")

print("Theoretically, let's say you could only have one type of ADHD and the number of people with that type of ADHD is equal to the rest.")
print("How many people would have each type of ADHD? Well, " + name + ", let's see!")
print("16,639,283 // 7 = ", 16639283 // 7)

adhdPop= 16639283 // 7
adhd_pop_string = str(adhdPop)
adhdPopleft = 16639283 % 7
pop_left_string = str(adhdPopleft)
      
print("That would make it so one type of ADHD would affect " + adhd_pop_string + " people with a remainder of " + pop_left_string + " people left to be categorized with those")
print("that do not have ADHD.")
print(" ")
print("Now let's say that EVERYONE had ADHD! How many people would be in each group now, " + name + "?")
print("Let's do some more math to figure it out!")
print("332,785,650 / 7 = ", 332785650 / 7)
print("That would make it roughly 47,540,808 people with each type of ADHD! That's crazy!")
print(" ")
print("Now let's say the population in the United States was magically squared over night! How many people would have ADHD then?")

popSquaredADHD = 332785650 ** 2 // 7
pop_squared_string = str(popSquaredADHD)

print("(332,785,650 ** 2) // 7 = ", pop_squared_string)
print("Woah! That would be about " + pop_squared_string + " people for each type of ADHD!")
print(" ")

print("Now let's try something new! We are going to let the program randomly decide on a number between 7 and 332875650 for the population and you, " + name + ", can pick a number to represent the percentage of that randomly generated number that have ADHD!")
print(" ")

#Call back to function
populationRandom(randomNum)
print(" ")

print("I think we can both agree that both are a lot of people!")
print(" ")

print("BUT we can't forget about those who say there are only 3 forms of ADHD/ADD. These three groups break down ADHD/ADD into a much simpler terms as far as descriptions.")
print(" ")
print("The 3 types are known as: ")
#Call back to function
adhdFunctionList3()
print(" ")

print("Inattentive ADHD include the symptoms listed previously such as lack of attention, distractability, and forgetfulness.")
print("Hyperactive-impulsive ADHD is said to be the least common type and comes with the symptoms found in the name (hyperactivity and impulsive behavior).")
print("Combined ADHD is the most common type out of these three. As the name implies, it is a combination between Inattentive and Hyperactive-impulsive ADHD. This form of ADHD comes with all the previously listed symptoms.")
print(" ")

print("Let's review this one more time.")

while True:
    threeTypes = input("What is the lower number of 'types' of ADHD/ADD? (Please use an integer): ")
    sevenTypes = input("What's the higher amount? (Please use an integer): ")
    if threeTypes == "3" and sevenTypes == "7":
        print("That is correct! The discussing is between 3 and 7 types!")
        break
    else:
        print("No, thats not right.")
print(" ")

print("New research and information about ADHD/ADD is slow survicing, but it is still important to educate yourself about the existing information to help better understand those around you!")

print("Thank you, " + name + ", for using our program to learn more about ADHD/ADD! I hope this program has inspired you to learn more about the illness and to help educate others as well!")
print(" ")

while True:
    redirect = input("Would you like to be directed to the Works Cited? (Yes/No): ")
    if redirect == "No" or redirect == "no":
        break
    if redirect == "Yes" or redirect == "yes":
        print(" ")
        print("   Works Cited:")
        print(" ")
        print("        Do You Have ADHD--Or Are You Just Easily Distracted? | CBS News")
        print("              -  https://www.cbsnews.com/news/do-you-have-adhd-or-are-you-just-easily-distracted/")
        print(" ")
        print("        What Are The 7 Types Of ADHD? | Betterhelp")
        print("              -	https://www.betterhelp.com/advice/adhd/what-are-the-7-types-of-adhd/")
        print(" ")
        print("        What is Inattentive ADHD? ADD Symptoms, Causes, Treatment | ADDitudemag")
        print("              -	https://www.additudemag.com/slideshows/symptoms-of-inattentive-adhd/")
        print(" ")
        print("        3 types of ADHD: What are the differences? | MedicalNewsToday")
        print("              -	https://www.medicalnewstoday.com/articles/317815")
        print(" ")
        print("        What Are the Three Types of ADHD? | HealthLine")
        print("              -	https://www.healthline.com/health/adhd/three-types-adhd")
        print(" ")
        print("        Population of USA 2021 | USAPopulation")
        print("              -	https://www.usapopulation.org/#:~:text=US%20Population%202021%20United%20States%20of%20America%20(U.S.A.),largest%20country%20with%20size%20of%209.834%20million%20km%C2%B2.")
        break
    else:
        print(" ")


