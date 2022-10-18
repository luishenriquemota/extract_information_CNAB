
from xmlrpc.client import _datetime_type
from pytz import utc
from utils.cnab_handler import read_cnab
from datetime import date, time, datetime, timedelta, timezone
import os

for caminho, _, arquivo in os.walk("./arquivos_cnab"):
    file = caminho + "/" + arquivo[0]
    print(read_cnab(file))
    # os.remove(file)

num = "20190301"

hora = 153453



print(datetime.fromtimestamp(hora).strftime("%H:%M:%S")) #hora
print(datetime.strptime(num, '%Y%m%d').strftime('%Y-%m-%d')) # date

