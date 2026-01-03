from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello! Server is working correctly."

@app.route('/api/analyze', methods=['GET'])
def analyze():
    # รับลิงก์จากหน้าเว็บ
    url = request.args.get('url')
    # ส่งข้อมูลปลอมๆ กลับไปก่อน (เพื่อเทสต์ว่าเชื่อมต่อได้)
    return jsonify({
        "status": "success",
        "title": "Test Song from Server",
        "artist": "Server Artist",
        "cover": "https://placehold.co/400"
    })

if __name__ == '__main__':
    app.run(debug=True)