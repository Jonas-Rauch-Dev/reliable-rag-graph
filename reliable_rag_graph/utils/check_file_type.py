from fastapi import UploadFile, HTTPException, status
from filetype import guess


def check_file_type(file: UploadFile) -> bool:
    """
    Validates the type of an uploaded file.

    This function checks if the uploaded file is of an accepted file type. It raises an HTTP 415 error if the file type cannot be determined or if the file type is not supported.

    Args:
        file (UploadFile): The file uploaded by the user, provided as an UploadFile object.

    Returns:
        bool: Returns the detected file type if it is valid and supported.

    Raises:
        HTTPException: If the file type cannot be determined or if the file type is not one of the accepted types, an HTTP 415 UNSUPPORTED_MEDIA_TYPE exception is raised.
    """
    accepted_file_types = [
        "application/pdf",
        "pdf",
    ]

    file_info = guess(file.file)
    if file_info is None:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Could not determine file type",
        )

    detected_file_type = file_info.extension.lower()

    if(
        file.content_type not in accepted_file_types 
        or detected_file_type not in accepted_file_types
    ):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Unsupported file type"
        )

    return detected_file_type