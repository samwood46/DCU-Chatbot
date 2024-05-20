from unittest import TestCase
# import src.Chat as Chat
# from src.Chat import *
import aiml

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")


class TestResponses(TestCase):
    # tests responses in building codes file

    def test_get_bot_response_codes1(self):
        y = "C"
        x = kernel.respond(y)
        self.assertEqual(x, "C is the Henry Grattan Building. Do you need directions ? (Yes/No)")

    def test_get_bot_response_codes2(self):
        y = "what is J"
        x = kernel.respond(y)
        self.assertEqual(x, "J is the Hamilton Building. Do you need directions ? (Yes/No)")

    def test_get_bot_response_codes3(self):
        y = "What does A mean on the campus map ?"
        x = kernel.respond(y)
        self.assertEqual(x, "A is the Albert College Building. Do you need directions ? (Yes/No)")

    def test_get_bot_response_codes4(self):
        y = "X please"
        x = kernel.respond(y)
        self.assertEqual(x, "X is the Science Building. Do you need directions ? (Yes/No)")

    def test_get_bot_response_codes5(
            self):  # ensures the user can reply yes to the code meaning and receice directions.
        z = "X please"
        i = kernel.respond(z)
        y = "yes"
        x = kernel.respond(y)
        self.assertEqual(x,
                         "Walk through the Collin's ave entrance/n The second building on your left is the science building.")

    # tests for aquiring directions to buildings on the DCU campus
    def test_get_bot_response_buildings1(self):
        y = "Where is the Nursing building"
        x = kernel.respond(y)
        self.assertEqual(x,
                         "Walk through the collins ave entrance/n The Nursing building is the first building on your left.")

    def test_get_bot_response_buildings2(self):
        y = "Can you tell me where the Science building is"
        x = kernel.respond(y)
        self.assertEqual(x,
                         "Walk through the Collin's ave entrance/n The first building on your left is the science building.")

    def test_get_bot_response_buildings3(self):
        y = "Business Building"
        x = kernel.respond(y)
        self.assertEqual(x,
                         "Walk in through the collins ave entrance/n Take a right at the building in front of you/n The Business building is the second building on your left.")

    # tests for directions to various rooms on campus
    def test_get_bot_response_rooms1(self):
        y = "HG05"
        x = kernel.respond(y)
        self.assertEqual(x,
                         "On the bottom floor of the nursing building/n Walk in the doors to the left of the front entrance/n The rooms are in order on the left from/n HG05, HG06, HG07, HG08, HG09, HG10, HG11, HG12, HG13, HG50")

    def test_get_bot_response_rooms2(self):
        y = "Where is QG13"
        x = kernel.respond(y)
        self.assertEqual(x,
                         "On the bottom floor of the business building/n If you stand with your back facing the stairs (main area)/n The doors on this side are numbered from QG13, QG15, QG21 and QG22.")

    def test_get_bot_response_rooms3(self):
        y = "can you tell me where L128 is?"
        x = kernel.respond(y)
        self.assertEqual(x,
                         "On the first floor of the computing building/n Walk up the stairs take a left and keep walking/n The door is on your left.")

    def test_get_bot_response_rooms4(self):
        y = "l128 please ?"
        x = kernel.respond(y)
        self.assertEqual(x,
                         "On the first floor of the computing building/n Walk up the stairs take a left and keep walking/n The door is on your left.")

    # tests for acquiring certain images
    def test_get_bot_response_images1(self):
        y = "Helix image"
        x = kernel.respond(y)
        self.assertEqual(x, "../static/Assets/images/helix.jpg /n This is an image of the helix")

    def test_get_bot_response_images2(self):
        y = "Nursing building image"
        x = kernel.respond(y)
        self.assertEqual(x, "../static/Assets/images/_nursing.jpg /n This is an image of the Nursing Building")

    # help message
    def test_get_bot_response_help(self):
        y = "help"
        x = kernel.respond(y)
        self.assertEqual(x,
                         "Text 'BUILDING CODES MORE'/n 'ROOM DIRECTIONS MORE' /n 'BUILDING DIRECTIONS MORE'/n 'BUILDING IMAGES MORE'/n 'SHOP DIRECTIONS MORE'/n for information on these features.")

    # test for basic chat
    def test_basicchat(self):  # testing the thanks
        y = "thanks"
        basic = ["Your welcome!", "No problem!", "I am happy to help",
                 "No problem! If you have any more questions just ask!", "Any time!", "Of course! It is why I am here!"]
        x = kernel.respond(y)
        self.assertTrue(x in basic)

    # test for traceback function
    def test_get_bot_response_traceback(self):
        whats0 = "I don't understand. Do you need help with the campus map codes or directions /nC is the Henry Grattan Building. Do you need directions ? (Yes/No)"
        whats = "C is the Henry Grattan Building. Do you need directions ? (Yes/No)"
        whats1 = "I'm sorry, I didn't quite catch that. /nC is the Henry Grattan Building. Do you need directions ? (Yes/No)"
        whats2 = "Excuse me, do you have everything typed out properly /nC is the Henry Grattan Building. Do you need directions ? (Yes/No)"
        whats3 = "Not sure I know what you mean, maybe type 'Help' and see if that is of any use to you? /nC is the Henry Grattan Building. Do you need directions ? (Yes/No)"
        y = "C"
        i = kernel.respond(y)
        y2 = "dnwidb"
        j = kernel.respond(y2)
        self.assertTrue(whats in j)

    #  y3 = "Yes"
    #  x = kernel.respond(y3)
    # self.assertEqual(x, "Walk down the path from the Ballymun entrance and take the third left/n You will come to a Building with Bank of Ireland on it/n This is the Henry Grattan.")

    # test for greetings
    def test_greeting(self):
        y = "hi "
        greetings = ["Hello! Welcome to the DCU Campus chatbot!",
                     "Hi! Are you having trouble with the campus map? I am here to help!",
                     "Hello there! What can I help you with today?",
                     "Hi! What are your DCU Campus queries? I will try and answer to the best of my ability!",
                     "Hi! DCU Campus Chatbot at your service!",
                     "Hello! Do you need help with directions? Ask away! You are helping me learn!",
                     "Hi there, need help with Building codes or directions on campus? You need look no further!",
                     "Hi! I am the DCU Campus Chatbot service! How can I assist?",
                     "Salutations! What can I do for you on this fine day?",
                     "Hi! What questions do you have for me? I am eager to learn!"]
        x = kernel.respond(y)
        self.assertTrue(x in greetings)

    # tests for FAQ's
    def test_FAQ(self):
        y = "where can i get my timetable"
        x = kernel.respond(y)
        self.assertEqual(x,
                         "You can get the time table at the following link/n https://www.dcu.ie/registry/Open-Timetables.shtml")

    # test a query for the buses file
    def test_buses(self):
        y = "Can you tell me about buses from DCU"
        x = kernel.respond(y)
        self.assertEqual(x, "There is a number of buses from the College./n Would you like to see a list?")
