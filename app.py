from flask import Flask, render_template, request, jsonify
from algorithms import dijkstra, a_star

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pathfind', methods=['POST'])
def pathfind():
    data = request.get_json()
    algorithm = data.get('algorithm')
    grid = data.get('grid')
    start = tuple(data.get('start'))
    end = tuple(data.get('end'))

    if algorithm == 'dijkstra':
        path = dijkstra(grid, start, end)
    elif algorithm == 'a_star':
        path = a_star(grid, start, end)
    else:
        return jsonify({'error': 'Invalid algorithm'})

    return jsonify({'path': path})

if __name__ == '__main__':
    app.run(debug=True)
