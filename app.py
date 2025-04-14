import os  
from flask import Flask, render_template, request

# Import OCR + translate functions from ocr.py
from ocr_core import ocr_core, translatee


# Define a folder to store and later serve the images
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to check the file extension
def allowed_file(filename):  
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for home page
@app.route('/')
def home_page():  
    return render_template('index.html')

# Route for upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():  
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            # Save the file
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Perform OCR and translation
            extracted_text = ocr_core(filepath)
            translated_text = translatee(extracted_text)

            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   translated_text=translated_text,
                                   img_src='/' + filepath)

    return render_template('upload.html')

if __name__ == '__main__':  
    app.run(debug=True)
