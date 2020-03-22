
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

statements = ["Never have I ever tried watching TV upside down.",
              "Never have I ever agreed with something Donald Trump said.",
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
              "Never have I ever tried a restaurant's food challenge.",
              "Never have I ever eaten a full frozen pizza by myself.",
              "Never have I ever counted calories.",
              "Never have I ever had to call the cops on someone.",
              "Never have I ever locked an animal in my car.",
              "Never have I ever lied during this game."]


player2_answers = [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1]

score = [11, 11]

class ActionGameA(Action):

    def name(self) -> Text:
        return "action_play_game"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        for jix in range(len(statements)-1):
            t = statements[jix]
            intent = tracker.latest_message['intent'].get('name')
            dispatcher.utter_message(t)

            if intent == 'affirm':
                score[0] = score[0]-1
                dispatcher.utter_message(str(score[0]))
            if player2_answers[jix] == 1:
                score[1] = score[1]-1
                dispatcher.utter_message(str(score[1]))

            statements.pop(jix)
            dispatcher.utter_message(str(statements))
            player2_answers.pop(jix)

            dispatcher.utter_message(str(player2_answers))

            return [SlotSet("jix", jix), SlotSet("score", score), SlotSet("intent_slot", intent)]


class ActionGameB(Action):

    def name(self) -> Text:
        return "action_play_game_2"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        for jix in range(0,len(statements)-1):
            t = statements[jix]
            dispatcher.utter_message(t)
            dispatcher.utter_message(str(score[0]))
            if player2_answers[jix] == 1:
                score[1] = score[1]-1
            dispatcher.utter_message(str(score[1]))
            statements.pop(jix)
            dispatcher.utter_message(str(statements))
            player2_answers.pop(jix)
            dispatcher.utter_message(str(player2_answers))

            return [SlotSet("jix", jix), SlotSet("score", score)]



class GetScore(Action):
    def name(self) -> Text:
        return "action_get_score"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        score = tracker.get_slot("score")
        player1 = "Player1: " + str(score[0])
        player2 = "Player2: " + str(score[1])

        dispatcher.utter_message(player1)
        dispatcher.utter_message(player2)

        return []
