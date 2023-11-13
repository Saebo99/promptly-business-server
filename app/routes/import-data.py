from quart import Quart, request, jsonify
import PyPDF2
import io

app = Quart(__name__)

@app.route('/import-data', methods=['POST'])
async def import_data():
    # Check if the post request has the file part
    if 'file' not in await request.files:
        return jsonify({'error': 'No file part'}), 400

    file = (await request.files)['file']

    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        try:
            # Read the PDF file
            pdf_file = io.BytesIO(await file.read())
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            num_pages = pdf_reader.numPages
            return jsonify({'message': f'PDF processed, number of pages: {num_pages}'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

if __name__ == '__main__':
    app.run(debug=True)
