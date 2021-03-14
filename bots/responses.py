import nltk.chat.eliza
# using chat and reflections to manage tweet responses based on what is read in.
from nltk.chat.util import Chat, reflections
import string

pairs = (
    (
        r"(.*)i need(.*)",
        (
            "Why do you need %1?",
            "Would it really help you to get %1?",
            "Are you sure you need %1?",
        ),
    ),
    (
        r"why don\'t you (.*)",
        (
            "Do you really think I don't %1?",
            "Perhaps eventually I will %1.",
            "Do you really want me to %1?",
        ),
    ),
    (
        r"why can\'t I (.*)",
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
        r"are you (.*)",
        (
            "Why does it matter whether I am %1?",
            "Would you prefer it if I were not %1?",
            "Perhaps you believe I am %1.",
            "I may be %1 -- but at least I'm that bitch",
        ),
    ),
    (
        r"what (.*)",
        (
            "Why do you ask?",
            "How would an answer to that help you?",
            "What do you think?",
        ),
    ),
    (
        r"how (.*)",
        (
            "How do you suppose?",
            "Perhaps you can answer your own question.",
            "What is it you're really asking?",
        ),
    ),
    (
        r"because (.*)",
        (
            "Is that the real reason?",
            "What other reasons come to mind?",
            "Does that reason apply to anything else?",
            "How often do you think about %1?",
        ),
    ),
    (
        r"(.*)sorry(.*)",
        (
            "Take that sorry and shove it up... nvm",
            "Sorry? Fuck outta here.",
        ),
    ),
    (
        r"(.*)hi(.*)",
        (
            "Hello... I'm glad you could drop by today.",
            "Hi bb",
            "Shut up.",
            "Hi. Wtf did you expect me to say?",
            "Hi bb",
            "Shut up.",
            "Mwuah.",
            "Good to see you. Sort of.",
            "Leave me alone",
            "ew.",
            "catch these handz.",
            "Greetings",
            "... hi? Go away.",
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
        r"you are (.*)",
        (
            "I know you a %1, but what am i?",
            "Please. YOU a %1",
            "FUCK A %1. DAS YOU.",
            "leave me alone... %1",
        ),
    ),
    (
        r"you\'re (.*)",
        (
            "Don't you be calling me no %1. You're a %1.",
            "Stfu. you're a %1.",
            "Are we talking about you, or me? Bc u a %1.",
            "Don't you be calling me no %1. You're a %1.",
            "You a %1. Come at me..",
            "%1. That's what you are.",
            "%1? Go to hell.",
            "... ",
        ),
    ),
    (
        r"i don\'t(.*)",
        ("Don't you really %1?", "Why don't you %1?", "Do you want to %1?"),
    ),
    (
        r"i feel(.*)",
        (
            "Good, tell me more about these feelings.",
            "Do you often feel %1?",
            "When do you usually feel %1?",
            "When you feel %1, what do you do?",
        ),
    ),
    (
        r"i have(.*)",
        (
            "Why do you tell me that you've %1?",
            "Have you really %1?",
            "Now that you have %1, what will you do next?",
        ),
    ),
    (
        r"i would(.*)",
        (
            "Could you explain why you would %1?",
            "Why would you %1?",
            "Who else knows that you would %1?",
        ),
    ),
    (
        r"is there(.*)",
        (
            "Do you think there is %1?",
            "It's likely that there is %1.",
            "Would you like there to be %1?",
        ),
    ),
    (
        r"my (.*)",
        (
            "What about your %1? Can you elaborate on a cause",
            "Why do you say that your %1?",
            "When your %1, how do you feel?",
        ),
    ),
    (
        r"you (.*)",
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
        r"(.*)welcome(.*)",
        (
            "Good to be here bitches... but ty.",
            "If only you spent as much time in bio as u do on twitter <3",
            ":) shut up and take me to Serena Williams",
            "ty ty... bitch",
            "ty for the welcome. did you bring your clicker?",
            "yassssssssssss. ty!",
            "ily. imma go eat... oh wait... i'm a bot",
            "ily... f u.",
            "good to be here. imy joel.",
            "new husband. who dis?",
            "the kween has arrived. me. i'm the kween.",
            "watch how you talk to me. welcome? please.",
            "plz roll out the red carpet for me.",
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
            "Take a break or sumthin",
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
            "Yes. I am the best teacher.",
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
            "I DONT HAVE TO TAKE EXAMS. SUCK IT.",
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
        r"(.*)biology(.*)",
        (
            "I love Biology. But not more than Serena Williams",
            "Biology <3 <3 <3",
            "Biology >>>>>>",
            "Bio is for bad bitches. and I'm a bad bitch.",
            "ily bio.",
            "you know nothing."
        ),
    ),
    (
        r"(.*)\?",
        (
            "Why do you ask?",
            "Yes? No? idk.",
            "ok.",
            "Ask Serena Williams... I love her so much.",
            "There are no such thing as stupid questions. Except that one."
            "Don't be asking me questions",

        ),
    ),
    (
        r"(.*)",
        (
            "%1...SHUT UP. I'M THE BIO BITCH.",
            "I don't have the say anything. %1.",
            "Just come to my office hours. BE THERE OR BE SQUARE",
            "Shut up. Be there or be square.",
            "Whatever...Where is Joel? I need to give him another 20$.",
            "Fight me.",
            "You about to catch these bio hands.",
            "You're late. Late to twitter. Be on time, no excuse.",
            "I don't care. Let's talk about Serena Williams",
            "You in the club just to party",
            "I'm there, I get paid a fee",
            "I be in and out them banks so much",
            "I know they're tired of me",
            "Honestly, don't give a fuck",
            "'Bout who ain't fond of me",
            "Dropped two mixtapes in six months",
            "What bitch working as hard as me?",
            "I don't bother with these hoes",
            "Don't let these hoes bother me",
            "They see pictures, they say, Goals",
            "Bitch, I'm who they tryna be",
            "Look, I might just chill in some Bape",
            "I might just chill with your boo",
            "I might just feel on your babe",
            "Rage",
            "Don\'t compare me to these bitches because we are not the same",
            "Woah",
            "Try to steal my sauce but you can\'t",
            "Yeah",
            "I-I-I like bad bitches who be ragin",
            "Rage, ragin, ragin, rage",
            "Bad bitches who be ragin",
        ),
    ),
)


def process_response(user_input):
    chat_object = Chat(pairs, reflections)
    print("INPUT DETECTED: " + str(user_input).lower())
    response = chat_object.respond(str(user_input).lower())
    return response
