from django.core.management.utils import get_random_secret_key  

try:
    with open(".secret.key", encoding = 'utf-8') as f:
        secret_key = f.read()
except FileNotFoundError:
    with open(".secret.key",'w', encoding = 'utf-8') as f:
        secret_key = get_random_secret_key()
        f.write(secret_key)