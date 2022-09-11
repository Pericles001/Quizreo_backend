from typing import Any, List
import shutil, ntpath, base64, time, os, magic
from sqlalchemy.orm import Session
from fastapi import Response, UploadFile, HTTPException
from passlib.context import CryptContext
from slugify import slugify


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
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    with open(file_location, "wb") as file_path:
        shutil.copyfileobj(file.file, file_path)
    return file_location

def store_base64_file(file: str, storage_path: str):
    try:
        file_as_byte = str.encode(file)  
        recovered_file = base64.b64decode(file_as_byte)
        file_chunks = [recovered_file[i:i+2048] for i in range(0, len(recovered_file), 2048)]
        first_2048_bytes = file_chunks[0]
        file_type = magic.from_buffer(first_2048_bytes, mime=True)
        file_extension = file_type.split("/")[-1]
        file_location = f"{storage_path}/file{time.time()}.{file_extension}" 
    except:
       raise HTTPException(400, "An error occured ! Your file is probably invalid! Expecting a valid base64 file or Object of class UploadFile 🙂️") 
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    with open(file_location, "wb") as file_path: 
        file_path.write(recovered_file)
    return file_location


def set_profile_picture(file: UploadFile | str):
    profiles_pictures_path = "public/uploads/profiles_pictures"
    file_path = store_uploaded_file(file, profiles_pictures_path) if isinstance(file, UploadFile) else store_base64_file(file, profiles_pictures_path)
    return file_path

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