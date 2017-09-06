# Copy this file to `conf/settings.py` to put it into effect. It overrides the
# values defined in `resultsdb_frontend/config.py`.
RDB_URL = 'http://resultsdb:5001/api/v2.0'
# SECRET_KEY = 'replace-me-with-something-random'
FILE_LOGGING = False
LOGFILR = '/var/log/resultsdb_frontend/resultsdb_frontend.log'
SYSLOG_LOGGING = False
STREAM_LOGGING = True
RUN_HOST = '0.0.0.0'
RUN_PORT = 5002
