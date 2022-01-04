import json
from typing import List

# import requests
# 2次方程式 ax^2 + bx + c = 0 （x^2はxの2乗の意味）の係数a, b, cを入力し、
# 2次方程式の解が2つの実数解か、重解か、2つの虚数解かを判別するプログラムを作成せよ。
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

def is_quadratic_equation(numbers:List[int])->str:
    D = numbers[1]*numbers[1]-4*numbers[0]*numbers[2]
    if D > 0:
        return "２つの異なる実数解"
    elif D == 0:
        return "重解"
    else:
        return "虚数解"



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
        n = is_quadratic_equation(n)
        print(n)
    except:
        return{
        "statusCode": 400,
        "headers":{
            "Content-Type": "application/json"
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
        "body": json.dumps({
            "message": n,
            # "location": ip.text.replace("\n", "")
        }),
    }