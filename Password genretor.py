import random
import string

letters_len = int(input("enter length password: "))

print(
    "".join(
        random.choices(
            string.ascii_letters + string.digits + string.punctuation, k=letters_len
        )
    )
)
