from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def handle_command():
    command = request.json.get('command')
    if command == 'start_vacuum':
        # Start Vacuum code
        return 'Vacuum started', 200
    elif command == 'stop_vacuum':
        # Stop Vacuum code
        return 'Vacuum stopped', 200
    else:
        return 'Unknown command', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
