from flask import *
import os
from werkzeug.utils import secure_filename
import label_image

def load_image(image):
    text = label_image.main(image)
    return text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        # Make prediction
        result = load_image(file_path)
        result = result.title()
        d = {"no dr":"✓",'Mild':"❌","Moderate":"❌","Severe":"❌","proliferative dr":"❌"}
        result = result+d[result]
	#result = [result]
        print(result)
        os.remove(file_path)
        return result
    return None

if __name__ == '__main__':
    app.run()