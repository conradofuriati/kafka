import random 
import string 
from datetime import datetime

user_ids = list(range(1, 101))
recipient_ids = list(range(1, 101))

def generate_message() -> dict:
    random_user_id = random.choice(user_ids)

    # Copy the recipients array
    recipient_ids_copy = recipient_ids.copy()

    # User can't send message to himself
    recipient_ids_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids_copy)

    # Generate a random message
    message = ''.join(random.choice(string.ascii_letters) for i in range(32))
    dtime = datetime.now().strftime('%d/%m/%Y %H:%M')

    return {
        'user_id': random_user_id,
        'recipient_id': random_recipient_id,
        'time': dtime,
        'message': message
    }
    