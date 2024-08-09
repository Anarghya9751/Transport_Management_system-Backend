from datetime import datetime
import random
import string

def generate_id():
    return datetime.now().strftime("%Y%m%d%H%M%S") + ''.join(random.choice(string.ascii_uppercase) for _ in range(2))