from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from static.etf_parsing import *

app = Flask(__name__)
CORS(app, resources={r"/api/*"})

@app.route('/api', methods=['GET', 'POST'])
def get_stock_data():

    # JSON 형태로 전달된 데이터 받기
    request_data = request.get_json()

    # 전달된 데이터에서 필요한 값 추출
    stock = request_data['stock']
    start_date = request_data['startDate']
    end_date = request_data['endDate']
    
    data = stock_df(stock)
    
    result_data = []
    

    # 검색 결과를 이용해 결과 데이터 생성
    for item in data:
        if item['date'] >= start_date and item['date'] <= end_date:
            result_data.append(item)

    # 결과 데이터 JSON 형태로 반환
    return jsonify({'data': result_data})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)