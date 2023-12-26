from flask import Flask, request, app
from handlers.elastic_search_sales_handler import ElasticSearchSalesHandler


app = Flask(__name__)
elasticsearch = ElasticSearchSalesHandler()


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        data = request.json
        response = elasticsearch.search(data)
        return response
    else:
        return {}


@app.route('/sum-sales', methods=['GET'])
def sum_sales():
    return elasticsearch.sumSales()


@app.route('/analyze-trends', methods=['GET'])
def analyze_trends():
    interval = request.args.get('interval')
    if interval is None:
        interval = 'day'
    return elasticsearch.analyze_trends_over_time(interval)



if __name__ == '__main__':
    app.run(port=8000, debug=True)