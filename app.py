from flask import flask

app = Flast (__name__)

@app.route('/'(methods={'GET'}))
def helloworlkd():
    return 'Hello Worls'

if __name__=="__main__":
    app.run(port=3000, debug=True)
    
           

