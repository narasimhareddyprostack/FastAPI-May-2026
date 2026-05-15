from fastapi import FastAPI
from typing import Optional
app=FastAPI()

#import Dummy data
products=[
    {"id":1,"name":"Pen","category":"Stationary","price":50},
    {"id":2,"name":"Notebook","category":"Stationary","price":10},
    {"id":3,"name":"T-Shirt","category":"Clothing","price":500},
    {"id":4,"name":"Eraser","category":"Stationary","price":5000},
    {"id":5,"name":"ThinkPad","category":"Electronics","price":50000}
]

'''
usage: Applicaton Root
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: NONE 
Access Type:Public
'''

@app.get("/")
def app_root():
    return {"msg":"Application Root"}

'''
usage: fetch products by category,price
Rest API URL:
http://127.0.0.1:8000/products                                - without Query Para
http://127.0.0.1:8000/products?category=Electronics           - with Query Para
http://127.0.0.1:8000/products?category=Electronics&price=200 - with Multiple Query Para

Method Type:GET
Required Fields: NONE 
Access Type:Public
'''
@app.get("/products")
def get_products(category:Optional[str]=None,price:Optional[int]=None):
    filtered_products=[]
    #if category - Query Para is there
    if category and price==None:
        filtered_products=[product for product in products 
            if product['category']==category ]
        
        return filtered_products
    #if price and category- Query Para is there
    if price and category:
        print("inside sec if st")
        for product in products:
            if product['price']<=price and product['category']==category:
                filtered_products.append(product)
        return filtered_products
            
    #if there is no Query Parameters
    return products
