def isMobileValid(str): 
    if len(str)==10:
        if str.isdigit():
            return True
        else:
            return False
    else:
        return  False


def isNameValid(str):
    ##str = input("Enter your name::")
    l=str.split()
    ##print(l)
    for i in l:
        if i[0].isalpha() and i[1:].isalpha():
            continue
        else:
            return False    
    return True

def isPanValid(str):
    ##str = input("Enter your pan no::")
    if len(str)!=10:
        return False
    for s1 in str[:5]:
        ##s1=str[:5]
        if not s1.isalpha():
           return False
    for s2 in str[5:9]:
        ##s2=str[5:9]
        if not s2.isdigit():
            return False
    for s3 in str[9]:
        ##s3=str[9]
        if not s3.isalpha():
            return False
    else:       
            return True

def isEmpidValid(eno):
    if len(eno)==6 and eno.isdigit():
        return True
    else:

        return False
    
def isDobValid(d):
    ##d = input("Please enter your dob (dd/mm/yyyy)::")
    if len(d)==10:
        d1=d[:2]
        d2=d[2]
        d3=d[3:5]
        d4=d[5]
        d5=d[6:]
        if not d1.isdigit():
            return False
        if not d2 =='-':
            return False
        if not d3.isdigit():
            return False
        if not d4 =='-':
            return False
        if not d5.isdigit():
            return False
        
        return True

def isSalValid(sal):
    if sal.isdigit():
        if not len(sal)>=5:
            return False
        return True

def isAgeValid(age):
    ##age = input("Enter your age::")
    if age.isdigit() and len(age)==2:
        a = int(age)
        if not a>=18 and a<=58:
            return False

        return True
    
def isAdharValid(adn):
    ##adn= input("Enter your Adhar::")  
    if  len(adn)!=12:
        return False
    if not adn.isdigit():
        return False
    else:
        return True

  
