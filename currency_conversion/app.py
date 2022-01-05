import json
from typing import List

# import requests
# 換算したい金額（円単位）と1ドル何円かを整数値で入力すると、入力した金額が何ドル何セントか計算して表示するプログラムを作成せよ。
# 1セントは1/100ドルである。結果は整数値でよい（1セント未満の端数切り捨て）。

class InvalidError(Exception):
    pass
def is_number(x: str):
    if x.startswith("-"):
        x = x[1:]
    if not x.isdigit():
        return False
    return True
def number(x):
    if not is_number(x):
        raise InvalidError("整数値を入力してください。")
    return int(x)

# 入力された文字列を分割し、listする 
def split_numbers(text: str):
    text_list = text.split(",")
    number_list = []
    for i in text_list:
        i = number(i)
        number_list.append(i)
    return number_list

def is_currency_conversion(numbers:List[int])->str:
    d = numbers[0]/numbers[1]
    d = int(d)
    s = (d*100)/numbers[1]
    s = int(s)
    return d,s




def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    print(event)
    try:
        n = event.get('queryStringParameters').get('numbers')
        n = split_numbers(n)
        n = is_currency_conversion(n)
        print(n)
    except:
        return{
        "statusCode": 400,
        "headers":{
            "Content-type": "application/json;charset=UTF-8"
        },
        "body":json.dumps({
            "message":"整数値を入力してください。"
        }),
    }
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "headers":{
            "Content-type": "application/json;charset=UTF-8"
        },
        "body": json.dumps({
            "message": n,
            # "location": ip.text.replace("\n", "")
        }),
    }