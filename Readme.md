# 🪨📄✂️ Stone Paper Scissor Game (Flask Web App)

A simple web-based **Stone Paper Scissors** game built using **Flask (Python)** as the backend and **HTML/CSS** for the frontend. Play against a bot, and see who wins!

---

### 🔗 Live Demo

👉 [Click here to play the game](https://stone-paper-scissor-game-96cs.onrender.com)

---

### 🧩 Features

- Built with Python Flask framework
- Play against the computer (random moves)
- Clean UI with images for Stone, Paper, and Scissors
- Responsive frontend using HTML and static image assets

---

### 📁 Folder Structure

```bash
stone_paper_scissor_game/
│
├── main.py # Main Flask app
├── requirements.txt # Python dependencies
├── Procfile # For deployment (Render)
├── .gitignore
│
├── /templates
│ └── index.html # Main HTML page
│
├── /static
│ └── /images # Game images (Stone.jpg, Paper.jpg, Scissors.jpg, logo.jpg)
│
├── /Scripts, /Include, /Lib, pyvenv.cfg # (Ignored virtual environment files)
```

---

### 🚀 How to Run Locally

Follow the steps below to run this Flask project on your local machine:

#### 1. Clone the repository

```bash
git clone https://github.com/murugappan18/Stone-Paper-Scissor-Game.git
cd stone_paper_scissor_game
```

#### 2. Create & activate a virtual environment (optional but recommended)

```bash
python -m venv venv
# Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```
#### 4. Run the Flask app

```bash
python main.py
```

Now visit http://127.0.0.1:5000 in your browser to play the game locally.

---

#### 🛠 Deployment
This project is deployed for free using Render. The Procfile and requirements.txt are already set up for easy deployment.

---

### Developed by Murugappan