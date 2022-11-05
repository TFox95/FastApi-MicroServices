import hashlib


class Hash():

    def encode(key: str, algorithm: str = None) -> str:
        """
        class Based function that takes in a key and optional algorithm arguments
        to return a hashed value string for the key that was implemented based on the
        algorithm used. Avaiable algorithms are sha3_256 & sha3_512.

        If no algorithm is Selected, the default algorithm of sha3_256 will
        be selected.
        """
        if type(key) is not str:
            raise Exception(
                "value passed was not a str; argument must be a String")
        if algorithm and type(algorithm) is not str:
            raise Exception(
                "value passed was not Falsy or a str; Field must either be blank, Falsy, or a String")

        try:
            if algorithm is str("sha3_256") or not algorithm:
                encode = hashlib.sha3_256(key.encode())
                hexEncoded = encode.hexdigest()
                return hexEncoded

            elif algorithm is str("sha3_512"):
                encode = hashlib.sha3_512(key.encode())
                hexEncoded = encode.hexdigest()
                return hexEncoded

            else:
                raise Exception("incorrect algorithm used. Please utilize one of the following algorithms: sha3_256 & sha3_512. Or leave algorithm field blank, which will invoke default algorithm, which is sha3_256")

        except Exception as exc:
            return exc

    def verify(key: str, keyHash: str, algorithm: str = None) -> bool:
        """
        class Based function that takes in a key, a hash of a key, & optional algorithm arguments
        to return a True or False value depending on the comparison of the two provided keys. 
        Avaiable algorithms are sha3_256 & sha3_512.

        If no algorithm is Selected, the default algorithm of sha3_256 will be
        be selected.
        """

        if type(key) is not str:
            raise Exception(
                "key passed wasn't a str; argument must be a String")
        if type(keyHash) is not str:
            raise Exception(
                "keyHash passed wasn't a str; argument must be a String")
        if algorithm and type(algorithm) is not str:
            raise Exception(
                "value passed was not None or a str; Field must either be blank, or a String")

        try:
            if algorithm is str("sha3_256") or not algorithm:
                encode = hashlib.sha3_256(key.encode())
                hexEncoded = encode.hexdigest()

                if hexEncoded != keyHash:
                    return False

                return True

            elif algorithm is str("sha3_512"):
                encode = hashlib.sha3_512(key.encode())
                hexEncoded = encode.hexdigest()

                if hexEncoded != keyHash:
                    return False

                return True

            else:
                raise Exception("incorrect algorithm used. Please utilize one of the following algorithms: sha3_256 & sha3_512. Or leave algorithm field blank, which will invoke default algorithim, which is sha3_256")

        except Exception as exc:
            raise exc