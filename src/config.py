
class Local(object):
    """
    Development environment configuration
    """
    
    DEBUG = True
    TESTING = False
    PROJECT_ID = "yas-dev-tpm"
    POKE_URL="https://pokeapi.co/api/v2"

class Dev(object):
    """
    Development environment configuration
    """
    
    DEBUG = True
    TESTING = False
    PROJECT_ID = "yas-dev-tpm"
    POKE_URL="https://pokeapi.co/api/v2"

app_config = {
    "local":Local,
    "dev":Dev
}
