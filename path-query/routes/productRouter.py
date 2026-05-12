from fastapi import APIRouter
from fastapi import HTTPException, status
from typing import Optional

router=APIRouter(prefix="/products")

#Get Data from Model Class/Dummy Data

products=[
    {"id":1,"name":"Pen","category":"Stationary","price":50},
    {"id":2,"name":"Notebook","category":"Stationary","price":10},
    {"id":3,"name":"T-Shirt","category":"Clothing","price":500},
    {"id":4,"name":"Eraser","category":"Stationary","price":5},
    {"id":5,"name":"ThinkPad","category":"Electronics","price":50000},
]

'''
Usage: Get all products
Rest API URL:http://127.0.0.1:8000/products/read
Method Type:GET
Required Fields:None
Access Type:Public
'''
@router.get("/read")
def get_all_Products():
    return products


'''
Usage: fetch product by Id 
Rest API URL:http://127.0.0.1:8000/products/1
Method Type:GET
Required Fields:None
Access Type:Public
'''
# Get Product By ID
@router.get("/{productId}")
def get_product(productId: int):

    for product in products:
        if product["id"] == productId:
            return product

    # Executes only if no product found
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product Not Exists"
    )
    

'''
Usage: fetch all product by categroy
Rest API URL: http://127.0.0.1:8000/products?category=electroics
Method Type:GET
Required Fields: None
Access Type Public
'''

@router.get("/")
def search_products(category: Optional[str] = None):
    
    print(category)

    filter_products = []

    if category:
        for product in products:
            if product["category"] == category:
                filter_products.append(product)
    else:
        filter_products = products

    return filter_products
'''
Path Paramter vs Query Parameters
Path Para - To identify Specific resours
Path Para - To identify Specific resourse by Id

Query Para: Best for - filtering, Pagination, Logging 
'''
