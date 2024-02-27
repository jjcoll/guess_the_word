from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    session,
    redirect,
    url_for,
)
from app.hangman import choose_word, read_word_list, print_board, check_board

# Create a Blueprint for routes
bp = Blueprint("routes", __name__)


# Generate new board and words
def start_new_game(wordfile):

    words = read_word_list(wordfile)
    word = choose_word(words)
    lives = 6

    # allow words with spaces
    board = []
    for letter in word:
        if letter != " ":
            board.append("_")
        else:
            board.append(" ")

    # store in session so they can be accessed outside the scope of this function
    # and like this we create a new board and word each session
    session["word"] = word
    session["board"] = board
    session["lives"] = lives
    session["won"] = 0
    return word, board, lives


# Define routes
@bp.route("/")
def index():

    letters = "abcdefghijklmnopqrstuvwxyz"
    letters_list = list(letters)

    # Keep the previous gamemode by default
    print(session.keys())
    if "wordsfile" in session.keys():
        start_new_game(session["wordsfile"])

        # here

    else:
        start_new_game("200words.txt")
        session["wordsfile"] = "200words.txt"

    return render_template(
        "index.html",
        letters_list=letters_list,
        board=print_board(session["board"]),
        lives=session["lives"],
        wordlist=session["wordsfile"],
    )


@bp.route("/guess", methods=["POST"])
# we have to pass board and word directly, due to race conditions
def guess_letter():

    board = session["board"]
    word = session["word"]
    previous_lives = session["lives"]

    slected_letter = request.json.get("letter")
    board, lives, won = check_board(slected_letter, board, word, previous_lives)

    # redirect the user because he has won
    # if won:
    #     return redirect(url_for("routes.game_over", outcome="win"))

    # update session
    session["board"] = board
    session["lives"] = lives

    if lives != previous_lives:
        update_lives = True
    else:
        update_lives = False

    # print(request.json)

    # return updated word to client
    return jsonify(
        {
            "updatedWord": print_board(board),
            "updateLives": update_lives,
            "lives": lives,
            "won": won,
        }
    )


@bp.route("/game-over")
def game_over():

    outcome = request.args.get("outcome")
    # validate that the user has won by looking at the session

    # I would like to make sure the user can only access this when
    # he actually wins or loses
    if outcome == "win":
        return render_template("gameover-win.html", lives=session["lives"])
    else:
        return render_template("gameover-lose.html", word=session["word"])


@bp.route("/about")
def about():
    print(session["theme"])
    return render_template("about.html")


@bp.route("/change-wordlist", methods=["POST"])
def change_wordlist():
    words_file = request.json.get("wordsfile")
    session["wordsfile"] = words_file

    start_new_game(words_file)

    print(session["wordsfile"])

    return jsonify(
        {
            "updatedWord": print_board(session["board"]),
            "updateLives": False,
            "lives": session["lives"],
            "won": session["won"],
            "wordsfile": session["wordsfile"],
        }
    )


@bp.route("/change-theme", methods=["POST"])
def change_theme():
    theme = request.json.get("theme")
    session["theme"] = theme
    return jsonify({"works": True})


@bp.route("/theme", methods=["GET"])
def update_theme():
    print(f"Sesssion theme: {session['theme']}")
    if "theme" in session.keys():
        return jsonify({"theme": session["theme"]})
    else:
        return jsonify({"theme": 0})
