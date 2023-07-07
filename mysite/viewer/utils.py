import environ
from .models import Theme

def get_name(name : str) -> str:
    try:
        theme = Theme.objects.get(directory=name)
    except:
        return ''
    return theme.theme

def get_path(suffix : str) -> str:
    env = environ.Env()
    env.read_env('.env')
    return env('OUTPUT_DIR') + '/' + suffix
