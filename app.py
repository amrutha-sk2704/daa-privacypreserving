from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the processed dataset
dataset_path = r"C:\Users\LENOVO T 470S\OneDrive - Amrita vishwa vidyapeetham\Desktop\daa-prj\web_app\processed_dataset.csv"
data = pd.read_csv(dataset_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-data', methods=['GET'])
def get_data():
    """Serve the anonymized dataset."""
    return jsonify(data.to_dict(orient='records'))

@app.route('/visualization', methods=['GET'])
def visualization():
    """Serve privacy-utility visualization (To be implemented)."""
    return jsonify({'message': 'Visualization endpoint coming soon!'})

if __name__ == '__main__':
    app.run(debug=True)
