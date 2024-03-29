from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
model = pickle.load(open('randomForest_clssify_model.pkl', 'rb'))
vect = pickle.load(open('vectorize.pkl', 'rb'))
tfidf = pickle.load(open('tfidfTransformer.pkl', 'rb'))


@app.route("/", methods=['Get'])
def home():
    return render_template('index.html')


standard_to = StandardScaler()


@app.route("/predict", methods=['Post'])
def predict():
    review = []
    keyword = ['food', 'hotel', 'staff', 'service', 'parking', 'floor', 'cleaning', 'rooms']

    if request.method == 'POST':
        review.append(request.form['review'])
        newReview = vect.transform(review)
        finalData = tfidf.transform(newReview)
        if review[0] != '':
            prediction = int(model.predict(finalData))

            review = review[0].split()

            kword = [word for word in review if word in keyword]
            
            if prediction == 0:
                return render_template('index.html', prediction='provided review is {}, rating should be 1 or 2, review is about {}'.format('Negative', ", ".join(word for word in kword)))

            elif prediction == 1:
                return render_template('index.html', prediction='Provide review is {}, rating should be 3, review is about {}'.format('Neutral', ", ".join(word for word in kword )))

            else:
                return render_template('index.html', prediction='Provide review is {}, rating should be 4 or 5, review is about {}'.format('Positive', ", ".join(word for word in kword )))
        else:
            return render_template('index.html', prediction='please provide a review')

if __name__ == "__main__":
    app.run(debug=True)


