import os
import requests

# URL הבסיסי של האתר שלך
BASE_URL = "https://noyshoshan.i.ng"

# רשימת הפוסטים לפרסום
files_to_publish = [
    "posts/2024-06-10_content_creation_strategies.html",
    "posts/2024-06-11_seo_tips.html",
    "posts/2024-06-12_social_media_ads.html",
    "posts/2024-06-13_using_crm.html",
    "posts/2024-06-14_intro_to_digital_marketing.html",
]

def publish_post(file_path):
    # קריאת תוכן הקובץ
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    
    # יצירת ה-URL של הפוסט
    post_name = os.path.basename(file_path).replace('.html', '')
    post_url = f"{BASE_URL}/{post_name}.html"
    
    # הכנת הנתונים לשליחה
    data = {
        "content": content
    }

    # שליחת בקשה לשרת
    print(f"Publishing to {post_url}...")
    response = requests.put(post_url, data=data)

    if response.status_code == 200:
        print(f"Post {file_path} published successfully at {post_url}")
    else:
        print(f"Failed to publish post {file_path}. Status code: {response.status_code}, Response: {response.text}")

# פרסום כל הפוסטים ברשימה
for file_path in files_to_publish:
    publish_post(file_path)
