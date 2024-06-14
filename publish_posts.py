import http.client
import mimetypes
import os

# פרטי השרת והנתיב
SERVER = "yourdomain.com"
PATH = "/upload"  # הנתיב בשרת שבו מקבלים את הקבצים

# רשימת הפוסטים לפרסום
files_to_publish = [
    "posts/2024-06-10_content_creation_strategies.html",
    "posts/2024-06-11_seo_tips.html",
    "posts/2024-06-12_social_media_ads.html",
    "posts/2024-06-13_using_crm.html",
    "posts/2024-06-14_intro_to_digital_marketing.html",
]

def publish_post(file_path):
    boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
    payload = ''
    payload += '--' + boundary + '\r\n'
    payload += 'Content-Disposition: form-data; name="file"; filename="' + os.path.basename(file_path) + '"\r\n'
    payload += 'Content-Type: ' + mimetypes.guess_type(file_path)[0] + '\r\n\r\n'
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    payload += content + '\r\n'
    payload += '--' + boundary + '--'

    headers = {
        'Content-type': 'multipart/form-data; boundary=' + boundary
    }
    
    conn = http.client.HTTPSConnection(SERVER)
    conn.request("POST", PATH, payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    if res.status == 200:
        print(f"Post {file_path} published successfully.")
    else:
        print(f"Failed to publish post {file_path}. Status code: {res.status}, Response: {data.decode('utf-8')}")

# פרסום כל הפוסטים ברשימה
for file_path in files_to_publish:
    publish_post(file_path)
