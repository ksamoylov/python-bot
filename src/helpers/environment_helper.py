import os
from dotenv import load_dotenv


def get_env_by_name(name: str) -> str:
    load_dotenv()

    return os.getenv(name)


if __name__ == "__main__":
    print(get_env_by_name('foo'))
