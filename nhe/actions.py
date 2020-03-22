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

player2_answers = (1,0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0)

class ActionGame(Action):

    def name(self) -> Text:
        return "action_play_game"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        player1 = 10
        player2 = 10
        while player1 >= 1 or player2 >= 1:
            for i in range(len(statements)-1):
                t = statements[i]
                intent= tracker.get_slot("intent_slot")
                dispatcher.utter_message(t)
                if player2_answers[i] == 1:
                    player2 = player2-1

                elif intent == "affirm":
                    player1 = player1-1
                    return [SlotSet("player1", player1), SlotSet("player2", player2), SlotSet('intent_slot', intent)]
        dispatcher.utter_message("You have reached the end of this game. Final score: ","player1", player1,"player2 ", player2)
