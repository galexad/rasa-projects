# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import random

JOKES = [("Doctor", "lol"),
         ("Deja", "Hahaha"),
	 ("Alex","Alex-plain when you open the door!"),
	 ("Pasta", "Pasta salt please!"),
	 ("Broken pencil", "Never mind, there’s no point."),
	 ("A herd", "A herd you inside, open up!"),
	 ("Cereal", "Ce-real pleasure to see you!"),
	 ("who","What is this, Harry Potter’s Sanctuary for Injured Owls?"),
	 ("Ice cream soda","Ice Cream Soda whole neighborhood can hear!"),
	 ("Razor", "Razor hands and dance the boogie!"),
	 ("Roach","Roach you a poem but decided on a knock knock joke instead.")]
jokes = []

class ActionJokeSetup(Action):

    def name(self) -> Text:
        return "action_joke_setup"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        for jix in range(0,len(JOKES)+1):
            if JOKES[jix] not in jokes:
                t = JOKES[jix][0]
                jokes.append(JOKES[jix])
                dispatcher.utter_message(t)
                return [SlotSet("jix", jix), SlotSet("jokes", jokes)]

            if len(jokes) == len(JOKES):
               jokes.clear()

class ActionJokePunchline(Action):

    def name(self) -> Text:
        return "action_joke_punchline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        jix = int(tracker.get_slot("jix"))
        joke = JOKES[jix]

        dispatcher.utter_message(text=joke[1])

        return []
