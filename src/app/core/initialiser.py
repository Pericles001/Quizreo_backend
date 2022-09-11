from src.app.core.initialise import initialise
from src.app.core.session import SessionLocal


def init() -> None:
    db = SessionLocal()
    initialise(db)


def main() -> None:
    init()


if __name__ == "__main__":
    main()
