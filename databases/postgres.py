import os, threading

try:
    import iluxaMod as ilm
except:
    os.system("pip install iluxaMod")
    import iluxaMod as ilm

database = ilm.postgreSQL_connect(host="illyashost.ddns.net", database="postgres", user="postgres", password="armageddon")
db = database.db
sql = database.sql


VERBOSE = True


def migration(verbose: bool=VERBOSE) -> None:
    """
    Create Databases if not exists

    :param verbose:
    print_logs boolean

    :return:
    None
    """

    def standard_init():
        database.init_DB(stages=True, staff=True, sub=True, balance=True, settings=True, stdout=False)

    for TableCreationFunc in [standard_init]:
        th = threading.Thread(target=TableCreationFunc)
        th.daemon = True
        th.start()
        threading.main_thread()
        if verbose:
            print(f"[+] Thread preDB.{TableCreationFunc.__name__} started")


migration()

