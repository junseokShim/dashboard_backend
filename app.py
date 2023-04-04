from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, resources={r"/api/*"})

@app.route('/api', methods=['GET', 'POST'])
def get_stock_data():

    # JSON 형태로 전달된 데이터 받기
    request_data = request.get_json()
    print(f"gd: {request_data}")

    # 전달된 데이터에서 필요한 값 추출
    stock = request_data['stock']
    start_date = request_data['startDate']
    end_date = request_data['endDate']
    

    # 해당 데이터를 이용해 데이터베이스에서 데이터 검색

    # 샘플 데이터 생성 (실제로는 데이터베이스에서 데이터를 가져와야 함)
    data = [
        {'date': '2023-04-01', 'price': 100},
        {'date': '2023-04-02', 'price': 105},
        {'date': '2023-04-03', 'price': 95},
        {'date': '2023-04-04', 'price': 110},
        {'date': '2023-04-05', 'price': 115},
    ]

    

    result_data = []

    # 검색 결과를 이용해 결과 데이터 생성
    for item in data:
        if item['date'] >= start_date and item['date'] <= end_date:
            result_data.append(item)

    # 결과 데이터 JSON 형태로 반환
    return jsonify({'data': result_data})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)