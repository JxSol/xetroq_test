from datetime import datetime
from typing import NoReturn

from django.core.exceptions import ValidationError


def validate_past_year(value: int) -> NoReturn:
    """Валидатор корректности года."""
    current_year = datetime.now().year
    if value > current_year:
        raise ValidationError(
            'Год должен быть не позднее текущего.',
        )
