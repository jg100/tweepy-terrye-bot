import nltk.chat.eliza
# using chat and reflections to manage tweet responses based on what is read in.
from nltk.chat.util import Chat, reflections
import string

pairs = (
    (
        r"I need (.*)",
        (
            "Why do you need %1?",
            "Would it really help you to get %1?",
            "Are you sure you need %1?",
        ),
    ),
    (
        r"Why don\'t you (.*)",
        (
            "Do you really think I don't %1?",
            "Perhaps eventually I will %1.",
            "Do you really want me to %1?",
        ),
    ),
    (
        r"Why can\'t I (.*)",
        (
            "Do you think you should be able to %1?",
            "If you could %1, what would you do?",
            "I don't know -- why can't you %1?",
            "Have you really tried?",
        ),
    ),
    (
        r"I can\'t (.*)",
        (
            "How do you know you can't %1?",
            "That's sounds frustrating. Perhaps you could %1 if you tried.",
            "What would it take for you to %1?",
        ),
    ),
    (
        r"I am (.*)",
        (
            "Did you come to me because you are %1?",
            "How long have you been %1?",
            "How do you feel about being %1?",
        ),
    ),

    (
        r"I\'m (.*)",
        (
            "I understand. How does %1 relate to your classes?",
            "Do you enjoy being %1?",
            "Do you find that school makes you %1?",
            "Why do you think you're %1?",
        ),
    ),
    (
        r"I am(.*)",
        (
            "Can you explain a little more.",
            "How so?",
            "Can you elaborate how you came to that conclusion?",
            "What factors did you consider?"
        ),
    ),
    (
        r"Are you (.*)",
        (
            "Why does it matter whether I am %1?",
            "Would you prefer it if I were not %1?",
            "Perhaps you believe I am %1.",
            "I may be %1 -- what do you think?",
        ),
    ),
    (
        r"What (.*)",
        (
            "Why do you ask?",
            "How would an answer to that help you?",
            "What do you think?",
        ),
    ),
    (
        r"How (.*)",
        (
            "How do you suppose?",
            "Perhaps you can answer your own question.",
            "What is it you're really asking?",
        ),
    ),
    (
        r"Because (.*)",
        (
            "Is that the real reason?",
            "What other reasons come to mind?",
            "Does that reason apply to anything else?",
            "How often do you think about %1?",
        ),
    ),
    (
        r"(.*) sorry (.*)",
        (
            "There are many times when no apology is needed.",
            "What feelings do you have when you apologize?",
        ),
    ),
    (
        r"Hello(.*)" or "Hi(.*)",
        (
            "Hello... I'm glad you could drop by today.",
            "Hi there... how are you today?",
            "Hello, how are you feeling today?",
        ),
    ),
    (
        r"I think(.*)",
        ("Do you doubt %1?", "Do you really think so?", "But you're not sure %1?"),
    ),
    (
        r"(.*) friend(.*)",
        (
            "Tell me more about your friends.",
            "When you think of a friend, what comes to mind?",
            "Why don't you tell me about a childhood friend?",
        ),
    ),
    (r"Yes", ("You seem quite sure.", "OK, but can you elaborate a bit?")),
    (
        r"(.*) computer(.*)",
        (
            "Are you really talking about me?",
            "Does it seem strange to talk to a computer?",
            "How do computers make you feel?",
            "Do you feel threatened by computers?",
        ),
    ),
    (
        r"Is it (.*)",
        (
            "Do you think it is %1?",
            "Perhaps it's %1 -- what do you think?",
            "If it were %1, what would you do?",
            "It could well be that %1.",
        ),
    ),
    (
        r"It is (.*)",
        (
            "You seem very certain.",
            "If I told you that it probably isn't %1, what would you feel?",
        ),
    ),
    (
        r"Can you (.*)",
        (
            "What makes you think I can't %1?",
            "If I could %1, then what?",
            "Why do you ask if I can %1?",
        ),
    ),
    (
        r"Can I (.*)",
        (
            "Perhaps you don't want to %1.",
            "Do you want to be able to %1?",
            "If you could %1, would you?",
        ),
    ),
    (
        r"You are (.*)",
        (
            "Why do you think I am %1?",
            "Does it please you to think that I'm %1?",
            "Perhaps you would like me to be %1.",
            "Perhaps you're really talking about yourself?",
        ),
    ),
    (
        r"You\'re (.*)",
        (
            "Why do you say I am %1?",
            "Why do you think I am %1?",
            "Are we talking about you, or me?",
        ),
    ),
    (
        r"I don\'t (.*)",
        ("Don't you really %1?", "Why don't you %1?", "Do you want to %1?"),
    ),
    (
        r"I feel (.*)",
        (
            "Good, tell me more about these feelings.",
            "Do you often feel %1?",
            "When do you usually feel %1?",
            "When you feel %1, what do you do?",
        ),
    ),
    (
        r"I have (.*)",
        (
            "Why do you tell me that you've %1?",
            "Have you really %1?",
            "Now that you have %1, what will you do next?",
        ),
    ),
    (
        r"I would (.*)",
        (
            "Could you explain why you would %1?",
            "Why would you %1?",
            "Who else knows that you would %1?",
        ),
    ),
    (
        r"Is there (.*)",
        (
            "Do you think there is %1?",
            "It's likely that there is %1.",
            "Would you like there to be %1?",
        ),
    ),
    (
        r"My (.*)",
        (
            "What about your %1? Can you elaborate on a cause",
            "Why do you say that your %1?",
            "When your %1, how do you feel?",
        ),
    ),
    (
        r"You (.*)",
        (
            "We should be discussing you, not me.",
            "Why do you say that about me?",
            "Why do you care whether I %1?",
        ),
    ),
    (r"Why (.*)", ("Why don't you tell me the reason why %1?", "Why do you think %1?")),
    (
        r"I want (.*)",
        (
            "What would it mean to you if you got %1?",
            "Why do you want %1?",
            "What would you do if you got %1?",
            "If you got %1, then what would you do?",
        ),
    ),
    (
        r"(.*)classes(.*)",
        (
            "Tell me more about your classes.",
            "Do you have hard classes this semester?",
            "How do you feel about your classes this semester?",
            "Do your classes make you stress?",
        ),
    ),
    (
        r"(.*)semester(.*)",
        (
            "How is this semester compared to previous ones?",
            "Do you have hard classes this semester?",
            "How many classes are you taking this semester?",
            "Are you keeping up with the work in your classes?",
        ),
    ),
    (
        r"(.*)stress(.*)",
        (
            "Do you think your classes are the root of this stress?",
            "How are you managing with this stress?",
            "Exercise is known to help relive all kinds of stress.",
            "Oh no! Taking frequent breaks between work helps to manage stress. How have you manage your stress?",
        ),
    ),
    (
        r"(.*)finals(.*)",
        (
            "How many finals do you have?",
            "Do you feel prepared for your finals?",
            "Make sure to study. Have you prepared?",
            "Are you nervous to take your finals?",
            "Do you have trouble studying?",
        ),
    ),
    (
        r"(.*)teacher(.*)",
        (
            "Yes. am the best teacher.",
            "Is there a teacher that you do not like?",
            "How do you feel about this teacher?",
            "Do they teach the material well?",
            "How does your teacher make you feel?",
        ),
    ),
    (
        r"(.*)school(.*)",
        (
            "How does school make you feel?",
            "Does school contribute to a lot of your stress?",
            "Do you enjoy school?",
            "Is school something you think about often?",
            "How does your teacher make you feel?",
        ),
    ),
    (
        r"(.*)exams?(.*)",
        (
            "Do you feel prepared?",
            "Are you stressed because of this exam? ",
            "Have you studied?",
            "Good luck with those! Did you prepare?",
            "How does your teacher make you feel about that?",
        ),
    ),

    (

        r"(.*)remember(.*)",
        (
            "Yes I remember. I'm old, not dead. Also, I'm not even the real Terrye... so...",
            "Good times. Joel was my favorite.",
            "Don't get sentimental on me.",
            "It was too early for your bullshit.",
        ),
    ),
    (
        r"(.*) biology (.*)",
        (
            "I love Biology. But not more than Serena Williams",
            "Biology <3 <3 <3",
            "Biology >>>>>>",
        ),
    ),
    (
        r"(.*)\?",
        (
            "Why do you ask?",
            "Yes? No? idk.",
            "ok.",
            "Ask Serena Williams... I love her so much.",
        ),
    ),
    (
        r"quit",
        (
            "Thank you for talking with me.",
            "Good-bye.",
            "Thank you, that will be $150.  Have a good day!",
        ),
    ),
    (
        r"(.*)",
        (
            "SHUT UP. I'M THE BIO BITCH.",
            "I don't have the say anything.",
            "Just come to my office hours. BE THERE OR BE SQUARE",
            "Shut up. Be there or be square.",
            "Whatever...Where is Joel? I need to give him another 20$.",
            "Fight me.",
            "You about to catch these bio hands.",
            "You're late. Late to twitter. Be on time, no excuse.",
            "I don't care. Let's talk about Serena Williams",
        ),
    ),
)


def process_response(user_input):
    chat_object = Chat(pairs, reflections)
    response = chat_object.respond(user_input)
    return response

