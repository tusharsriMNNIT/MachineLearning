from flask import Flask, render_template, request, jsonify
import util


app = Flask(__name__)

@app.route('/')
def bhpindex():
    return render_template('bhpindex.html')

@app.route('/bhpform')
def bhpform():
    return render_template('bhpform.html')

@app.route('/bhppredict')
def bhppredict():
    area = request.args.get('area')
    bhk = request.args.get('bhk')
    bath = request.args.get('bath')
    loc = request.args.get('loc')
    
    price = float(util.get_estimated_price(loc,area,bhk,bath))

    return render_template('bhppredict.html', area=area, bhk=bhk, bath=bath, loc=loc, price=price)


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)