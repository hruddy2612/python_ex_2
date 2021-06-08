# Python refresher exercises 2 - task 2

# - as part of some app, the user has to create a valid email address
# - any address will do as long as it's valid
# - your validation will only allow a number of retries if a invalid email is given (default 3)
# - once the number of attempts is exhausted (you should show how many retries are left!), set the
#   variable (flag) gave_up to True and bail out.
# 
# - it's OK to start with my solution from the lecture in flow control, although I 
#   encourage you to try you own solution first (if you can't remember). Any other, working
#   solution is fine, too!
# - when it comes to how to react to an error, your user MUST re-enter a string, but it's up to 
#   you how helpful you want to be:
#   - you could just list all the rules on error and demand a new input
#   - you could list the appropriate error message returned from you function and demand a new input
#   - you could do something fancy and only require re-typing of what's wrong (if that's technically possible):
#       e.g. if the pre @ is wrong (too long, contains a invalid char) you could demand that
#       only that incorrect part is re-entered. Warning - this can be complicated and laborious to test!
# - Note that the check for a valid email is a bit weird (b/c of how I set it up):
#   - iff the first return is None (r == None), the email is valid (yes, None doesn't sound like an OK ...)
#   - if you didn't get None (r != None), then r contains an error code, which you could use in your 
#     flow control for branching, if you want to do something fancy

# Optionally, you can use regex for all this!

# Once you're solved this, run some tests to show me that it works. 
# Again, manually copy/paste the console output in a text file (results2.txt)



# import your function from the previous .py file as a module (you can abbreviate it)
# use ex_2_task_2 here instead once your function works!

def is_valid_email_address(s):
    s = "hruddy@iastate.edu" 

    is_valid_email_address (s)

    #how many characters in A (characters before the @)
    A = s.split("@")
   
    if len(A) < 3 or len(A) >16: # A needs to be within 3-16 characters, if outside the range, an error occurs
        print ("error 1")
    else:
        print ("ok") #the character amount is ok 

    
    #how many characters in B (after the @ but before the '.') I don't know how to get B out of the string.
    B = s.split (".")
    if len(B) <2 or len(B) >8:
        print ("error 2")
    else print ("ok")

    #is C one of the correct endings?

    # I don't know how to check if the email ends in comm, edu, org, gov
    # I also do not understand how return function works. I have looked through lecture notes/videos and
    #I have watched additional youtube videos and I don't understand it. I will try to set up a meeting with you Monday. 
    #I also looked through your solutions and I don't follow them. 

    for each email: #This is not correct code, but I am not sure how to write this
        if there are no errors
        print ("ok, seems legit")
        else
        print ("error code, with error code message")
    

# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu", 
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org", 
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com",
        ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address(e) 
        if r == None:
            print(e, s) # OK
        else:
            print(f"{e} - error: {s}, error code: {r}") # Error

from ex_2_task_1_solution import is_valid_email_address as is_valid 

gave_up = False
attempts_left = 3

# your code - start
#I don't understand what I'm supposed to be doing with this. I also don't have working code from the first task. 

# your code - end
if not gave_up:
    print("valid email", email)
else:
    print("invalid email", email)
