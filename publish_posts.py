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

def read_post_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def update_blog_file(posts_content):
    with open(blog_page, 'r', encoding='utf-8') as file:
        blog_content = file.read()
    
    # חיפוש נקודת ההוספה בתוך ה-HTML
    insert_point = blog_content.find("</main>")
    if insert_point == -1:
        raise Exception("Couldn't find the insertion point in the blog file.")
    
    # הוספת התוכן של הפוסטים לפני סיום התגית </main>
    updated_content = blog_content[:insert_point] + posts_content + blog_content[insert_point:]

    with open(blog_page, 'w', encoding='utf-8') as file:
        file.write(updated_content)

def publish_post():
    try:
        # ניווט לתיקיית הפרויקט
        os.chdir(project_dir)
        
        # משיכת השינויים מהמאגר
        subprocess.run(["git", "pull", "origin", "main"])
        
        # קריאת התוכן של כל הפוסטים
        posts_content = ""
        for file_path in files_to_publish:
            post_content = read_post_content(os.path.join(project_dir, file_path))
            posts_content += post_content + "\n\n"
        
        # עדכון קובץ הבלוג הראשי
        update_blog_file(posts_content)

        # הוספת קובץ הבלוג המעודכן
        subprocess.run(["git", "add", blog_page])
        
        # יצירת קומיט
        subprocess.run(["git", "commit", "-m", "Updating blog with new posts"])
        
        # דחיפת השינויים ל-GitHub
        subprocess.run(["git", "push", "origin", "main"])
        
        print("Posts published successfully.")
    except Exception as e:
        print(f"Failed to publish posts. Error: {e}")

# פרסום הפוסטים
publish_post()

