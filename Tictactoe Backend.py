from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def sum(a, b, c):
    return a + b + c

def checkWin(xState, zState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            return "X"
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            return "O"
    return None

# game state (will reset on refresh)
xState = [0]*9
zState = [0]*9
turn = 1

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    global turn
    value = int(request.form["value"])
    
    if xState[value] == 1 or zState[value] == 1:
        return jsonify({"message": "Taken"})
    
    if turn == 1:
        xState[value] = 1
        turn = 0
    else:
        zState[value] = 1
        turn = 1

    winner = checkWin(xState, zState)
    return jsonify({"winner": winner, "turn": turn})

if __name__ == "__main__":
    app.run(debug=True)