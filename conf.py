import os
from sqlalchemy.orm import declarative_base

DATABASE_URL = os.environ.get('DB_URI', 'postgresql://mpmnyhpdqfkysz:74fb1cea523c76029effb7c4638410e83d1c66f7a292a8495563dc68dd2d9efc@ec2-54-74-95-84.eu-west-1.compute.amazonaws.com:5432/d7jfim7rcp2eq3')
AUTH_LOGIN = os.environ.get('AUTH_LOGIN', 'api')
AUTH_PASS = os.environ.get('AUTH_PASS', 'niesamowicieskomplikowanehaslo')
Base = declarative_base()
