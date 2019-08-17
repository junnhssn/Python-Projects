def math_score():
    math  = int(input("Enter your Math marks : "))
    return math

def english_score():
    english  = int(input("Enter your English marks : "))
    return english 

def science_theory():
    sci_th  = int(input("Enter your Science theory marks : "))
    return sci_th

def science_practical():
    sci_pra  = int(input("Enter your Science practical marks : "))
    return sci_pra
   
    
def class_declaration(p,m,e,s1,s2):


    if 90 <= p < 100 and m > 35 and e > 25 and s1> 8  and s2 >25 :
        print("Congratulations, you have obtained an A grade with", p,"%")



    elif 75 <= p < 90 and m > 35 and e > 25 and s1> 8  and s2 >25 :
        print("Congratulations, you have obtained a B grade with", p,"%")


    elif 35 <= p < 75 and m > 35 and e > 25 and s1> 8  and s2 >25 :
        print("Congratulations, you have obtained a B grade with", p,"%")

    else :
        print("Unfortunately you have failed")



def percentage(m,e,s1,s2):
    
    total_marks = 275 
    total_scored = m + e + s1 + s2
    percentage = (total_scored/total_marks)*100
    return percentage

    
def main():
    math = math_score()
    english = english_score()
    science_1 = science_practical()
    science_2 = science_theory()
    percentage(math,english,science_1,science_2)
    class_declaration(percentage,math,english,science_1,science_2)
        
#main starts here       
main()       
        
        
        
        
        