from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Connection
from rest_framework.views import APIView
from django.http import JsonResponse
import json
import sqlalchemy
import pandas as pd
import cx_Oracle
from functools import lru_cache


class IndexView(generic.ListView):
    template_name = 'connection/index.html'
    context_object_name = 'all_dbs'

    def get_queryset(self):
        return Connection.objects.all()


class DetailView(generic.DetailView):
    model = Connection
    template_name = 'connection/detail.html'


class ConnectionCreate(CreateView):
    model = Connection
    fields = ["usr_name", "passwd", "server_addr", "conn_type", "db_name"]


class ConnectionUpdate(UpdateView):
    model = Connection
    fields = ["usr_name", "passwd", "server_addr", "conn_type", "db_name"]


class ConnectionDelete(DeleteView):
    model = Connection
    success_url = reverse_lazy('connection:index')


class DBQuery(APIView):

    @lru_cache()
    def get(self, request, pk):
        query_str = request.GET.get('query')
        db_obj = Connection.objects.filter(pk=pk).values()[0]
        conn = self.create_connection(db_obj)
        df = pd.read_sql_query("{}".format(query_str), conn)
        # db_obj does not work
        print(df, df.to_dict(orient='records'))
        try:
            return JsonResponse({'data': df.to_dict(orient='records')})
        except:
            return JsonResponse({'data': '{}'.format(df.to_json(orient='records'))})

    def create_connection(self, db_obj):
        """Cached version of sqlalchemy.create_engine.

        Normally, this is not required. But :py:func:`get_table` caches the engine
        *and* metadata *and* uses autoload=True. This makes sqlalchemy create a new
        database connection for every engine object, and not dispose it. So we
        re-use the engine objects within this module."""
        # "mysql://scott:tiger@localhost/test",
        # "dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')\n",
        # "conn = cx_Oracle.connect(user='HRMS_USER', password='gramener', dsn=dsn_tns)\n",
        if not db_obj['passwd']:
            url_str = "{}://{}@{}/{}".format(
                db_obj['conn_type'], db_obj['usr_name'],
                db_obj['server_addr'], db_obj['db_name'])

        else:
            url_str = "{}://{}:{}@{}/{}".format(
                db_obj['conn_type'], db_obj['usr_name'],
                db_obj['passwd'], db_obj['server_addr'], db_obj['db_name'])
        print(url_str, "xxxxxxxxx")
        engine = sqlalchemy.create_engine(url_str)

        return engine.connect()
