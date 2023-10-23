import random

response_table = dict()

def create_response_table():
    response_table = {'help':"`git gud`",
                      'roll':str(random.randint(1,6)),
                      'hello dingus':'Hello There!'}
    print(response_table)

def handle_response(message) -> str:
    return response_table.get(message.lower(), "???")