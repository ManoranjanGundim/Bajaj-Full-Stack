from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# your details
FULL_NAME = "Gundimi Manoranjan"
DOB = "05082004"
EMAIL = "mano.gundimi@gmail.com"
ROLL_NUMBER = "22BCE20153"

def alternating_caps_reverse(s):
    s = s[::-1]  # reverse string
    result = ""
    for i, ch in enumerate(s):
        if i % 2 == 0:
            result += ch.upper()
        else:
            result += ch.lower()
    return result

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get("data", [])
        
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_chars = []
        total_sum = 0
        concat_letters = ""

        for item in data:
            if item.isdigit():  # numbers
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                total_sum += num
            elif re.match("^[A-Za-z]+$", item):  # alphabets
                alphabets.append(item.upper())
                concat_letters += item
            else:  # special characters
                special_chars.append(item)

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum": str(total_sum),
            "concat_string": alternating_caps_reverse(concat_letters)
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
