
HOW TO USE:

1. Open config.json and fill APP_PASSWORD with your Gmail App Password.
2. Run: python3 job_alert.py
3. To schedule daily at 7 AM:
   Linux/macOS:
     - crontab -e
     - Add:
        0 7 * * * python3 /path/to/job_alert.py
