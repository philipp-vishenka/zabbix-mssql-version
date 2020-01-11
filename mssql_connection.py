from argparse import ArgumentParser
import pyodbc
from os import getenv
from dotenv import load_dotenv, find_dotenv


def parsing():
    parser = ArgumentParser()
    parser.add_argument("server", type=str)
    parser.add_argument("database", type=str)
    parser.add_argument("username", type=str)
    parser.add_argument("password", type=str)
    parser.add_argument("driver", type=str)
    return parser.parse_args()


def get_cursor():
    return cursor


load_dotenv(find_dotenv())
args = parsing()
conn = pyodbc.connect(f"DRIVER={args.driver};"
                      f"SERVER={args.server};"
                      f"DATABASE={args.database};"
                      f"UID={getenv(args.username)};"
                      f"PWD={getenv(args.password)}")

cursor = conn.cursor()
