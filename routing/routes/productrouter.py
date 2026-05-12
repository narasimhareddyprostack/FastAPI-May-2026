from fastapi import APIRouter

router=APIRouter(prefix='/product')

'''
Usage:Delete new Product
Rest API URL:http://127.0.0.1:8000/product/delete
Method Type:DELETE
Required Fields:None
Access type:Public
'''
@router.delete("/delete")
def delete_product():
    return {"msg":"Product Deleted successfully"}