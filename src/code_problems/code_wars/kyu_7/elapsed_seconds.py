from datetime import datetime


def elapsed_seconds(start: datetime, end: datetime):
    """o uso do .seconds falha caso o intervalo das datas sejam em dias diferentes
    nos testes do execício todos os casos são do mesmo dia, logo não vai falhar,
    mas o mais correto seria usar o total_seconds()"""
    return (end - start).total_seconds()