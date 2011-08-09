class iterableString(str):
    """
    Adds a new next() method to str class
    Use only next(), not other methods.
    """
    
    def replaceCharInString(self,index,new):
        """Replaces a char in string on the given position"""
        s = list(self)
        s[index] = new
        return iterableString("".join(s))

    
    def icrementString(self,x):
        """Icrements the string by one.
        aaab becomes aaac
        aaaz becomes aaza"""

        #Get char position
        currentCharIndex = x * -1
        
        #Icrement that char by one
        nextCharValue = chr(ord(a[currentCharIndex])+1)
       
        #If the icremented char is "z"+1, replace current position with "a"
        #Then check previous characters
        if nextCharValue == chr(ord("z")+1):
            self = self.replaceCharInString(currentCharIndex,"a")
            x += 1
            return self.icrementString(x)
        
        #Else, replace current position with icremented char
        else:
            self = self.replaceCharInString(currentCharIndex,nextCharValue)
            return self
        
        
    def next(self):
        """Returns a new icremented string"""
        # If the string is full of "z"'s, return a string full of "a"'s
        if self == "z" * len(self):
            self = "a" * (len(self) +1)
            return self
        # Else try to icrement the string
        else:
            return self.icrementString(1)



 
