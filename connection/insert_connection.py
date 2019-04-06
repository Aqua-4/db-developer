from connection.models import Connection

Connection.objects.all()
c = Connection(usr_name="lol", passwd="lol",
               server_addr="localhost:3306", conn_type="pymysql", db_name="rofl")
c.save()
