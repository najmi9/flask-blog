from core import create_application

app = create_application()

if __name__ == '__main__':
    app.run('127.0.0.1', 8000, True)
