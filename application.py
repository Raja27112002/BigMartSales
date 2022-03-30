from flask import Flask, render_template, request
import getdata
import model
import data_transform

application = Flask(__name__)


@application.route('/', methods= ['GET', 'POST'])

def homePage():
    return render_template("index.html")

@application.route('/predict', methods= ['POST'])

def prediction():
    try:
        if (request.method == 'POST'):
            data = getdata.getdata()
            data2 = data_transform.data_transform()
            pred = model.prediction_(data, data2)


            print('prediction is',pred.predic)

            return render_template('results.html',prediction=pred.predic)

        else:

            return render_template('index.html')
    except Exception as e:
        return render_template('results.html',prediction=e)


if __name__ == "__main__":
    application.run(port=2500, debug=True)









