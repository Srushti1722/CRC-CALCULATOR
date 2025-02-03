from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# CRC Calculation Logic
def calculate_crc(data, generator):
    """
    Calculate the CRC checksum using modulo-2 division.
    """
    # Check if data and generator are binary strings
    if not all(bit in '01' for bit in data) or not all(bit in '01' for bit in generator):
        raise ValueError("Data and generator must be binary strings containing only 0s and 1s.")

    # Append zeros to the data (length = len(generator) - 1)
    padded_data = list(data + '0' * (len(generator) - 1))
    generator = list(generator)

    # Perform modulo-2 division
    for i in range(len(data)):
        if padded_data[i] == '1':  # Only XOR when the leading bit is 1
            for j in range(len(generator)):
                padded_data[i + j] = str(int(padded_data[i + j]) ^ int(generator[j]))

    # Extract the remainder (last len(generator) - 1 bits)
    remainder = ''.join(padded_data[-(len(generator) - 1):])
    return remainder

@app.route('/')
def index():
    """
    Render the homepage with the form for data input.
    """
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Handle CRC calculation requests.
    """
    data = request.form.get('data')
    generator = request.form.get('generator')

    # Validate inputs
    if not data or not generator:
        return jsonify({'error': 'Please provide both data and generator polynomial!'})

    try:
        # Calculate CRC and transmitted frame
        crc = calculate_crc(data, generator)
        transmitted_frame = data + crc
        return jsonify({
            'data': data,
            'generator': generator,
            'crc': crc,
            'transmitted_frame': transmitted_frame
        })
    except ValueError as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
