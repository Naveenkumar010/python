import json
from difflib import get_close_matches

testfile = json.load(open("Test.json"))

#dict={ "Name":x ,"DOB": y }
word= input("The word to check: ")
def check(d):
    d= d .lower()
    if d in testfile:  
        return testfile[d]
    elif len(get_close_matches(d,testfile.keys()))>0:
        choice =input( "Did you mean %s !?, I yes='Y';No='N' "%get_close_matches(d,testfile.keys())[0])
        if choice=="Y"or"y" : 
            return testfile[get_close_matches(d,testfile.keys())[0]]
        elif choice== "N"or"n":
            return "The Word dosen't EXIST,enter the CORRECT Word"
        else:
            return "you have entered the Wrong Choice"
    else:
        return "The Word dosen't EXIST,enter the CORRECT Word"    

Report=(check(word))
if type(Report) == list:
    for i in  Report:
        print(i)
else:
    print(Report)
