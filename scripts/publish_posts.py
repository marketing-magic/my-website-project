import os
import subprocess

# נתיב לתיקיית הפרויקט
project_dir = "C:/Users/User/Desktop/MyWebsite"

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
        # ניווט לתיקיית הפרויקט
        os.chdir(project_dir)
        
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
