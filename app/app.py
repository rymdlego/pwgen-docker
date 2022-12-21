from flask import Flask, request, jsonify
import random

app = Flask(__name__)

def get_password():
  adjectives = open("adj.txt", "r").read().splitlines()
  nouns = open("noun.txt", "r").read().splitlines()

  adjective = random.choice(adjectives)
  noun = random.choice(nouns) 
  number = format(random.randint(0,9999), '04')

  password = (f'{adjective}{noun}.{number}')

  return password

@app.route('/')
def hello_world():
  return get_password()

@app.route('/api/v1/passwords', methods=['GET'])
def count():
    if 'count' in request.args:
        count = int(request.args['count'])
    else:
        count = 1

    results = []

    for i in range(count):
        password = get_password()
        results.append({'id': i, 'password': password})

    return jsonify(results)
