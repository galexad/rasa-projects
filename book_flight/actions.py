# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class BookingForm(FormAction):

    def name(self) -> Text:
        return "booking_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["from", "to", "date", "n_pass"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {"to": [self.from_entity(entity="to"),
                         self.from_text()],
            "from": [self.from_entity(entity="from"),
                         self.from_text()],
            "date": [self.from_entity(entity="date"),
                         self.from_text()],
             "n_pass": [self.from_entity(entity="n_pass"),
                         self.from_text()]}


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(template="utter_submit")
        return []
