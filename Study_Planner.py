from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

subjects = []
exam_dates = []
plan = {}

def get_state():
    return {
        "subjects": subjects,
        "examDates": exam_dates,
        "plan": plan
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify(get_state())

@app.route("/api/subject", methods=["POST"])
def add_subject():
    data = request.json
    sub = data.get("subject")
    date = data.get("date")
    if sub and date:
        subjects.append(sub)
        exam_dates.append(date)
        return jsonify({"status": "ok", **get_state()})
    return jsonify({"error": "Invalid data"}), 400

@app.route("/api/subject/<int:index>", methods=["DELETE"])
def remove_subject(index):
    if 0 <= index < len(subjects):
        subjects.pop(index)
        exam_dates.pop(index)
        return jsonify({"status": "ok", **get_state()})
    return jsonify({"error": "Invalid index"}), 400

@app.route("/api/generate", methods=["POST"])
def generate():
    if len(subjects) == 0:
        return jsonify({"error": "Add subjects first"}), 400
    
    data = request.json
    hours_input = float(data.get("hpd", 6))
    today = datetime.today()

    weights = []
    total_weight = 0

    for date in exam_dates:
        exam = datetime.strptime(date, "%Y-%m-%d")
        days_left = (exam - today).days

        if days_left <= 0:
            days_left = 1

        weight = 1 / days_left
        weights.append(weight)
        total_weight += weight

    plan.clear()

    for i in range(len(subjects)):
        hours = (weights[i] / total_weight) * hours_input
        minutes = int(round(hours * 60, 0))
        plan[subjects[i]] = minutes

    return jsonify({"status": "ok", **get_state()})

@app.route("/api/save", methods=["POST"])
def save():
    data = {
        "subjects": subjects,
        "dates": exam_dates,
        "plan": plan
    }

    with open("study_plan.json", "w") as f:
        json.dump(data, f, indent=4)

    return jsonify({"status": "ok"})

@app.route("/api/load", methods=["POST"])
def load():
    global subjects, exam_dates, plan
    if not os.path.exists("study_plan.json"):
        return jsonify({"error": "No saved file found"}), 404
        
    try:
        with open("study_plan.json", "r") as f:
            data = json.load(f)

        subjects.clear()
        exam_dates.clear()
        plan.clear()

        subjects.extend(data.get("subjects", []))
        exam_dates.extend(data.get("dates", []))
        plan.update(data.get("plan", {}))

        return jsonify({"status": "ok", **get_state()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)