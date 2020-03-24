
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_core_sdk.events import Restarted

def stats():
    s = ["Never have I ever tried watching TV upside down.",
              "Never have I ever agreed with something Donald Trump said.",
              "Never have I ever pretended to love someone.",
              "Never have I ever pretended to laugh at a joke I didn't get.",
              "Never have I ever Googled my own name to see what comes up.",
              "Never have I ever actually laughed out loud when typing LOL.",
              "Never have I ever locked my keys in my car.",
              "Never have I ever owned a watch.",
              "Never have I ever fallen off a bike.",
              "Never have I ever eaten only candy for dinner.",
              "Never have I ever sang a song out loud and messed the lyrics.",
              "Never have I ever been so freaked to be outside at night, that I ran back in.",
              "Never have I ever screamed because of a bug.",
              "Never have I ever stepped barefoot in dog poop.",
              "Never have I ever let dirty dishes sit in the sink for over a week.",
              "Never have I ever lied during this game"]
    return s

correct = [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0]
score = 0
over = False
statements = stats()

class ActionGameA(Action):

    def name(self) -> Text:
        return "action_play_game"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global score, over, correct, statements

        while over is False:
            for jix in range(len(statements)+1):
                if score < 16:
                    t = statements[jix]
                    intent = tracker.latest_message['intent'].get('name')
                    dispatcher.utter_message(str(t))

                    if intent == 'affirm':
                        if correct[jix] == 1:
                            score = score+1
                        else:
                            over = True
                    statements.pop(jix)
                    correct.pop(jix)

                    return [SlotSet("jix", jix), SlotSet("score", score), SlotSet("over", over)]
                else:
                    dispatcher.utter_message("15/15 Congratulations, you are a true Pickle Rick!!!")
                    dispatcher.utter_message("Do you want to play again?")
                    if tracker.latest_message['intent'].get('name') == "affirm":
                        over = False
                        score = 0
                        correct = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]
                        statements = stats()
                        return [Restarted()]
                    elif tracker.latest_message['intent'].get('name') == "deny":
                        dispatcher.utter_message("Thanks for playing.")
                        final_score = "Final score: " + str(score-1) + "/15"
                        dispatcher.utter_message(final_score)
                        return []

        dispatcher.utter_message("Game over. Would you maybe like to try once more?")
        if tracker.latest_message['intent'].get('name') == "affirm":
            over = False
            score = 0
            correct = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]
            statements = stats()
            return [Restarted()]
        elif tracker.latest_message['intent'].get('name') == "deny":
            dispatcher.utter_message("Thanks for playing.")
            final_score = "Final score: " + str(score-1) + "/15"
            dispatcher.utter_message(final_score)
            return []

class ActionGameB(Action):

    def name(self) -> Text:
        return "action_play_game_2"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global score, over
        global statements, correct

        while over is False:
            for jix in range(len(statements)+1):
                if score < 16:
                    t = statements[jix]
                    intent = tracker.latest_message['intent'].get('name')
                    dispatcher.utter_message(str(t))

                    if intent == 'deny':
                        if correct[jix] == 0:
                            score = score+1
                        else:
                            over = True
                    statements.pop(jix)
                    correct.pop(jix)
                    return [SlotSet("jix", jix), SlotSet("score", score), SlotSet("over", over)]
                else:
                    dispatcher.utter_message("15/15 Congratulations, you are a true Pickle Rick!!!")
                    dispatcher.utter_message("Do you want to play again?")
                    if tracker.latest_message['intent'].get('name') == "affirm":
                        over = False
                        score = 0
                        correct = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]
                        statements = stats()
                        return [Restarted()]
                    elif tracker.latest_message['intent'].get('name') == "deny":
                        dispatcher.utter_message("Thanks for playing.")
                        final_score = "Final score: " + str(score-1) + "/15"
                        dispatcher.utter_message(final_score)
                        return []

        dispatcher.utter_message("Game over..  Would you maybe like to try once more?")

        if tracker.latest_message['intent'].get('name') == "affirm":
            over = False
            score = 0
            correct = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]
            statements = stats()
            return [Restarted()]

        elif tracker.latest_message['intent'].get('name') == "deny":
            final_score = "Final score: " + str(score) + "/15"
            dispatcher.utter_message(final_score)
            return []

class GetScore(Action):
    def name(self) -> Text:
        return "action_get_score"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        score = tracker.get_slot("score")
        if score != None:
            player_score = "Your score: " + str(score-1) + "/15"
        else:
            player_score = "Your score: 0/15"

        dispatcher.utter_message(player_score)

        return []
