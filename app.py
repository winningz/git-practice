from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pickle
import numpy as np

'''
이미지 업로드로 받으면/
그 이미지를 다시 패키징 파일로 넘겨주고!(.png 검색 조건으로!)
결과값을 뱉어!


'''

model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)


# 업로드 HTML 렌더링
@app.route('/upload')
def render_file():
    return render_template('upload.html')

# 파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # 저장할 경로 + 파일명
        f.save(secure_filename(f.filename))
        print(type(f))
        print(f)

        return 'uploads 디렉토리 -> 파일 업로드 성공!'


# 모델 인퍼런스
@app.route('/model_inference')
def model_inference():
    

    return 1

if __name__ == "__main__":
    app.run(debug=True)