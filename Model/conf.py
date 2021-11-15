import os

DB_URI = os.environ.get('DB_URI', 'postgresql://admin:password@db/lasy_database')
AUTH_LOGIN = os.environ.get('AUTH_LOGIN', 'api')
AUTH_PASS = os.environ.get('AUTH_PASS', 'niesamowicieskomplikowanehaslo')
