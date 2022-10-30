import hashlib

password = "jalonTaylor345678?>?:L"

#encode = hashlib.sha512(password.encode())


# print(encode.hexdigest())


class Hash():

    def encode(key: str, algorithim: str = None) -> str:
        """
        class Based function that takes in a key and optional algorithim arguments
        to return a hashed value string for the key that was implemented based on the
        algorithim used. Avaiable algorithims are sha256 & sha512.

        If no algorithim is Selected, the default algorithm of SHA512 will
        be selected.
        """
        try:

            if algorithim is str("sha512") or algorithim is None:

                encode = hashlib.sha512(key.encode())
                hexEncoded = encode.hexdigest()
                return str(hexEncoded)

            elif algorithim is str("sha256"):

                encode = hashlib.sha256(key.encode())
                hexEncoded = encode.hexdigest()
                return str(hexEncoded)

            else:
                return str("incorrect algorithim used. Please utilize one of the following algorithims: sha256, sha384, sha 512, or md5")

        except Exception as e:
            return str(e)

Hash.encode("Mikal1029*")
