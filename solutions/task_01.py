def print_first_chars():
    '''
    1. Írassa ki új sorba a message string minden szavának 
    kezdőbetűjét a string metódusai és vágási műveletei segítségével!
    (Minden karakter új sorban legyen.)
    '''
    message = 'Hello, this is a test message.'
    parts = message.split(' ')
    for word in parts:
        print(word[0:1])
