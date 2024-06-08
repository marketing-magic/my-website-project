import os
import shutil
from datetime import datetime

# נתיב לתיקיית הפוסטים המתוזמנים
scheduled_posts_path = 'scheduled_posts'
published_posts_path = 'posts'

def publish_scheduled_posts():
    now = datetime.now()
    print(f"Current time: {now}")

    for filename in os.listdir(scheduled_posts_path):
        post_path = os.path.join(scheduled_posts_path, filename)
        publish_date_str = filename.split('_')[0]  # נניח שהתאריך מופיע בתחילת שם הקובץ

        try:
            publish_date = datetime.strptime(publish_date_str, '%Y-%m-%d')
            print(f"Processing file: {filename}, scheduled for {publish_date}")

            if publish_date <= now:
                # הוספת תאריך לפרסום בפוסט
                with open(post_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                content = f"<p>פורסם בתאריך: {publish_date_str}</p>\n" + content
                with open(post_path, 'w', encoding='utf-8') as file:
                    file.write(content)

                # העבר את הפוסט לתיקיית הפוסטים המפורסמים
                shutil.move(post_path, os.path.join(published_posts_path, filename))
                print(f'Published post: {filename}')
            else:
                print(f'Post not published yet: {filename} (scheduled for {publish_date_str})')
        except ValueError:
            print(f'Invalid date format in filename: {filename}')

if __name__ == '__main__':
    publish_scheduled_posts()
