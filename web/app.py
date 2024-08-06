from flask import Flask, render_template, request, redirect, url_for
import json
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setup', methods=['POST'])
def setup():
    server_name = request.form['server_name']
    max_players = request.form['max_players']
    gamemode = request.form['gamemode']
    difficulty = request.form['difficulty']
    level_seed = request.form['level_seed']

    config = {
        "server_name": server_name,
        "max_players": int(max_players),
        "gamemode": gamemode,
        "difficulty": difficulty,
        "level_seed": level_seed
    }

    with open('config/server_defaults.json', 'w') as f:
        json.dump(config, f, indent=4)

    subprocess.run(['./setup.sh'])

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
