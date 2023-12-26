from typing import Dict, Any
from elasticsearch import Elasticsearch
import json

class ElasticSearchSalesHandler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            with open('../config.json', 'r') as file:
                config = json.load(file)
            cls.url = config['elasticsearch']['url']
            cls.username = config['elasticsearch']['username']
            cls.password = config['elasticsearch']['password']
            cls._instance = super().__new__(cls)
            # Create Elasticsearch client
            cls._instance.elasticsearch = Elasticsearch(cls.url, http_auth=(cls.username, cls.password), verify_certs=False)
            cls._instance.index_name = "sales"
        return cls._instance

    def search (self, query: dict) -> Dict[str, Any]:
        query = {
            "query": {
                "match": {
                    query['field_name']: query['value']
                }
            }
        }
        response = self.elasticsearch.search(index=self.index_name, body=query)
        if response.get('hits'):
            return response.get('hits')
        else:
            return {}

    def sumSales(self) -> Dict[str, Any]:
        aggregation_query = {
            "aggs": {
                "sum_of_amount": {
                    "sum": {
                        "field": "price"
                    }
                }
            }
        }
        result = self.elasticsearch.search(index= self.index_name, body= aggregation_query, size=0)
        return {'total':result['aggregations']['sum_of_amount']['value']}

    def analyze_trends_over_time(self, interval: str) -> Dict[str, Any]:
        # Define the date histogram aggregation query to analyze sales trends over time
        aggregation_query = {
            "aggs": {
                "sales_over_time": {
                    "date_histogram": {
                        "field": "timestamp",
                        "calendar_interval": interval  # Adjust the interval as needed
                    },
                    "aggs": {
                        "products": {
                            "terms": {
                                "field": "product_name.keyword",
                                "size": 10  # Number of top products to retrieve
                            },
                            "aggs": {
                                "total_sales": {
                                    "sum": {
                                        "script": {
                                            "source": "doc['quantity'].value * doc['price'].value",
                                            "lang": "painless"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        response = []
        result = self.elasticsearch.search(index=self.index_name, body=aggregation_query, size=0)
        sales_over_time_buckets = result['aggregations']['sales_over_time']['buckets']
        for bucket in sales_over_time_buckets:
            date = bucket['key_as_string']
            products = bucket['products']['buckets']
            for product in products:
                product_name = product['key']
                total_sales = product['total_sales']['value']
                doc = {'date': date, 'product': product_name, 'total_sales': total_sales}
                response.append(doc)
        return response



