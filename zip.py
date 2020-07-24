import os
import zipfile


def zip_files_recursively(archpath, dirpath, condition_cb=None):
    """
    Создаёт zip-архив по пути archpath.

    :param archpath: Имя (путь до) архива.
    :param dirpath: Директория, которую надо заархивировать.
    :param condition_cb: Опциональный коллбэк (принимающий аргументов путь к файлу),
                         который должен возвращать True, чтобы файл попал в архив.
    :return:
    """
    zipf = zipfile.ZipFile(archpath, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            fp = os.path.join(root, file)
            if condition_cb and condition_cb(fp) or not condition_cb:
                zipf.write(fp, fp.replace(dirpath, '').strip('/'))
    zipf.close()
