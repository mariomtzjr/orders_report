from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List

from report.models import Operador, Comensal


@dataclass
class ReportOrderEntry:
    """ ReportOrderEntry class to store the report data
    like object from the orders API.
    """
    id: int
    operador: Dict
    comensal: Dict
    order_items: List[Dict]
    grand_total: Decimal
    date: str


