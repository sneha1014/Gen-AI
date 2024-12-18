import os
from flask import Flask, request, jsonify
from groq import Groq
from flask_cors import CORS  # to enable frontend-backend communication

# Initialize the Groq API client
client = Groq(api_key="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")

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend access

@app.route("/", methods=["GET"])
def home():
    """
    Home route for basic status message.
    """
    return "Welcome to the Personalized Learning Assistant API!"

@app.route("/ask", methods=["POST"])
def ask_question():
    """
    Handles POST requests to answer user questions based on grade level.
    """
    # Get the JSON data from the request
    data = request.get_json()
    user_question = data.get("question", "")
    grade_level = data.get("grade_level", "middle school")

    try:
        # Use the Groq client to generate a response (replace with correct method for Groq)
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Assuming this is the correct model identifier for Groq
            messages=[
                {"role": "system", "content": f"You are a helpful learning assistant for {grade_level} students."},
                {"role": "user", "content": user_question}
            ],
            max_tokens=200  # Limit the response length
        )

        # Extract the answer from the API response
        answer = response.choices[0].message.content.strip().strip()
        return jsonify({"answer": answer})

    except Exception as e:
        # Handle errors and return an error message
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask app on port 5001
    app.run(host="127.0.0.1", port=5000)
