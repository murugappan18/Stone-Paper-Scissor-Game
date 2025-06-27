from flask import Flask, render_template, request
import random

app = Flask(__name__)

user_count, bot_count = 0, 0
name = None
imgs = ['Rock.jpg', 'Paper.jpg', 'Scissors.jpg']

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit(): 
    global name  
    msg = f"Hello👋 {name}, Choose your Next Move ⏩!"
    if request.form.get('username'):
        name = request.form.get('username')
        msg=f"Hello👋, {name}! Choose Your Move ✅!"
    return render_template('index.html', msg=msg, name=name, imgs=imgs)

@app.route('/game', methods=['POST'])
def game():
    global user_count, bot_count, name

    ind = int(request.form.get('ind'))
    sel_img = []
    sel_img.append(imgs[ind])
    sel_img.append(random.choice(imgs))
    msg = "Hello👋!"
    if sel_img[0] == sel_img[1]:
        msg = "Draw 😐, Retry 🔄️"
    elif (sel_img[0] == 'Paper.jpg' and sel_img[1] == 'Rock.jpg') or (sel_img[0] == 'Rock.jpg' and sel_img[1] == 'Scissors.jpg') or (sel_img[0] == 'Scissors.jpg' and sel_img[1] == 'Paper.jpg'):
        user_count += 1
        msg = f"{name}🫅 Win!"
    elif (sel_img[0] == 'Paper.jpg' and sel_img[1] =='Scissors.jpg') or (sel_img[0] == 'Rock.jpg' and sel_img[1] == 'Paper.jpg') or (sel_img[0] == 'Scissors.jpg' and sel_img[1] == 'Rock.jpg'):
        bot_count += 1
        msg = "Bot🤖 Win!"
    else:
        msg = "Undefined"

    win_msg = None
    if user_count >= 3 or bot_count >= 3:
        if user_count >= 3:
            win_msg = f"Congratulations🎉 {name}, You are the Winner🫅!"
        else:
            win_msg = f"Better Luck Next time🤝 {name}, Bot🤖 Wins!"
        tu_cnt, tb_cnt = user_count, bot_count
        user_count, bot_count = 0, 0
        return render_template('index.html', win_msg=win_msg, name=name, tu_cnt=tu_cnt, tb_cnt=tb_cnt, msg=f"{win_msg}", sel_img=None, imgs=None)

    return render_template('index.html', msg=msg, sel_img=sel_img, user_count=user_count, bot_count=bot_count, name=name, imgs=None)

if __name__ == '__main__':
    app.run(debug=True)