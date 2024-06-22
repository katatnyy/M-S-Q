#-------------------------------------
def new_game(): 
    gusses =[]
    correct_gussess = 0 
    ask_num = 1

    for key in ask :
        print("-------------------------------------")
        print(key)
        for i in answer[ask_num -1] :
            print(i)
        guess = input("enter (A ,B ,C ,D ): ")
        guess=  guess.upper()
        gusses.append(guess)
        correct_gussess +=check_answer(ask.get(key), guess) 
        ask_num +=1
    display_source(correct_gussess, gusses)
#-------------------------------------
def check_answer (anwser , guess):
    if anwser == guess :
        print("correct !")
        return 1 
    else :
        print("wrong ")
        return 0 
#-------------------------------------
def display_source(correct_gussess, gusses) :
    print("-------------------------------------")
    print("results")
    print("-------------------------------------")
    print("answer : ", end="")
    for i in ask : 
        print(ask.get(i), end="")
    print()

    print("gusses  : ", end="")
    for i in gusses : 
        print(i , end=" ")                       #        print(gusses.get(i), end=" ")  wrong code 
    print()
    scor = int((correct_gussess/len(ask))*100)
    print("your scor is "+str(scor)+ (" %"))
#-------------------------------------
def play_again () :
    respons = input("do u want play again ? (YES OR NO ) :  ")
    respons= respons.upper
    if respons == ("yes"): 
        return True
    else:
        return False









ask = {"tell me about musles ?":"A" ,
       "what u know about training ?":"B",
       "what is your know about nutration ?":"B"}

answer = [["A.bicep","B . tricep ","C . femur ","D . lat"],
          ["A . sales ","B . stoall ","C . help ","D . think"],
          ["A . meat ","B . carb","C . fat","D . darty food"]]


new_game()

while play_again():
    new_game()
print("byeeeeeeeeeeee")
