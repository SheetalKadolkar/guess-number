from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "change-this-to-a-secure-random-string"  # replace in production


def ensure_game():
    # Make sure a target number and attempt count exist in the session
    if "target" not in session:
        session["target"] = random.randint(1, 100)
        session["attempts"] = 0
        session["history"] = []


@app.route("/", methods=["GET", "POST"])
def index():
    ensure_game()
    message = None
    result = None

    if request.method == "POST":
        guess_raw = request.form.get("guess", "").strip()
        if not guess_raw.isdigit():
            message = "Please enter a number between 1 and 100."
        else:
            guess = int(guess_raw)
            session["attempts"] = session.get("attempts", 0) + 1
            session.modified = True

            target = session["target"]

            if guess < target:
                result = "low"
                message = f"{guess} is too low."
            elif guess > target:
                result = "high"
                message = f"{guess} is too high."
            else:
                result = "correct"
                message = (
                    f"🎉 Correct — {guess}! You guessed it in {session['attempts']} attempts."
                )

            # store history for small feedback
            history = session.get("history", [])
            history.append({"guess": guess, "result": result})
            session["history"] = history

            # if correct, keep the success message but allow resetting
            if result == "correct":
                # leave target in session (or could remove)
                pass

    return render_template(
        "index.html",
        message=message,
        result=result,
        attempts=session.get("attempts", 0),
        history=session.get("history", []),
    )


@app.route("/reset", methods=["POST"])
def reset():
    # Start a new game
    session.pop("target", None)
    session.pop("attempts", None)
    session.pop("history", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    # For local development only
    app.run(host="0.0.0.0", port=5000, debug=True)
