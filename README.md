# Installation
string and random models are used. if these not installed then install them with following command in your terminal/CMD.

pip install strings
pip install random

# Main Coding
# import both modules.

import string
import random
Now, get a-z, A-Z, 0-9, and symbols using string functions provided by string module inbuilt.

    l = string.ascii_lowercase
    u = string.ascii_uppercase
    d = string.digits
    p = string.punctuation

now, ask user to get password length

passlen = int(input("Enter the length of your password: "))

Now, we make list of character we get using string function.

    st = []
    st.extend(list(l))
    st.extend(list(u))
    st.extend(list(d))
    st.extend(list(p))

Here, we convert l, u, d, and p in list type because above string functions like string.ascii_lowercase return a string. And extend() is used to concrete list. This list looks like this.

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

So, we get all character in one list. We use this list to get our password. 

For that we use sample() function to get random character of given length.

sample() is an inbuilt function of a random module in Python that returns a particular length list of items chosen from the sequence i.e. list, tuple, string, or set. Used for random sampling without replacement.

At last, join all character in a list into a string, using a “” character as separator.

print("".join(random.sample(st, passlen)))

# Final Code
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
    
Output
Enter password length: 12
Your password: 7rZ&;v{x0A9n

You can  make this code better by 
- adding a minimum length password in 8 characters or 
- can also exclude some character from the symbol list.
