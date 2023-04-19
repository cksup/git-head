message = ['spam', 'ham', 'spam', 'ham', 'spam']

dummy = [ 1 for msg in message if msg == 'spam' else 0 ]