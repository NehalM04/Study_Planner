# 📚 StudyFlow — Smart Study Planner

An intelligent study planning web application that helps students efficiently allocate their daily study time based on upcoming exam dates.

Built using **Flask (Python)** for backend and a modern **HTML/CSS/JavaScript UI** for frontend.

---

## 🚀 Features

* 📌 Add subjects with exam dates
* 🧠 Smart study plan generation based on urgency
* ⏳ Automatic time allocation using weighted algorithm
* 📊 Visual daily study distribution
* 💾 Save and load study plans locally
* ❌ Remove subjects easily
* 🎨 Clean and modern UI with animations

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **Data Storage:** JSON file

---

## 📂 Project Structure

```
StudyFlow/
│── app.py
│── templates/
│   └── index.html
│── study_plan.json (generated after saving)
```

---

## ⚙️ How It Works

The system uses a **weighted algorithm**:

* Subjects with **closer exam dates get more study time**
* Formula used:

```
weight = 1 / days_left
```

* Study hours are distributed proportionally based on weights

---

## ▶️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/your-username/studyflow.git
cd studyflow
```

2. **Install dependencies**

```bash
pip install flask
```

3. **Run the app**

```bash
python app.py
```

4. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📌 API Endpoints

| Method | Endpoint            | Description         |
| ------ | ------------------- | ------------------- |
| GET    | `/api/data`         | Get current data    |
| POST   | `/api/subject`      | Add subject         |
| DELETE | `/api/subject/<id>` | Remove subject      |
| POST   | `/api/generate`     | Generate study plan |
| POST   | `/api/save`         | Save plan           |
| POST   | `/api/load`         | Load saved plan     |

---

## 💡 Future Improvements

* 🔐 User authentication system
* ☁️ Cloud database integration (MySQL/Firebase)
* 📱 Mobile responsiveness
* 📊 Progress tracking
* 🔔 Notifications

---

## 👨‍💻 Developed By

**Nehal Mehta**

---

## ⭐ Support

If you like this project, please ⭐ the repository!
