from flask import Flask

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def test():
    return 'this is my Machine learning project and testing it'



if __name__ =='__main__':
    app.run(debug=True)