
import random 
import string 
from datetime import datetime


#tick data
def generate_message() -> dict:
    book_type = random.randint(1, 2)
    dtime = datetime.now().strftime('%d/%m/%Y %H:%M')
    price = round(random.uniform(10.01, 10.50), 2) #random.randint()
    volume = random.randint(1, 10)
    volume_dbl = random.randrange(100)
    
    return {
        'book_type': book_type,
        'time': dtime,
        'price': price,
        'volume': volume,
        'volume_dbl': volume_dbl
    }

#variação tick
def generate_message() -> dict:
    book_type = random.randint(1, 2)
    dtime = datetime.now().strftime('%d/%m/%Y %H:%M')
    price = round(random.uniform(10.01, 10.50), 2) #random.randint()
    volume = random.randint(1, 10)
    volume_dbl = random.randrange(100)
    tick_data = {
        'book_type': book_type,
        'time': dtime,
        'price': price,
        'volume': volume,
        'volume_dbl': volume_dbl
    }
    return tick_data

#book data
def generate_message2() -> dict:
    orderbook = [{'book_type': random.randint(1, 2), 
                 'dtime': datetime.now().strftime('%d-%m-%Y %H:%M:%S'), 
                 'price': round(random.uniform(10.01, 10.50), 2),
                 'volume': random.randint(1, 10),
                 'volume_dbl': random.randrange(100)
                 },
                 {'book_type': random.randint(1, 2), 
                 'dtime': datetime.now().strftime('%d-%m-%Y %H:%M:%S'), 
                 'price': round(random.uniform(10.01, 10.50), 2),
                 'volume': random.randint(1, 10),
                 'volume_dbl': random.randrange(100)
                 },
                 {'book_type': random.randint(1, 2), 
                 'dtime': datetime.now().strftime('%d-%m-%Y %H:%M:%S'), 
                 'price': round(random.uniform(10.01, 10.50), 2),
                 'volume': random.randint(1, 10),
                 'volume_dbl': random.randrange(100)
                 },
                 {'book_type': random.randint(1, 2), 
                 'dtime': datetime.now().strftime('%d-%m-%Y %H:%M:%S'), 
                 'price': round(random.uniform(10.01, 10.50), 2),
                 'volume': random.randint(1, 10),
                 'volume_dbl': random.randrange(100)
                 },
                 {'book_type': random.randint(1, 2), 
                 'dtime': datetime.now().strftime('%d-%m-%Y %H:%M:%S'), 
                 'price': round(random.uniform(10.01, 10.50), 2),
                 'volume': random.randint(1, 10),
                 'volume_dbl': random.randrange(100)
                 }]
    
    return orderbook
