## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_range": "mid"}
    - slot{"price_range": "mid"}
    - action_search_restaurants
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "mysore"}
    - slot{"location": "mysore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* price{"price_range": "mid"}
    - slot{"price_range": "mid"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "bangalore", "price_comp": "under", "price1": "400"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "bangalore"}
    - slot{"price1": "400"}
    - slot{"price_comp": "under"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "pune", "price_comp": "over", "price2": "700"}
    - slot{"location": "pune"}
    - slot{"price2": "700"}
    - slot{"price_comp": "over"}
    - utter_ask_cuisine
* cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_search_restaurants
* affirm{"farewell": "nice"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "hyderabad", "cuisine": "north indian", "price_range": "high"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "hyderabad"}
    - slot{"price_range": "high"}
    - action_search_restaurants
    - utter_ask_feedback
* restaurant_search{"price_comp": "under", "price2": "900"}
    - slot{"price2": "900"}
    - slot{"price_comp": "under"}
    - action_search_restaurants
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* location{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - utter_ask_price
* price{"price_comp": "above", "price2": "650"}
    - slot{"price2": "650"}
    - slot{"price_comp": "above"}
    - action_search_restaurants
    - utter_ask_feedback
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_2
    - utter_greet
* goodbye
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* location{"location": "mysore"}
    - slot{"location": "mysore"}
    - utter_ask_price
* price{"price_range": "mid"}
    - slot{"price_range": "mid"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_feedback
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* price{"price_range": "low"}
    - slot{"price_range": "low"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_feedback
* affirm
    - utter_goodbye
