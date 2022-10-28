from datetime import datetime


def ServerDateTime():
    dateTimeString: str = str(datetime.now())
    return dateTimeString


def ServerINFO(NAMESPACE: str, Message: str, obj=None):
    if obj:
        print(f"[{ServerDateTime()}] [{NAMESPACE}] [INFO] {Message}, [object] {obj}")
    else:
        print(f"[{ServerDateTime()}] [{NAMESPACE}] [INFO] {Message}")


def ServerWARNING(NAMESPACE: str, Message: str, obj=None):
    if obj:
        print(f"[{ServerDateTime()}] [{NAMESPACE}] [INFO] {Message}, [object] {obj}")
    else:
        print(f"[{ServerDateTime()}] [{NAMESPACE}] [INFO] {Message}")


def ServerERROR(NAMESPACE: str, Message: str, obj=None):
    if obj:
        print(f"[{ServerDateTime()}] [{NAMESPACE}] [INFO] {Message}, [object] {obj}")
    else:
        print(f"[{ServerDateTime()}] [{NAMESPACE}] [INFO] {Message}")


def ServerDEBUG(NAMESPACE: str, Message: str, obj=None):
    if obj:
        print(f"[{ServerDateTime()}] [{NAMESPACE}] [INFO] {Message}, [object] {obj}")
    else:
        print(f"[{ServerDateTime()}] [{NAMESPACE}] [INFO] {Message}")
