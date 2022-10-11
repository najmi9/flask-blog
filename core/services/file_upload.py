from werkzeug.utils import secure_filename

def upload_for_blog(filename: str, path: str, f):
    filename = secure_filename(f.filename)
    f.save(f'../uploads/images/{filename}')
    pass


def delete_for_blog():
    pass
