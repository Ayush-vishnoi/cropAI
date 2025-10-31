from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
from database import supabase 

app = Flask(__name__)
CORS(app)

@app.route("/test-db", methods=["GET"])
@app.route("/test-db", methods=["POST"])
def test_db():
    try:
        response = supabase.table("predictions").insert({
            "user_id": "test_user_123",
            "state": "Uttar Pradesh",
            "crop": "Wheat",
            "temperature": 25,
            "humidity": 60,
            "rainfall": 100,
            "predicted_yield": 2000,
            "irrigation_alert": "NO IRRIGATION NEEDED",
            "created_at": datetime.utcnow().isoformat()
        }).execute()

        return jsonify({
            "status": "ok",
            "message": "Test record inserted successfully!",
            "data": response.data
        }), 200

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"status": "error", "error": str(e)}), 500


@app.route("/")
def home():
    return jsonify({"message": "🚀 CropAI Flask API connected to Supabase!"})


if __name__ == "__main__":
    app.run(debug=True)
