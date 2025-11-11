🎯 Guess The Number Game (Python + Flask)
A fun and simple number guessing web app built using Python Flask.
The player tries to guess a randomly generated number between 1 and 100, with hints like “Too High”, “Too Low”, or “Correct!”.

📸 Screenshot

🌟 Features
🔢 Random number generation on each game start
🧠 Real-time feedback — “Too High”, “Too Low”, or “Correct!”
🌐 Simple Flask-based web interface
🐳 Dockerized for easy setup and deployment

📂 Project Setup
🧭 Clone the Repository
bash
Copy code
git clone https://github.com/sheetalkadolkar/guess-number.git
cd guess-number

⚙️ How to Run the Project Locally
1️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
2️⃣ Activate the Virtual Environment
# Windows
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the Flask App
bash
Copy code
python app.py
5️⃣ Open the Game in Your Browser
Visit: 👉 http://127.0.0.1:5000
🐳 Run Using Docker
1️⃣ Build the Docker Image
bash
Copy code
docker build -t docker.io/sheetalkadolkar/guess-number .
2️⃣ Run the Container
bash
Copy code
docker run -d -p 5000:5000 docker.io/sheetalkadolkar/guess-number
3️⃣ Open in Browser
http://localhost:5000

🧱 Project Structure
guess-number/
│
├── app.py                 # Flask application
├── templates/
│   └── index.html         # Game interface
├── static/
│   └── style.css          # Optional styling
├── requirements.txt       # Python dependencies
└── Dockerfile             # Docker configuration

🌍 Access After Deployment
Once containerized and running, open:
👉 http://localhost:5000

🧠 Learning Goals
Understand Flask basics
Learn how to containerize Python web apps
Practice using Docker and GitHub
