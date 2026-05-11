# System Health Monitor

A lightweight Python script to monitor system resources (CPU, Memory, and Disk) and send automated email alerts when thresholds are exceeded.

## Features
- **Resource Monitoring**: Tracks CPU percentage, Virtual Memory, and Disk Usage.
- **Email Alerts**: Sends instant notifications via Gmail SMTP when usage exceeds configurable thresholds.
- **Logging**: Maintains a `summary.log` for routine checks and an `alerts.log` for recorded incidents.
- **Configurable**: Easily adjust thresholds and monitoring settings via `config.json`.
- **Environment Security**: Sensitive credentials are stored securely in a `.env` file.

## Prerequisites
- Python 3.12+
- A Gmail account with an [App Password](https://support.google.com/accounts/answer/185833) (if using Gmail).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Cyril-Dzantor/System-Health-Monitor-.git
   cd System-Health-Monitor-
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install psutil python-dotenv
   ```

4. **Setup Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   SENDER_EMAIL=your_email@gmail.com
   SENDER_PASSWORD=your_app_password
   RECEIVER_EMAIL=recipient@example.com
   ```

5. **Configure Thresholds**:
   Edit `config.json` to set your desired limits:
   ```json
   "thresholds": {
       "cpu": 80,
       "memory": 75,
       "disk": 90
   }
   ```

## Usage

Run the script manually:
```bash
python monitor.py
```

### Automation (WSL/Linux)
To run the monitor every 5 minutes using `cron`:
1. Open your crontab: `crontab -e`
2. Add the following line (adjusting paths as necessary):
   ```bash
   */5 * * * * cd "/path/to/System Health Monitor" && ./venv/bin/python monitor.py
   ```

## Files
- `monitor.py`: The core monitoring logic.
- `config.json`: Configuration for thresholds and SMTP settings.
- `.env`: Secret credentials (ignored by Git).
- `summary.log`: History of system metrics.
- `alerts.log`: History of triggered alerts.
