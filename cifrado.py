import hashlib

def main():

    clave = input('Ingrese una cadena de texto: ')

    md5 = hashlib.md5(clave.encode('utf-8')).hexdigest()
    print("Esto es un hash md5: " + md5)

    sha224 = hashlib.sha224(clave.encode('utf-8')).hexdigest()
    print("Esto es un hash sha224: " + sha224)

    sha1 = hashlib.sha1(clave.encode('utf-8')).hexdigest()
    print("Esto es un hash sha1: " + sha1)

    sha256 = hashlib.sha256(clave.encode('utf-8')).hexdigest()
    print("Esto es un hash sha256: " + sha256)

    sha384 = hashlib.sha384(clave.encode('utf-8')).hexdigest()
    print("Esto es un hash sha384: " + sha384)


if __name__ == '__main__':
    main()
