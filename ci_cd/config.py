import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="ci_cd",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="ci_cd_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from ci_cd.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export ci_cd_KEY=value
export ci_cd_KEY="@int 42"
export ci_cd_KEY="@jinja {{ this.db.uri }}"
export ci_cd_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
ci_cd_ENV=production ci_cd run
```

Read more on https://dynaconf.com
"""
