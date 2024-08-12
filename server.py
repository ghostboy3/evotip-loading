from flask import Flask, request
import RPi.GPIO as GPIO
import time
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
led_pin = 18
GPIO.setup(led_pin, GPIO.OUT)

@app.route('/command', methods=['POST'])
def handle_command():
    command = request.json.get('command')
    if command == 'start_vacuum':
        # Start Vacuum code
        GPIO.output(led_pin, GPIO.HIGH)
        return 'Vacuum started', 200
    elif command == 'stop_vacuum':
        # Stop Vacuum code
        GPIO.output(led_pin, GPIO.LOW)
        return 'Vacuum stopped', 200
    else:
        return 'Unknown command', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

GPIO.cleanup()