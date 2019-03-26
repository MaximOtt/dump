from channels import Group
from channels.sessions import channel_session
import random
from .models import Player, Group as OtreeGroup, Constants
import json # This is important for messages
import time # This is important for the timer

def ws_connect(message, group_name):
    Group(group_name).add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message, group_name):
    # This is how you get the group id - don't touch
    group_id = group_name[5:]
    
    print('Got a message!')
    # Load message content into some weird format
    jsonmessage = json.loads(message.content['text'])
    
    # Extract IDs from the message
    curplayer_id = jsonmessage['id']
    curplayer_id_in_group = jsonmessage['id_in_group']
    
    # Get group and player object
    mygroup = OtreeGroup.objects.get(id=group_id)
    curplayer = mygroup.get_player_by_id(curplayer_id_in_group)
    
    ####################################
    # ONLY TOUCH STUFF AFTER THIS LINE #
    ####################################
    
    # Extract other data from message
    curplayer_new_answer = int(jsonmessage['new_answer'])
    
    # Do whatever calculations and other things you have to do
    curplayer.my_player_int_variable = curplayer_new_answer
    number_of_player_one = mygroup.get_player_by_id(1).my_player_int_variable
    number_of_player_two = mygroup.get_player_by_id(2).my_player_int_variable
    who_is_bigger = 1 if number_of_player_one > number_of_player_two else 2
    
    # Timer stuff
    now = time.time()
    mygroup.auctionenddate = now + Constants.extra_time
    
    # Save player and group object/fields - IMPORTANT STEP!
    # data can now be retrieved in the html!
    curplayer.save()
    mygroup.save()
    
    # Compose message to be sent back
    time_left = round(mygroup.auctionenddate - now)
    textforgroup = json.dumps({
                                "time_left": time_left, # obviously timer stuff
                                "number_of_player_one": mygroup.get_player_by_id(1).my_player_int_variable,
                                "number_of_player_two": mygroup.get_player_by_id(2).my_player_int_variable,
                                "biggest_number": mygroup.my_group_int_variable,
                                "player_whos_number_is_bigger": curplayer_id_in_group,
                                "text_I_want_to_send": "Player 1 has the bigger number",
                                })
    
    #####################################
    # ONLY TOUCH STUFF BEFORE THIS LINE #
    #####################################
    
    # Send the message back to the html
    Group(group_name).send({
        "text": textforgroup,
    })



# Connected to websocket.disconnect
def ws_disconnect(message, group_name):
    Group(group_name).discard(message.reply_channel)
