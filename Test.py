import json
testfile = json.load(open("Test.json"))

#dict={ "Name":x ,"DOB": y }
word= input("The word to check: ")
def check(d): 
    return testfile[d]
print(check(word))