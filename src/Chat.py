from flask import *
#from spellchecker import SpellChecker
#from fuzzywuzzy import process
import aiml

#spell = SpellChecker()

app = Flask(__name__)

responses = ["I'm sorry, I didn't quite catch that.",
             "I don't understand. Do you need help with the campus map codes or directions",
             "Excuse me, do you have everything typed out properly",
             "Not sure I know what you mean, maybe type 'Help' and see if that is of any use to you?"]
userstate = []
botstate = []
campus_words = []
k = aiml.Kernel()
k.learn("std-startup.xml")


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/help')
def contact():
    return render_template('help.html')


@app.route("/get")
#function for the bot response
def get_bot_response():
    user_msg = request.args.get('msg')
    cleanmsg = spellchecker(user_msg)
    userstate.append(cleanmsg)
    x = k.respond(cleanmsg)
    if x != "":  # If the bot generated a response
        botstate.append(x)  # Store the response for traceback
        if x in responses:
            if len(userstate) > 1:  # if bot returned an response for invalid query traceback
                y = userstate[-2]
                z = k.respond(y)
                if z in responses:
                    return str(x)
                else:
                    x = x + "/n"
                    return str(x + z)
            else:
                return str(x)
        return str(x)
    else:
        return "I can't understand your question Type help to see what I can understand."


'''
def spellchecker(usermsg):
    wordlist = usermsg.lower().split()
    misspelled = spell.unknown(wordlist)
    for word in misspelled:
        i = wordlist.index(word)
        correction = spell.correction(word)
        possible_re_correct = process.extract(correction, campus_words)

        if possible_re_correct[0][1] >= 66:
            wordlist[i] = possible_re_correct[0][0]
        else:
            wordlist[i] = correction

    return " ".join(wordlist)


'''
def spellchecker(usermsg):
    return usermsg


if __name__ == '__main__':
    k.respond("load aiml b")
    #spell.word_frequency.load_text_file("./recognised_words.txt")
    #with open("./recognised_words.txt") as f:
     #   campus_words = f.read().split



    app.run(debug=True)
