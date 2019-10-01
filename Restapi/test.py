import requests
import json
import os
AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/jwt/'
REFRESH_ENDPOINT = AUTH_ENDPOINT+"refresh/"
ENDPOINT = 'http://127.0.0.1:8000/api/status/'
image_path = os.path.join(os.getcwd(),"logo.jpg")
headers ={
    "content-Type":"application/json",
    "Authorization":"JWT"+ "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImthcnRoaWsiLCJleHAiOjE1Njc5NDk5MDQsImVtYWlsIjoiIn0.C6fNlR7acJt-sLh2pK-o2ctgyKa9Ayww4k9TG0gnELo"
}


data ={
    'username':'karthik',
    'password':984989,
}
r = requests.post(AUTH_ENDPOINT,data=json.dumps(data),headers= headers)
token = r.json()
# print(token)
# refresh_data ={
#     'token':token
# }
# new_response = requests.post(REFRESH_ENDPOINT,data=json.dumps(refresh_data),headers=headers)
# new_token = new_response.json()['token']
# get_endpoint = ENDPOINT+str(12)
headers ={
    "content-Type":"application/json",
    "Authorization":"JWT" +"token",
}

post_data = json.dumps({"content":"some random content"})
posted_response = requests.post(ENDPOINT,data = post_data)
print(posted_response.text)
get_endpoint = ENDPOINT+str(12)
#
# r = requests.get(get_endpoint)
# print (r.text)
#
# r2 = requests.get(ENDPOINT)
# print(r2.status_code)
#
# post_headers ={
#     'content-type':'application/json'
# }
# post_response = requests.post(ENDPOINT,data=post_data,headers = post_headers)
#
# print (post_response.text)
#for getting image

# def do_img(method = 'get',data={},is_json = True,img_path =None):
#     headers ={}
#     if is_json:
#         headers['content-type'] ='application/json'
#         data =json.dumps(data)
#     if image_path is not None:
#         with open(image_path,'rb') as image:
#             file_data ={
#                 'image':image
#             }
#
#
#
#             r = requests.request(method,ENDPOINT,data=data,headers =headers,files = image)
#     else:
#
#       r = requests.request(method,ENDPOINT,data= data,headers=headers)
#     print (r.text)
#     print(r.status_code)
#     return r
#
# do_img(method='post',data={'user':1,"content":""},is_json=False, img_path= image_path)
#
#
#
#
#
#
#
#
#
#
#
#
# def do(method = 'get',data={},is_json = True):
#     headers ={}
#     if is_json:
#         headers['content-type'] ='application/json'
#         data =json.dumps(data)
#     r = requests.request(method,ENDPOINT,data= data,headers=headers)
#     print (r.text)
#     print(r.status_code)
#     return r
# do(data={'id':500})
# #do(method='delete',data={'id': 500})
# do(method='put',data={'id':13,"content":"some cool new content",'user':1})
