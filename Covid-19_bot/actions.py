# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import http.client
import mimetypes
import requests

class ActionConfirmed(Action):
        def name(self):
            return 'action_confirmed'

        def run(self, dispatcher, tracker, domain):
            loc = tracker.get_slot('country')
            api_address='https://api.covid19api.com/country/{}/status/confirmed'.format(loc) 
            total = requests.get(api_address).json()
            today=total[-1]
            case=today['Cases']
            response = "The total confirmed case in {} is {}".format(loc, case)
            dispatcher.utter_message(response)
            return []
