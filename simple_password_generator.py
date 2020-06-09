#follow @kapeed_thetechguy

import string
import random

if __name__== "__main__":
    l = string.ascii_lowercase
    u = string.ascii_uppercase
    d = string.digits
    p = string.punctuation


    passlen = int(input("Enter the length of your password: "))
    st = []
    st.extend(list(l))
    st.extend(list(u))
    st.extend(list(d))
    st.extend(list(p))
    
    print("The Password is: ", end="")
    print("".join(random.sample(st, passlen)))
    