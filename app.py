from flask import Flask, render_template
# create object of the class
app = Flask(__name__)
#create route (URL after domain name)
@app.route("/")
def hello_world():
  return render_template('home.html')

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
