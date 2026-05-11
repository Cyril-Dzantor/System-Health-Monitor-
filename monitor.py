import json
import psutil 
import smtplib 
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv 
import os 

# FUNCTION load_config()
#     READ config file
#     RETURN config values

def load_config():
    print("Loading configuration...")
    load_dotenv()
    with open('config.json', 'r') as file:
        config = json.load(file)
        config['email']['sender_email'] = os.getenv('SENDER_EMAIL')
        config['email']['sender_password'] = os.getenv('SENDER_PASSWORD')
        config['email']['receiver_email'] = os.getenv('RECEIVER_EMAIL')
        return config 

# FUNCTION get_system_metrics()
#     GET cpu usage
#     GET memory usage
#     GET disk usage
#     RETURN metrics




def get_system_metrics():
    metrics = {
        'cpu':psutil.cpu_percent(interval=1),
        'memory':psutil.virtual_memory().percent,
        'disk':psutil.disk_usage('/').percent, 
    }
    return metrics


# FUNCTION check_thresholds(metrics, config)
#     CREATE empty alerts list

#     IF cpu exceeds threshold
#         ADD cpu alert

#     IF memory exceeds threshold
#         ADD memory alert

#     IF disk exceeds threshold
#         ADD disk alert

#     RETURN alerts

def check_thresholds():
    alert = []
    metrics = get_system_metrics()
    config = load_config()

    if metrics['cpu'] > config['thresholds']['cpu']:
        alert.append(f"CPU usage is at {metrics['cpu']}%")
    
    if metrics['memory'] > config['thresholds']['memory']:
        alert.append(f"Memory usage is at {metrics['memory']}%")

    if metrics['disk'] > config['thresholds']['disk']:
        alert.append(f"Disk usage is at {metrics['disk']}%")

    return alert

# FUNCTION send_email(alerts)
#     CONNECT to SMTP server
#     LOGIN to email account
#     SEND alert email

def send_email(alerts,config):
    subject = f'System Monitor Alert - {config['monitoring']['hostname']}'
    body = "\n".join(alerts) 

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = config['email']['sender_email']
    msg['To'] = config['email']['receiver_email']

    print(f"Connecting to {config['email']['smtp_server']}...")
    with smtplib.SMTP(config['email']['smtp_server'], config['email']['smtp_port'], timeout=10) as smtp:
        smtp.starttls()
        print("Logging in...")
        smtp.login(config['email']['sender_email'], config['email']['sender_password'])
        print("Sending email...")
        smtp.sendmail(config['email']['sender_email'], config['email']['receiver_email'], msg.as_string())
    print("Email sent successfully!")



# FUNCTION write_log(metrics, alerts)
#     APPEND timestamp and metrics to log file
def write_log(metrics,alerts,config):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if alerts:
        with open(config['logs']['alert_log'], 'a') as file:
            file.write(f"[{timestamp}] - Alert : {alerts}\n")
    else:
        with open(config['logs']['summary_log'], 'a') as file:
            file.write(f"[{timestamp}] - Metrics : {metrics}\n")

# MAIN
#     config = load_config()

#     metrics = get_system_metrics()

#     alerts = check_thresholds(metrics, config)

#     IF alerts exist
#         send_email(alerts)

#     write_log(metrics, alerts)

# END

if __name__ == "__main__":
    config = load_config()
    metrics = get_system_metrics()
    alerts = check_thresholds()
    if alerts:
        send_email(alerts,config)
    write_log(metrics,alerts,config)