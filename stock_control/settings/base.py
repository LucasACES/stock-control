from pathlib import Path
from ..secretKey import key

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = key()

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True