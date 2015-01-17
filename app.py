
# import the Flask class from the flask module
from flask import Flask, render_template, jsonify
from stock_scraper import get_data

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('mainPage.html')


# Generic route for MPs
@app.route('/mp/<mpName>')
def mp(mpName):
    from compute import do_compute
    do_compute()
    return render_template(mpName + '/index.html')


@app.route('/mp1')
def mp1():
    return render_template('mp1/index.html')  # render a template

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/data')
def data():
    return jsonify(get_data())

@app.route('/images')
def imagest():
    from imageSingle import get_image_data
    return jsonify(get_image_data())

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

