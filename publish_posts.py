import os
import subprocess

# נתיב לתיקיית הפרויקט
project_dir = "C:/Users/User/Desktop/MyWebsite"

# נתיב לדף הבלוג שלך
blog_page = os.path.join(project_dir, "post1.html")

# רשימת הפוסטים לפרסום
files_to_publish = [
    "posts/2024-06-10_content_creation_strategies.html",
    "posts/2024-06-11_seo_tips.html",
    "posts/2024-06-12_social_media_ads.html",
    "posts/2024-06-13_using_crm.html",
    "posts/2024-06-14_intro_to_digital_marketing.html",
]

def publish_post():
    try:
        # קריאת התוכן הקיים בדף הבלוג
        if os.path.exists(blog_page):
            with open(blog_page, 'r', encoding='utf-8') as blog_file:
                blog_content = blog_file.read()
        else:
            blog_content = "<html><body><h1>Blog Posts</h1>"

        # ניווט לתיקיית הפרויקט
        os.chdir(project_dir)

        # הוספת התוכן של כל פוסט לדף הבלוג
        for file_path in files_to_publish:
            full_path = os.path.join(project_dir, file_path)
            if os.path.exists(full_path):
                with open(full_path, 'r', encoding='utf-8') as post_file:
                    post_content = post_file.read()
                    blog_content += f"<hr>{post_content}"

        # סגירת תגיות HTML
        blog_content += "</body></html>"

        # כתיבת התוכן המעודכן חזרה לדף הבלוג
        with open(blog_page, 'w', encoding='utf-8') as blog_file:
            blog_file.write(blog_content)

        # הוספת קבצים
        for file_path in files_to_publish:
            subprocess.run(["git", "add", file_path])
        
        # יצירת קומיט
        subprocess.run(["git", "commit", "-m", "Publishing new posts"])
        
        # דחיפת השינויים ל-GitHub
        subprocess.run(["git", "push", "origin", "main"])
        
        print("Posts published successfully.")
    except Exception as e:
        print(f"Failed to publish posts. Error: {e}")

# פרסום הפוסטים
publish_post()

