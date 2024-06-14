import os
from ftplib import FTP

# פרטי ה-FTP (עדכן לפי הפרטים שלך)
FTP_HOST = "ftp.yourdomain.com"  # כתובת ה-FTP
FTP_USER = "your_username"       # שם המשתמש
FTP_PASS = "your_password"       # הסיסמה
FTP_DIR = "/path/to/upload"      # הנתיב לתיקיית היעד בשרת

# רשימת הפוסטים לפרסום
files_to_publish = [
    "posts/2024-06-10_content_creation_strategies.html",
    "posts/2024-06-11_seo_tips.html",
    "posts/2024-06-12_social_media_ads.html",
    "posts/2024-06-13_using_crm.html",
    "posts/2024-06-14_intro_to_digital_marketing.html",
]

def publish_post(file_path):
    try:
        # חיבור ל-FTP
        ftp = FTP(FTP_HOST)
        ftp.login(user=FTP_USER, passwd=FTP_PASS)
        ftp.cwd(FTP_DIR)
        
        # העלאת הקובץ
        with open(file_path, 'rb') as file:
            ftp.storbinary(f'STOR {os.path.basename(file_path)}', file)
        
        ftp.quit()
        print(f"Post {file_path} published successfully.")
    except Exception as e:
        print(f"Failed to publish post {file_path}. Error: {e}")

# פרסום כל הפוסטים ברשימה
for file_path in files_to_publish:
    publish_post(file_path)
