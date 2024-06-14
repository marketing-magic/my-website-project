import os
import shutil
from datetime import datetime

# נתיב לתיקיית הפוסטים המתוזמנים
scheduled_posts_path = 'scheduled_posts'
published_posts_path = 'posts'

def publish_all_posts():
    for filename in os.listdir(scheduled_posts_path):
        post_path = os.path.join(scheduled_posts_path, filename)
        
        # הוספת תאריך לפרסום בפוסט
        with open(post_path, 'r', encoding='utf-8') as file:
            content = file.read()
        publish_date_str = datetime.now().strftime('%Y-%m-%d')
        content = f"<p>פורסם בתאריך: {publish_date_str}</p>\n" + content
        with open(post_path, 'w', encoding='utf-8') as file:
            file.write(content)

        # העבר את הפוסט לתיקיית הפוסטים המפורסמים
        if not os.path.exists(published_posts_path):
            os.makedirs(published_posts_path)
        shutil.move(post_path, os.path.join(published_posts_path, filename))
        print(f'Published post: {filename}')

if __name__ == '__main__':
    publish_all_posts()
