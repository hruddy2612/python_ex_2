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

#make sure there is exactly one @
    if not s.count("@") == 1:
        return 2, "you need exactly one @"
    
   
    #how many characters in A (characters before the @)
    A = s.split("@")
   
    if len(A[0]) < 3 or len(A[0]) > 16: # A needs to be within 3-16 characters, if outside the range, an error occurs
        return  1, "must be 3-16 characters"  # returns error code, error message
     
    
    
    #how many characters in B (after the @ but before the '.') 
    B = A[1].split (".")
    if len(B[0]) < 2 or len(B[0]) > 8: # spaces around operators: len(B) < 2 or len(B) > 8:
        return 4, "must contain between 2 and 8 characters" # returns error code, error message
    
    #checking for correct email address ending for C
    if not B[1] in ["com", "edu", "org", "gov"]: 
        return 3, "must contain com, edu, org, gov"

  
    else:
        return None, "email is ok"
'''
# check email string and print result of check (when returning 1 thing!)
email = "hruddy@iastate.eu"


err, res = is_valid_email_address(email) #(when returning 2 things!)
if err != None: # so err must be an int error code!
    print("Error:", err, res)
else: # err must be None, i.e. email was OK
    print(email, "is ok!")
'''

# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu", 
        "chris.edu",
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
 
if r == None: #email is valid
    print(e,"is valid")

# attempts need to count down somehow, I am not sure how to make that happen

elif attempts_left == 0 #if attempts reach zero, user has to give up
    print(" No attempts left, email is invalid")
 

# your code - end
if not gave_up:
    print("valid email", email)
else:
    print("invalid email", email)
