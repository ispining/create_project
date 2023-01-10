#!venv/bin/python

import argparse


def sys_args() -> dict:
    result = {}

    def get_file_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("--system", required=True, help="system for build")
        parser.add_argument("--db", required=True, help="system for build")
        args = parser.parse_args()

        return args

    if get_file_args().db in ["postgres"]:
        result["db"] = get_file_args().db
    else:
        print(f"""[-] Error! Database argument "{get_file_args().db}" not found""")

    if get_file_args().system in ["telebot"]:
        result["system"] = get_file_args().system

    else:
        print(f"""[-] Error! Building system argument "{get_file_args().system}" not found""")

    return result


class Builders:
    class System:
        class Telebot:
            def __init__(self):
                pass

    class Database:
        class Postgres:
            def __init__(self):
                pass


class ProgramStarter:
    def __init__(self):
        if all(("db" in sys_args().keys(), "system" in sys_args().keys())):
            self.sys_args = sys_args()

    def db_build(self):
        if self.sys_args['db'] == "postgres":
            pass

    def system_build(self):
        if self.sys_args['system'] == "telebot":
            pass


ProgramStarter()
