from flask import Flask,request, render_template
from python import Convert
from connect import addition,delete
app = Flask(__name__)
input=0
no=""
@app.route('/', methods=['GET'])
def number():
    return render_template('Input.html')

@app.route('/add', methods=['POST'])
def add():
    global input
    global no
    num = request.form.get('num')
    if num.strip() == '':   # Empty input
        return "<h1>Invalid number</h1>"
    elif ((int(num))>32767 or (int(num))<-32767):
        return "<h1>Invalid number</h1>"
    no=int(num)
    input = Convert(no)
    showtable=addition(num,input)
    num=""
    return render_template('answer.html', Convertofnum=input, num=no,records=showtable)

@app.route('/delete', methods=['POST'])
def erase():
    global input
    global no
    delet = request.form.get('ID') 
    showtable=delete(int(delet))
    return render_template('answer.html', Convertofnum=input, num=no,records=showtable)

if __name__ == '__main__':
    app.run(debug=True)


# from connect import addition
# from python import Convert
# input=int(input("Enter Number: "))

# addition(input,Convert(input))
# # print(Convert(-23))
