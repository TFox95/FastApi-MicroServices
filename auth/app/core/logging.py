
def ServerINFO(NAMESPACE: str, Message: str, obj=None):
    if obj is not None:
        print(f"[{getServerTime()}] [{namespace}] [INFO] {message}, [object] {obj}")
    else:
        print(f"[{getServerTime()}] [{namespace}] [INFO] {message}")

    if obj is not None:
        print(f"[{getServerTime()}] [{namespace}] [INFO] {message}, [object] {obj}")
    else:
        print(f"[{getServerTime()}] [{namespace}] [INFO] {message}")


def ServerERROR(NAMESPACE: str, Message: str, obj=None):
    if obj is not None:
        print(f"[{getServerTime()}] [{namespace}] [INFO] {message}, [object] {obj}")
    else:
        print(f"[{getServerTime()}] [{namespace}] [INFO] {message}")


def ServerDEBUG(NAMESPACE: str, Message: str, obj=None):
    if obj is not None:
        print(f"[{getServerTime()}] [{namespace}] [INFO] {message}, [object] {obj}")
    else:
        print(f"[{getServerTime()}] [{namespace}] [INFO] {message}")
