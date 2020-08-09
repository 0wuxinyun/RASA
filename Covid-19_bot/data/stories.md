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

## Ask  1
* greet
  - utter_greet
* ask_total_confirmed{"country": "singapore"}
    - slot{"country": "singapore"}
    - action_confirmed
* goodbye
    - utter_goodbye

## Ask 2 
* greet
  - utter_greet
* ask_total_confirmed{"country": "china"}
    - slot{"country": "china"}
    - action_confirmed

## Ask  3
* greet
  - utter_greet
* ask_total_confirmed{"country": "finland"}
    - slot{"country": "finland"}
    - action_confirmed
* goodbye
    - utter_goodbye

## Ask  4
* ask_total_confirmed{"country": "japan"}
    - slot{"country": "japan"}
    - action_confirmed
* goodbye
    - utter_goodbye

## Ask  5
* ask_total_confirmed{"country": "lithuania"}
    - slot{"country": "lithuania"}
    - action_confirmed

## Ask  6
* ask_total_confirmed{"country": "canada"}
    - slot{"country": "canada"}
    - action_confirmed

## New Story

* greet
    - utter_greet
* ask_total_confirmed{"country":"china"}
    - slot{"country":"china"}
    - action_confirmed
