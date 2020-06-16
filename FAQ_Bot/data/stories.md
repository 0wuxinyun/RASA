## happy path
* mood_great
  - utter_happy

## sad path 1
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
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
 
## thank
* thank
  - utter_noworries
 
## Some question from FAQ
* faq
  - respond_faq
   
## sales form
* contact_sales
  - sales_form                   
  - form{"name": "sales_form"}   <!--Activate the form-->
  - form{"name": null}           <!--Deactivate the form-->