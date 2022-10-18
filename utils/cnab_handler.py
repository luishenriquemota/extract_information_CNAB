from datetime import datetime

def read_cnab(file_path):
    context_format = file_path.readlines()

    arr = []
    for line in context_format:
        convert_line = line.decode("utf-8")
        
        transaction = {
            "type": convert_line[:1],
            "date": datetime.strptime(convert_line[1:9], '%Y%m%d').strftime('%Y-%m-%d'),
            "value": convert_decimal(convert_line[9:19]),
            "cpf": convert_line[19:30],
            "card": convert_line[30:42],
            "hour": datetime.fromtimestamp(int(convert_line[42:48])).strftime("%H:%M:%S"),
            "store_owner": convert_line[48:62],
            "store_name": convert_line[62:81]
        }
        arr.append(transaction)

    return arr


def convert_decimal(value):
    for index, item in enumerate(value):
        if item != "0":
            result = int(value[index:]) / 100.00
            return result
