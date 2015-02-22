import bottle
import json


@bottle.get('/')
def index():
    return """
        <a href="https://github.com/sendwithus/battlesnake-python">
            battlesnake-python
        </a>
    """


@bottle.post('/start')
def start():
    data = bottle.request.json

    return json.dumps({
        'name': 'aspkickers',
        'color': '#00ffff',
        'head_url': 'http://i.imgur.com/jhitWnu.png',
        'taunt': 'There\'s a snake in my boot!'
    })


@bottle.post('/move')
def move():
    data = bottle.request.json

    print data['snakes']
    print data['food']

    oursnake_index = 0
    oursnake_head = [,]

    for index in range(len(data['snakes'])):
      if(data['snakes'][index] == 'aspkickers'):
        oursnake_index = index

    oursnake_head = data['snakes'][oursnake_index]['coords'][0]

    print data['snakes'][oursnake_index]['coords']
    print oursnake_head
    print data['food']

    
    all_snakes = []
    # for snake in snakes
    for snake in data['snakes']:
      for coord in snake['coords']:
        all_snakes.append(coord)

    print all_snakes
      

    # get coordinates 
    # accumulate coordinates


    return json.dumps({
        'move': 'right',
        'taunt': 'You\'re my favourite deputy!'
    })

#def isWall(point):




@bottle.post('/end')
def end():
    data = bottle.request.json

    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
