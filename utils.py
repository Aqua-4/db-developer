"""A graphical user interface allows database users and administrators
 to do their database tasks in fewer clicks and keystrokes"""


import sqlalchemy


class DataDev:
    """All the functions needed for queryiong the db"""

    def __init__(self):
        """Create DB engine
        db_type, u_name, passwd, server_addr, db_name
        """


        self.connection = self.create_connection( db_type, u_name, passwd, server_addr, db_name)
        

    def create_connection(self, db_type, u_name, passwd, server_addr, db_name):
        """Cached version of sqlalchemy.create_engine.

        Normally, this is not required. But :py:func:`get_table` caches the engine
        *and* metadata *and* uses autoload=True. This makes sqlalchemy create a new
        database connection for every engine object, and not dispose it. So we
        re-use the engine objects within this module."""

        # "mysql://scott:tiger@localhost/test",
        url_str = "{}://{}:{}@{}/{}".format(db_type,
                                            u_name, passwd, server_addr, db_name)

        engine = sqlalchemy.create_engine(url_str)
        
        return engine.connect()
