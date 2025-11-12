from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime_number(number: int):
    prime_status = is_prime(number)  # <-- define it first
    message = f"{number} is a prime number." if prime_status else f"{number} is not a prime number."
    return jsonify({
        "Number": number,
        "isPrime": prime_status,
        "message": message
    })

if __name__ == '__main__':
    app.run(debug=True)
