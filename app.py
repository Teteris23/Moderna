from flask import Flask, render_template

app=Flask(__name__)
#<meta http-equiv="X-UA-Compatible" content="IE=edge">
@app.route("/",methods=['GET'])
def home():
    data=[
        ("1",1),
        ("2",1),
        ("3",1),
        ("4",1),
        ("5",1),
        ("6",1),
        ("7",1)
    ]

    labels=[row[0]for row in data]
    values=[row[1]for row in data]

    return render_template("graph.html",labels=labels, values=values)


if __name__ == '__main__':
  app.run()