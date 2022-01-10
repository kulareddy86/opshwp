from flask import Flask

app=Flask(__name__)


@app.route('/')
def kula():
    return 'welcome to IT world'



if __name__=='__main__':
    app.run(debug=True)