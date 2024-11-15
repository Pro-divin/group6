import os
import pyodbc
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# Define connection string to SQL Server
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=DESKTOP-AAO6T7J\SQLEXPRESS;'
    r'DATABASE=assignment;'
    r'Trusted_Connection=yes;'
)

# Route for the upload page
@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No file part'
    
    file = request.files['image']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        # Read image file data
        image_data = file.read()  # Get image data
        filename = file.filename    # Get image filename

        # Save the image to the SQL Server database
        try:
            conn = pyodbc.connect(conn_str)  # Establish SQL connection
            cursor = conn.cursor()
            sql = "INSERT INTO Images (imageData, filename) VALUES (?, ?)"
            cursor.execute(sql, (image_data, filename))
            conn.commit()
            return redirect(url_for('success'))  # Redirect on success
        except Exception as e:
            return f"An error occurred: {e}"
        finally:
            cursor.close()
            conn.close()

@app.route('/success')
def success():
    return 'Image uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)  # Run the application
