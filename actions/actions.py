
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionObtenerDefinicion(Action):
    def name(self) -> Text:
        return "action_obtener_definicion"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        subtema = next(tracker.get_latest_entity_values("subtema"), None)
        if subtema:
            response = "respondiendo duda de concepto de: " + subtema
        else:
            response = "Lo lamento. No entendi el tema sobre el que tenes una duda. "\
                       "Por favor intenta nuevamente."
        dispatcher.utter_message(text=response) 
        return [SlotSet("subtema", subtema if subtema is not None else [])]


class ActionRecibirTema(Action):
    def name(self) -> Text:
        return "action_recibir_tema"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        subtema = next(tracker.get_latest_entity_values("subtema"), None)
        dispatcher.utter_message(text="Ok.") 
        return [SlotSet("subtema", subtema if subtema is not None else [])]
