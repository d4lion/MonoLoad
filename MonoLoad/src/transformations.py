from os import getcwd
from typing import Optional, Union


def transform_config_to_dict(config_path: Optional[str] = getcwd()+"/src/page.config") -> dict:

    with open(config_path, "r+") as f:
        lineas: list = list(f.readlines())

        listas_limpia: list[str] = [linea.strip() for linea in lineas]

        lista_valores_tupla: list[tuple[Union[str, int]]] = []

        for elemento in listas_limpia:
            clave, valor = elemento.split("=")
            if valor.isdigit():
                lista_valores_tupla.append((clave, int(valor)))
            elif isinstance(eval(valor), bool):
                lista_valores_tupla.append((clave, eval(valor)))
            else:
                lista_valores_tupla.append((clave, valor))

        return dict(lista_valores_tupla)
