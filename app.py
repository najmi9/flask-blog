from core import create_application

app = create_application()

if __name__ == '__main__':
    app.run('0.0.0.0', 8000, True)
