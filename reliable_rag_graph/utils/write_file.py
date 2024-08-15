from fastapi import UploadFile, HTTPException, status
from aiofiles import open
from os import makedirs, path

async def write_file(in_file: UploadFile, base_path: str = "/tmp") -> str:
    """
    Asynchronously writes an uploaded file to the specified directory on the server.

    Args:
        in_file (UploadFile): The uploaded file to be saved.
        base_path (str, optional): The base directory where the file should be stored. Defaults to "/tmp".

    Raises:
        HTTPException: Raised with status code 400 if the file already exists, 
                       if the specified directory does not exist, 
                       or if a directory with the same name as the file already exists.
        HTTPException: Raised with status code 403 if there are insufficient permissions to write to the specified directory.
        HTTPException: Raised with status code 500 if an unexpected error occurs or an OS error is encountered.

    Returns:
        str: The path of the uploaded file
    """
    file_path = f"{base_path}/{in_file.filename}"

    if path.isfile(file_path):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The file already exitsts"
        )
    try:
        makedirs(base_path, exist_ok=True)

        async with open(file_path, 'wb') as out_file:
            while content := await in_file.read(1024):
                await out_file.write(content)
    
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The specified directory does not exist."
        )

    except PermissionError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions to write to the specified directory."
        )

    except IsADirectoryError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A directory with the same name as the file already exists."
        )

    except OSError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An OS error occurred: {e.strerror}"
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )

    return file_path