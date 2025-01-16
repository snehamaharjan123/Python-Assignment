import json
import random
import logging

logging.basicConfig(filename='chatbot_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def load_responses(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def generate_agent_name():
    names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
    return random.choice(names)


def get_response(user_input, responses):
    user_input = user_input.lower()
    for keyword, replies in responses['keywords'].items():
        if keyword in user_input:
            return random.choice(replies)
    return "I'm not sure about that. Can you ask something else?"

def main():
    print("Welcome to the University of Poppleton Chatbot!")
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! I'm your virtual assistant today.")
    
    agent_name = generate_agent_name()
    print(f"Your agent today is {agent_name}.")

    responses = load_responses('responses.json')

    while True:
        user_question = input(f"{user_name}: ")
        logging.info(f"{user_name}: {user_question}")

        if user_question.lower() in ['bye', 'quit', 'exit']:
            print(f"{agent_name}: Goodbye, {user_name}! Have a great day!")
            logging.info(f"{agent_name}: Goodbye, {user_name}! Have a great day!")
            break

        response = get_response(user_question, responses)
        print(f"{agent_name}: {response}")
        logging.info(f"{agent_name}: {response}")

if __name__ == "__main__":
    main()import random
import logging


logging.basicConfig(filename='chatbot_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

responses = {
    "hello": ["Hi there! How can I help you today?", "Hello! What can I assist you with?"],
    "name": ["I'm a chatbot created to help you with university-related questions.", "My name is UniBot, your friendly assistant!"],
    "help": ["Sure! I can help you with general university info. Ask away!", "I'm here to assist you with anything about the university."],
    "courses": ["We offer courses in Science, Arts, and Technology. Which one interests you?", "You can study a variety of subjects, including Computer Science, Business, and more."],
    "admissions": ["You can apply on our website. The application deadline is June 30th.", "The deadline for applying is June 30th. Visit our website to apply!"],
    "library": ["The library is open from 9 AM to 5 PM. You can borrow books anytime!", "The library opens at 9 AM and closes at 5 PM. Don't forget your student ID!"],
    "campus": ["Our campus is located at 123 University Ave, right next to the park.", "The university campus is at 123 University Ave, near the city center."],
    "sports": ["We have a gym, basketball courts, and football fields! Come join us.", "You can join our basketball, football, and tennis teams at the sports center."],
    "dorms": ["The dorms are comfortable and have a great view. You can apply online.", "Our dorms are located on campus and are available for all students."],
    "contact": ["For more info, visit our contact page or email us at contact@university.com.", "You can contact us at contact@university.com for more details."]
}

random_responses = [
    "Sorry, I didn't understand that. Could you ask something else?",
    "I didn't catch that. Can you try again?",
    "Hmm, that's an interesting question. Let me think...",
    "I am still learning! Can you ask me something else?",
    "I don't know the answer to that, but I can help with other questions."
]

def generate_agent_name():
    names = ["UniBot", "EduBot", "StudyBot", "InfoBot", "HelpBot"]
    return random.choice(names)

def get_response(user_input):
    user_input = user_input.lower()
    for keyword, replies in responses.items():
        if keyword in user_input:
            return random.choice(replies)
    return random.choice(random_responses)


def log_conversation(user_name, user_input, agent_response):
    logging.info(f"{user_name}: {user_input}")
    logging.info(f"Agent: {agent_response}")

# Main chatbot function
def main():
    print("Welcome to the University Chatbot!")
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! I'm your virtual assistant today.")
    
    agent_name = generate_agent_name()
    print(f"Your agent today is {agent_name}. Let's chat!")

    while True:
        user_question = input(f"{user_name}: ").strip()

        if user_question.lower() in ['bye', 'quit', 'exit']:
            print(f"{agent_name}: Goodbye, {user_name}! Have a great day!")
            log_conversation(user_name, user_question, f"Goodbye, {user_name}!")
            break
        
        response = get_response(user_question)
        print(f"{agent_name}: {response}")
        log_conversation(user_name, user_question, response)

if __name__ == "__main__":
    main()
