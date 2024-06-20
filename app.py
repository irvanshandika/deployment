from flask import Flask, request, render_template, redirect, url_for
import tensorflow as tf
import numpy as np
import cv2
import os
from werkzeug.utils import secure_filename

# Load the trained model
model = tf.keras.models.load_model('best_model.h5')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/faq')
def faq():
    return render_template('faq.html', title="FAQ's")

@app.route('/klasifikasi')
def klasifikasi():
    return render_template('klasifikasi.html')

@app.route('/pendahuluan')
def pendahuluan():
    return render_template('pendahuluan.html')

# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(url_for('home'))
    
    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return redirect(url_for('home'))

    if file:
        # Save the uploaded file
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)

        # Read and preprocess the image
        img = cv2.imread(image_path)
        img = cv2.resize(img, (128, 128))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        # Make a prediction
        prediction_prob = model.predict(img)[0]
        class_names = ['Normal', 'Tuberculosis']
        predicted_class = class_names[np.argmax(prediction_prob)]
        accuracy = np.max(prediction_prob) * 100

        return render_template('result.html', prediction=predicted_class, accuracy=accuracy, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
