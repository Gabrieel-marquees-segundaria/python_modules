from texto import texto
from logguer import logger, configure_logger

logger = configure_logger()

def gzip_base_64(texto):
    """ compacta o texto em base64 e gzip

    Args:
        texto (_type_): texto a ser compactado
    """
    import base64
    import gzip
    texto_compact = gzip.compress(texto.encode())
    
    logger.info(f" - gzip_base_64 - ttexto compactado {texto_compact[:10]}..... {texto_compact[-10:]}")
    logger.info(f' - gzip_base_64 - tamanho do texto compactado {len(texto_compact)}')
    texto_descompact = gzip.decompress(texto_compact)
    logger.info(f" - gzip_base_64 - texto descompactado {texto_descompact[:20]}..... {texto_descompact[-20:]}")
    logger.info(f' - gzip_base_64 - tamanho do texto descompactado {len(texto_descompact)}')


def msgpack(texto):
    import msgpack
    compactado = msgpack.dumps(texto)
    logger.info(f" - msgpack - texto compactado {compactado[:10]}..... {compactado[-10:]}")
    logger.info(f' - msgpack - tamanho do texto compactado {len(compactado)}')
    descompactado = msgpack.loads(compactado)
    logger.info(f" - msgpack - texto descompactado {descompactado[:20]}..... {descompactado[-20:]}")
    logger.info(f' - msgpack - tamanho do texto descompactado {len(descompactado)}')


if __name__ == "__main__":
    gzip_base_64(texto)
    msgpack(texto)


