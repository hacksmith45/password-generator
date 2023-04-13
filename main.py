import random
import requests

def password_generator():
    user_input = input("For a strong password, type 'strong'. For a weak one, type 'weak': ")
    if user_input.lower() == 'weak':
        url = 'https://api.wordnik.com/v4/words.json/randomWord?api_key=98eod40twu9k6x1tvo7d3vy7itbyhxquf284oejc6qag9oiit'
        response = requests.get(url)
        if response.status_code == 200:
            word = response.json()['word']
            return word
        else:
            print("Error fetching word from API")
            return None
    else:
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWXYZ!@#$%^&*()?1234567890'
        password = ''.join(random.choices(letters, k=(random.randrange(8, 40))))
        return password
  
print(password_generator())
