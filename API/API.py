from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load the saved model from the pickle file
loaded_model = pickle.load(open('../model/best_model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()
    
    # Convert the JSON data to a DataFrame
    df = pd.DataFrame.from_dict(data)

    print(df.columns)
    
    # Make predictions using the loaded model
    predictions = loaded_model.predict(df)
    
    # Prepare the predictions as a JSON response
    response = {'predictions': predictions.tolist()}
    
    # Return the JSON response
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)