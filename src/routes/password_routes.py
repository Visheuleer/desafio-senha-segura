from fastapi import APIRouter, HTTPException, status
import services.password_services as service

router = APIRouter()


@router.post('/validate-password', status_code=status.HTTP_200_OK)
def validate_password(password: str):
    if not service.check_length(password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Password must have at least 8 characters')

    elif not service.check_uppercase(password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Password must have at least one uppercase character')

    elif not service.check_digit(password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Password must have at least one digit')

    elif not service.check_lowercase(password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Password must have at least one lowercase character')

    elif not service.check_special_characters(password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Password must have at least one special character')

    return {'message': 'Password is valid'}
