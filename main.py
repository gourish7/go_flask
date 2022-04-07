from threading import Timer
from app.application import create_app
import eel

app = create_app()
eel.init("app")


def eel_function():
    eel.start('/', port=5000)


if __name__ == '__main__':
    Timer(0, eel_function).start()
    app.run()
    # eel_function()
