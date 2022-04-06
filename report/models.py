from dataclasses import dataclass
from typing import Optional

from django.db import models


# Create your models here.
@dataclass
class Operador:
    """ Operator class to store the operator data 
    like object from the orders API.
    """
    id: int
    employee_number: int
    first_name: str
    last_name: str
    email: Optional[str]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

@dataclass
class Comensal:
    """ Comensal class to store the comensal data
    like object from the orders API.
    """

    id: int
    first_name: str
    last_name: str
    table_number: int

    def __str__(self):
        return f"{self.first_name} {self.last_name}"