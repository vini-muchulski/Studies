import platform
import socket
from datetime import datetime
import getpass

print("NOME DA MAQUINA........",platform.node())
print("ARQUITETURA............",platform.architecture())


print("SO.....................",platform.system())
print("versao so..............",platform.release())
print("processador............",platform.processor())
print("versao do python.......",platform.python_version())

ip = socket.gethostbyname(socket.gethostname())
print("IP.....................",ip)

print("Hora local.............",datetime.now())

print("User...................",getpass.getuser())


