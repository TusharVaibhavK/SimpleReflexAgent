import os

# Bind to the port provided by Render
bind = f"0.0.0.0:{os.environ.get('PORT', '5000')}"

# Use 4 worker processes
workers = 4

# Timeout after 60 seconds
timeout = 60

# Access log configuration
accesslog = "-"  # Log to stdout
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Error log configuration
errorlog = "-"  # Log to stderr
loglevel = "info"
