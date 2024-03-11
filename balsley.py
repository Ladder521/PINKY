import threading, os, time, random, string, pygame
from gtts import gTTS

#Initialize pygame mixer
pygame.mixer.init()
os.system('clear')

#Function to play audio
def play_audio(file_path, message=None):
    if message:
        print(message)
    
    def play_sound(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(9)

    audio_thread = threading.Thread(target=play_sound, args=(file_path,))
    audio_thread.start()

    if message:
        # Wait for the audio to start playing
        while not pygame.mixer.music.get_busy():
            time.sleep(0.1)
        # Print dots while audio is playing
        while pygame.mixer.music.get_busy():
            print(".", end='', flush=True)
            time.sleep(1)
        print()

play_audio('/data/data/com.termux/files/home/PINKY/mp3/pink.mp3')
print()
print("""
                             .--.            .--.
                            ( (`\\\\.\"--``--\".//`) )
                             '-.   __   __    .-'
                              /   /__\\ /__\\   \\
                             |    \\ 0/ \\ 0/    |
                             \\     `/   \\`     /
                              `-.  /-\"\"\"-\\  .-`  
                                /  '.___.'  \\       
                                \\     I     /       
                                 `;--'`'--;`        
                                   '.___.'    
                                  ___| |___           .\"`-.
                               .-`  .---.  `-.       /     )
                              /   .'     '.   \\     /      )
                             /  /||       ||\\  \\   /  /`\"\"`
                            /  / ||       || \\  \\ /  /
                           /  /  ||       ||  \\  /  /
                          /  (___||___.-=--.   \\   /
                         (                -;    '-'
                          `-----------.___~;

                                  PINKY Pink

                                   LADDER521
          """)

# Function to print text in yellow color
def print_yellow(text):
    for char in text:
        print("\033[93m" + char + "\033[0m", end='', flush=True)
        time.sleep(0.24)

# Function to print text in blue color
def print_blue(text):
    for char in text:
        print("\033[94m" + char + "\033[0m", end='', flush=True)
        time.sleep(0.3)

# Function to print text in purple color
def print_purple(text):
    for char in text:
        print("\033[95m" + char + "\033[0m", end='', flush=True)
        time.sleep(1)

# Function to print text in red color
def print_red(text):
    for char in text:
        print("\033[91m" + char + "\033[0m", end='', flush=True)
        time.sleep(0.18)

# Function to print text in white colour
def print_white(text):
    for char in text:
        print("\033[97m" + char + "\033[0m", end='', flush=True)
        time.sleep(0.8)

# Function to print text in green color
def print_green(text):
    for char in text:
        print("\033[92m" + char + "\033[0m", end='', flush=True)
        time.sleep(0.45)

def print_thank_you():
    message = " [~] THANK YOU [~] "
    play_audio('/data/data/com.termux/files/home/PINKY/mp3/thank_you.mp3')
    print_red(message)
    play_audio('/data/data/com.termux/files/home/PINKY/mp3/meet.mp3')
    print()


def generate_password():
    play_audio('/data/data/com.termux/files/home/PINKY/mp3/length.mp3')
    passlen = int(input("Enter the length of password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(characters, passlen))
    print()


    def print_your():
        message = " [¢] Choosing The Characters "
        print_yellow(message)
        print()

    print_your()
    print()


    def print_length(passlen):
        message1 = str(passlen)
        message2 = " Characters Choosed "
        message3 = " [!] "
        print_red(message3)
        print_white(message1)
        print_green(message2)
        print()

    print_length(passlen)
    print()


    def print_you():
        message = " [•] Permutating The Characters "
        print_yellow(message)
        print()

    print_you()
    print()



    def print_arrange():
        message1 = "     Arrangement Of Characters ..."
        message2 = "..."
        message3 = "...✓✓✓ COMPLETE "
        print_red(message1)
        print_yellow(message2)
        play_audio('/data/data/com.termux/files/home/PINKY/mp3/arrange.mp3')
        print_green(message3)
        print()

    print_arrange()
    print()


    def print_your_pass():
        message1 = " [✓] Your Password Is: "
        message2 = password
        print_green(message1)
        print_purple(message2)
        tts = gTTS(text=password, lang='en')
        tts.save("password.mp3")
        play_audio('/data/data/com.termux/files/home/PINKY/password.mp3')
        os.remove("password.mp3")
        print()

    print_your_pass()
    print()



    def print_strength():
        strength = "Password Strength: "
        m1 = "Weak"
        m2 = "Moderate"
        m3 = "Strong"
        if passlen < 8:
            strength += m1
            play_audio('/data/data/com.termux/files/home/PINKY/mp3/weak.mp3')
            print_red(strength)
        elif 8 <= passlen < 12:
            strength += m2
            play_audio('/data/data/com.termux/files/home/PINKY/mp3/moderate.mp3')
            print_yellow(strength)
        else:
            strength += m3
            play_audio('/data/data/com.termux/files/home/PINKY/mp3/strong.mp3')
            print_green(strength)
        print()

    print_strength()
    print()

while True:
    print()
    play_audio('/data/data/com.termux/files/home/PINKY/mp3/EV.mp3')
    user_input = input("Enter 'G' to generate a password or 'E' to exit: ")
    if user_input.lower() == 'g':
        print()
        generate_password()
    elif user_input.lower() == 'e':
          print()
          print_thank_you()
          break
