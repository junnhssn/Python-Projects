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
    

def main():
    total_marks = 275
    math = math_score()
    english = english_score()
    science_1 = science_practical()
    science_2 = science_theory()
    total_scored = math + english + science_1 + science_2
    percentage = (total_scored/total_marks)*100
    if 90 <= percentage < 100 and math > 35 and english > 25 and science_1> 8  and science_2 >25 :
        print("Congratulations, you have obtained an A grade with", percentage,"%")
        
        
        
    elif 75 <= percentage < 90 and math > 35 and english > 25 and science_1> 8  and science_2 >25 :
        print("Congratulations, you have obtained a B grade with", percentage,"%")
        
        
    elif 35 < percentage < 75 and math > 35 and english > 25 and science_1> 8  and science_2 >25 :
        print("Congratulations, you have obtained a B grade with", percentage,"%")
        
    else :
        print("Unfortunately you have failed")
        
        
#main starts here        
main()       
        
        
        
        
        