import tkinter as tk
from tkinter import messagebox
import random

class JokeTellingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎭 Alexa Joke Teller 🎭")
        self.root.geometry("550x350")
        self.root.resizable(True, True)
        self.root.configure(bg='#2C3E50')  # Dark blue background
        
        # Color scheme
        self.colors = {
            'bg': '#2C3E50',
            'secondary_bg': '#34495E',
            'accent': '#E74C3C',
            'primary': '#3498DB',
            'success': '#2ECC71',
            'warning': '#F39C12',
            'text': '#ECF0F1',
            'punchline': '#F1C40F'
        }
        
        # Load jokes from file
        self.jokes = self.load_jokes()
        self.current_joke = None
        
        # Create GUI elements
        self.create_widgets()
        
    def load_jokes(self):
        """Load jokes from the randomJokes.txt file"""
        try:
            with open('resources/randomJokes.txt', 'r', encoding='utf-8') as file:
                jokes = [line.strip() for line in file if line.strip()]
            return jokes
        except FileNotFoundError:
            # If file doesn't exist, use some default jokes
            default_jokes = [
                "Why did the chicken cross the road?To get to the other side.",
                "What happens if you boil a clown?You get a laughing stock.",
                "Why did the car get a flat tire?Because there was a fork in the road!",
                "How did the hipster burn his mouth?He ate his pizza before it was cool.",
                "What did the janitor say when he jumped out of the closet?SUPPLIES!!!!",
                "Have you heard about the band 1023MB?It's probably because they haven't got a gig yet…",
                "Why does the golfer wear two pants?Because he's afraid he might get a Hole-in-one.",
                "Why should you wear glasses to maths class?Because it helps with division.",
                "Why does it take pirates so long to learn the alphabet?Because they could spend years at C.",
                "Why did the woman go on the date with the mushroom?Because he was a fun-ghi.",
                "Why do bananas never get lonely?Because they hang out in bunches.",
                "What did the buffalo say when his kid went to college?Bison.",
                "Why shouldn't you tell secrets in a cornfield?Too many ears.",
                "What do you call someone who doesn't like carbs?Lack-Toast Intolerant.",
                "Why did the can crusher quit his job?Because it was soda pressing.",
                "Why did the birthday boy wrap himself in paper?He wanted to live in the present.",
                "What does a house wear?A dress.",
                "Why couldn't the toilet paper cross the road?Because it got stuck in a crack.",
                "Why didn't the bike want to go anywhere?Because it was two-tired!",
                "Want to hear a pizza joke?Nahhh, it's too cheesy!",
                "Why are chemists great at solving problems?Because they have all of the solutions!",
                "Why is it impossible to starve in the desert?Because of all the sand which is there!",
                "What did the cheese say when it looked in the mirror?Halloumi!",
                "Why did the developer go broke?Because he used up all his cache.",
                "Did you know that ants are the only animals that don't get sick?It's true! It's because they have little antibodies.",
                "Why did the donut go to the dentist?To get a filling.",
                "What do you call a bear with no teeth?A gummy bear!",
                "What does a vegan zombie like to eat?Graaains.",
                "What do you call a dinosaur with only one eye?A Do-you-think-he-saw-us!",
                "Why should you never fall in love with a tennis player?Because to them... love means NOTHING!",
                "What did the full glass say to the empty glass?You look drunk.",
                "What's a potato's favorite form of transportation?The gravy train",
                "What did one ocean say to the other?Nothing, they just waved.",
                "What did the right eye say to the left eye?Honestly, between you and me something smells.",
                "What do you call a dog that's been run over by a steamroller?Spot!",
                "What's the difference between a hippo and a zippo?One's pretty heavy and the other's a little lighter",
                "Why don't scientists trust Atoms?They make up everything."
            ]
            # Create resources folder and file with default jokes
            import os
            os.makedirs('resources', exist_ok=True)
            with open('resources/randomJokes.txt', 'w', encoding='utf-8') as file:
                for joke in default_jokes:
                    file.write(joke + '\n')
            return default_jokes
    
    def create_widgets(self):
        """Create and arrange all GUI widgets"""
        # Main title with emoji
        title_label = tk.Label(self.root, text="🎭 Alexa Joke Teller 🎭", 
                              font=("Comic Sans MS", 18, "bold"), 
                              fg=self.colors['text'],
                              bg=self.colors['bg'])
        title_label.pack(pady=15)
        
        # Joke display frame with rounded effect
        joke_frame = tk.Frame(self.root, bg=self.colors['secondary_bg'], 
                             relief='raised', bd=3)
        joke_frame.pack(pady=15, padx=20, fill='both', expand=True)
        
        # Joke setup display
        self.setup_label = tk.Label(joke_frame, 
                                   text="Click 'Alexa tell me a Joke' to start! 🤔", 
                                   font=("Arial", 13, "bold"), 
                                   wraplength=480, 
                                   justify="center",
                                   fg=self.colors['text'],
                                   bg=self.colors['secondary_bg'])
        self.setup_label.pack(pady=20)
        
        # Punchline display
        self.punchline_label = tk.Label(joke_frame, 
                                       text="", 
                                       font=("Arial", 12, "italic", "bold"), 
                                       fg=self.colors['punchline'],
                                       bg=self.colors['secondary_bg'],
                                       wraplength=480, 
                                       justify="center")
        self.punchline_label.pack(pady=15)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg=self.colors['bg'])
        button_frame.pack(pady=20)
        
        # Alexa tell me a Joke button
        self.joke_button = tk.Button(button_frame, 
                                    text="🎤 Alexa tell me a Joke", 
                                    font=("Arial", 12, "bold"), 
                                    bg=self.colors['primary'],
                                    fg='white',
                                    activebackground='#2980B9',
                                    activeforeground='white',
                                    relief='raised',
                                    bd=3,
                                    padx=15,
                                    pady=8,
                                    command=self.tell_joke)
        self.joke_button.grid(row=0, column=0, columnspan=2, padx=5, pady=8, sticky='ew')
        
        # Show Punchline button
        self.punchline_button = tk.Button(button_frame, 
                                         text="💡 Show Punchline", 
                                         font=("Arial", 11, "bold"), 
                                         bg=self.colors['success'],
                                         fg='white',
                                         activebackground='#27AE60',
                                         activeforeground='white',
                                         relief='raised',
                                         bd=3,
                                         padx=10,
                                         pady=6,
                                         command=self.show_punchline,
                                         state="disabled")
        self.punchline_button.grid(row=1, column=0, padx=5, pady=5)
        
        # Next Joke button
        self.next_button = tk.Button(button_frame, 
                                    text="➡️ Next Joke", 
                                    font=("Arial", 11, "bold"), 
                                    bg=self.colors['warning'],
                                    fg='white',
                                    activebackground='#E67E22',
                                    activeforeground='white',
                                    relief='raised',
                                    bd=3,
                                    padx=10,
                                    pady=6,
                                    command=self.next_joke,
                                    state="disabled")
        self.next_button.grid(row=1, column=1, padx=5, pady=5)
        
        # Quit button
        self.quit_button = tk.Button(button_frame, 
                                    text="🚪 Quit", 
                                    font=("Arial", 11, "bold"), 
                                    bg=self.colors['accent'],
                                    fg='white',
                                    activebackground='#C0392B',
                                    activeforeground='white',
                                    relief='raised',
                                    bd=3,
                                    padx=10,
                                    pady=6,
                                    command=self.root.quit)
        self.quit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=8, sticky='ew')
        
        # Status bar
        self.status_label = tk.Label(self.root, 
                                    text=f"📚 Loaded {len(self.jokes)} jokes | Ready!",
                                    font=("Arial", 9),
                                    fg=self.colors['text'],
                                    bg=self.colors['bg'])
        self.status_label.pack(side='bottom', pady=5)
    
    def tell_joke(self):
        """Select and display a random joke setup"""
        if not self.jokes:
            messagebox.showerror("Error", "No jokes found in the file!")
            return
        
        # Select a random joke
        self.current_joke = random.choice(self.jokes)
        
        # Split the joke into setup and punchline
        if '?' in self.current_joke:
            setup, punchline = self.current_joke.split('?', 1)
            setup += "?"  # Add back the question mark
        else:
            # Fallback if no question mark is found
            setup = self.current_joke
            punchline = "(Punchline not properly formatted)"
        
        # Display the setup with emoji
        self.setup_label.config(text=f"🤔 {setup}")
        self.punchline_label.config(text="")
        
        # Store the punchline for later
        self.current_punchline = punchline
        
        # Enable/disable buttons
        self.punchline_button.config(state="normal", bg=self.colors['success'])
        self.next_button.config(state="normal", bg=self.colors['warning'])
        self.joke_button.config(state="disabled", bg='gray')
        
        # Update status
        self.status_label.config(text="😄 Joke loaded! Click 'Show Punchline' to reveal the fun!")
    
    def show_punchline(self):
        """Display the punchline of the current joke"""
        if hasattr(self, 'current_punchline'):
            self.punchline_label.config(text=f"🎭 {self.current_punchline}")
            self.punchline_button.config(state="disabled", bg='gray')
            self.status_label.config(text="😂 Punchline revealed! Click 'Next Joke' for more fun!")
    
    def next_joke(self):
        """Reset for the next joke"""
        self.setup_label.config(text="Click '🎤 Alexa tell me a Joke' for another joke! 🤗")
        self.punchline_label.config(text="")
        
        # Enable/disable buttons with colors
        self.joke_button.config(state="normal", bg=self.colors['primary'])
        self.punchline_button.config(state="disabled", bg='gray')
        self.next_button.config(state="disabled", bg='gray')
        
        # Update status
        self.status_label.config(text="🔄 Ready for a new joke! Click the button above!")

def main():
    root = tk.Tk()
    app = JokeTellingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()