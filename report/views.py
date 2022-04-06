from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from report.reports import ReportOrderEntry
from report.models import Operador, Comensal, Product
from report.utils import get_orders, get_operator, get_comensal, get_product, get_dates_from_params, generate_order_report


# Create your views here.
class OrderReportView(generics.ListAPIView):
    queryset = get_orders()
    serializer_class = None

    def get(self, request):
        query_param = request.query_params
        qs = self.get_queryset()
        data = []
        for order_entry in qs:
            operador = Operador(**get_operator(order_entry.get("operador").get("id"))).__dict__
            comensal = Comensal(**get_comensal(order_entry.get("comensal").get("id"))).__dict__
            
            order_items_ = order_entry.get("order_items")
           
            order_items_processed = [Product(**get_product(order_item.get("id"))).__dict__ for order_item in order_items_]

            report_entry = ReportOrderEntry(
                id=order_entry.get("id"),
                operador=operador,
                comensal=comensal,
                order_items=order_items_processed,
                grand_total=order_entry.get("grand_total"),
                date=order_entry.get("date")
            )
            data.append(report_entry.__dict__)

        if query_param:
            qs = get_dates_from_params(data, request.query_params)
            if query_param.get("product"):
                filter_by_product = generate_order_report(qs)
                return Response(filter_by_product)
            return Response(qs)
        else:
            return Response(data)
        

