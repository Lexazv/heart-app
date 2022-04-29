from fastapi import HTTPException

from src.constants import ErrorDetails


class ValidationError(HTTPException):

    error_detail: str
    status_code: int = 400

    def __init__(self, **kwargs) -> None:
        super().__init__(
            status_code=self.status_code,
            detail={"detail": self.error_detail.value, **kwargs}
        )


class UnaccaptableColumnsError(ValidationError):

    error_detail = ErrorDetails.unaccaptable_columns


class HasNullColumnError(ValidationError):

    error_detail = ErrorDetails.has_null_column


class InvalidPersonalData(ValidationError):

    error_detail = ErrorDetails.invalid_personal_data


class InvalidAge(ValidationError):

    error_detail = ErrorDetails.invalid_age


class FileNotExist(ValidationError):

    error_detail = ErrorDetails.file_not_exist
