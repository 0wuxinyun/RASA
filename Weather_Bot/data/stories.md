## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## User introduction 
* user_introuction
  - utter_greet_user

## Ask Weather 1
* greet
  - utter_greet
* user_introuction
  - utter_greet_user
* ask_weather{"city": "Singapore"}
    - slot{"city": "Singapore"}
    - action_weather
    
* goodbye
    - utter_goodbye

## Generated Story -3351152636827275381
* greet
    - utter_greet
* ask_weather{"city": "London"}
    - slot{"city": "London"}
    - action_weather
* goodbye
    - utter_goodbye

## Ask weather 2
* greet
   - utter_greet
* ask_weather{"city":"Lithuania"}
   - slot{"city": "Lithuania"}
   - action_weather
* goodbye
   - utter_goodbye

## Ask Weather 3
* greet
  - utter_greet
* ask_weather{"city": "Singapore"}
    - slot{"city": "Singapore"}
    - action_weather
