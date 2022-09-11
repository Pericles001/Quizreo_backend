from typing import Any, List
import shutil
import ntpath
import time
from sqlalchemy.orm import Session
from fastapi import Response, UploadFile
from passlib.context import CryptContext
from slugify import slugify
import socket
import fcntl
import struct
import base64


crypto_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return crypto_context.hash(password)


def verify_hash(plain_password: str, hash: str):
    return crypto_context.verify(plain_password, hash)


def is_slice_in_list(slice, list):
    len_slice = len(slice)
    return any(
        slice == list[i : len_slice + i] for i in range(len(list) - len_slice + 1)
    )


def is_any_slice_element_in_list(slice, list):
    return any(i in list for i in slice)


def get_file_name_and_extension(filename: str) -> dict:
    parts_list = filename.split(".")
    if len(parts_list) > 2:
        name_parts = [parts_list[i] for i in range(len(parts_list) - 1)]
        filename = ".".join(name_parts)
        return {"filename": filename, "extension": parts_list[len(parts_list) - 1]}
    return {"filename": parts_list[0], "extension": parts_list[1]}


def get_filename_from_filepath(filepath: str):
    return ntpath.basename(filepath)


def store_uploaded_file(file: UploadFile | str, storage_path: str):
    files_infos = get_file_name_and_extension(file.filename)
    file_location = f"{storage_path}/{files_infos['filename']}-{time.time()}.{files_infos['extension']}" 
    with open(file_location, "wb") as file_path:
        shutil.copyfileobj(file.file, file_path)
    return file_location

def store_base64_file(file: str, storage_path: str):
    file_location = f"{storage_path}/profile_picture-{time.time()}.jpg" 
    with open(file_location, "wb") as file_path:
        base64string = base64.b64encode(file.encode('utf-8', errors='strict'))
        file_path.write(base64string)
    return file_location


def set_profile_picture(model: Any, db: Session, file: UploadFile | str):
    profiles_pictures_path = "public/uploads/profiles_pictures"
    file_path = store_uploaded_file(file, profiles_pictures_path) if isinstance(file, UploadFile) else store_base64_file(file, profiles_pictures_path)
    model.profile_picture = file_path
    db.add(model)
    db.commit()
    db.refresh(model)

def get_slug_from(string: str):
    return slugify(
        string,
        entities=True,
        decimal=True,
        hexadecimal=True,
        max_length=0,
        word_boundary=False,
        separator="",
        save_order=False,
        stopwords=(),
        regex_pattern=None,
        lowercase=True,
        replacements=(),
        allow_unicode=False,
    )


def update_values(*, destination, source) -> Any:
    model = destination
    source_object = source
    for key in list(source.keys()):
        source_attribute_value = source_object[key]
        destination_attribute_value = destination.__dict__[key]
        setattr(
            model,
            key,
            source_attribute_value
            if source_attribute_value is not None
            else destination_attribute_value,
        )
    return model

def set_cookie(
    *,
    response: Response,
    cookie_key: str,
    cookie_value: str,
    domains: List[str],
    expires: int = (10 * 365 * 24 * 60 * 60),
):
    for domain in domains:
        response.set_cookie(
            cookie_key,
            value=cookie_value,
            httponly=True,
            secure=True,
            samesite="none",
            domain=domain,
            expires=expires,
        )
    return