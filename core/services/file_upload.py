'''Manage file upload'''

import os
from flask import current_app
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

def upload_for_blog(file: FileStorage) -> str:
    '''Upload a file to the upload folder'''
    upload_folder = current_app.config.get('UPLOAD_FOLDER')
    if not upload_folder:
        raise ValueError(f'{upload_folder} not found')

    filename = secure_filename(file.filename)
    path = os.path.join(
        current_app.root_path,
        upload_folder,
        filename
    )
    file.save(path)

    return f'/{upload_folder}/{filename}'


def delete_for_blog(path: str):
    '''Delete a file of a blo*'''
    path = f'{current_app.root_path}{path}'
    if os.path.exists(path):
        os.remove(path)
