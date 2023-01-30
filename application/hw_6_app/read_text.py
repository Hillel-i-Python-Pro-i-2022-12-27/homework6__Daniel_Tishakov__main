from application.config.PATHS import INPUT_FILES


def read_text():
    data = INPUT_FILES / "text.txt"
    with open(data) as a:
        reading = a.read()
    return reading


if __name__ == "__main__":
    read_text()
