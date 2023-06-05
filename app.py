# import the necessary modules
from flask import Flask , render_template , request , jsonify

# importing sentiment_analysis file as sa
import sentiment_analysis as sa

app = Flask(__name__)

# app route for index page
@app.route('/')
def home():
    return render_template('index.html')

# write a route for post request
@app.route('/predict' , methods = ['POST'])
def review():

    # extract the customer_review by writing the appropriate 'key' from the JSON data
    review = request.json.get('customer_review')

    # check if the customer_review is empty, return error
    if not review:

        
        response = jsonify({'status' : 'error' , 
                        'message' : 'Empty response'})

    # if review is not empty, pass it through the 'predict' function.
    # predict function returns 2 things : sentiment and path of image in static folder
    # example : Positive , ./static/assets/emoticons/positive.png

    else:
        sentiment,emoji_url = sa.predict(review)

        return jsonify({'status':'Succes' , 'prediction':sentiment,'url':emoji_url})
    return response



if __name__  ==  "__main__":
    app.run(debug = True)