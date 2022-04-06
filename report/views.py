from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from report.reports import ReportOrderEntry
from report.models import Operador, Comensal
from report.utils import get_orders, get_operator, get_comensal


# Create your views here.
class OrderReportView(generics.ListAPIView):
    queryset = get_orders()
    serializer_class = None

    def get(self, request):
        data = []
        qs = self.get_queryset()
        for order_entry in qs:
            operador = Operador(**get_operator(order_entry.get("operador"))).__dict__
            comensal = Comensal(**get_comensal(order_entry.get("comensal"))).__dict__
            report_entry = ReportOrderEntry(
                id=order_entry.get("id"),
                operador=operador,
                comensal=comensal,
                order_items=order_entry.get("order_items"),
                grand_total=order_entry.get("grand_total"),
                date=order_entry.get("date")
            )
            data.append(report_entry.__dict__)

        return Response(data)

