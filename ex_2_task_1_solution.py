def is_valid_email_address(s):
    ''' validates email address in string s, returns tuple of bool and message string'''
    
    # How many @s ?
    num_at = s.count("@")
    if num_at != 1: return 1, "Must have exactly one @!"

    # How many chars pre @ i.e. in A ? All alfanum?
    l = s.split("@")
    A, post = l[0], l[1]  # A, post = l would also work but could be confusing ...
    if len(A) < 3 or len(A) > 16: 
        return 2, "pre @ part must contain 3 - 16 alfanum chars"
    elif A.isalnum() == False:
        return 3, "pre @ part must only contain alfanum chars"

    # how many dots in post?
    if post.count(".") != 1:
        return 4, "post @ part must have exactly one dot!"
    
    # split into B and C 
    B, C = post.split(".")

    # how many chars in B? All alfanum?
    if len(B) < 2 or len(B) > 8:
        return 5, "part after @ and before . must contain 2 - 8 alfanum chars"
    elif B.isalnum() == False:
        return 6, "part after @ and before . must only contain alfanum chars"

    # is C legit?
    if C not in ["com", "edu", "org", "gov"]: 
        return 7, "past-dot part invalid, must be from: com, edu, org, gov"

    return None, "Seems legit"
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

        
