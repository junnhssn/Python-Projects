def marks():
    print("Enter your English, Science and Math scores : ")
    x, y, z = map(int, input().split())
    res = x + y + z
    return res
    
    
    
def class_declaration(x):
    if 90 <= x < 100 :
        print("Congratulations, you have obtained a first class with", x, "%")
        
    elif 75 <= x < 90 :
        print("Congratulations, you have obtained a second class with", x, "%")
    
    elif 35 < x < 75 :
         print("Congratulations, you have obtained an average class with", x, "%")
    
    elif 0 < x <= 35 :
        print("Unfortunately, you have failed with", x +"%")
    
    else :
        print("Please enter the correct marks")
    
    
    
    
def main():
    marks_scored = marks()
    total_marks = 270
    percentage = (marks_scored/total_marks)*100
    class_declaration(percentage)
    
#main starts here
main()
    
    
    
    
    
    