from lib.command import SysCommand
from lib.colors import colored, Colors


command = 'paccache -rvk1'
cache_path = '/var/cache/pacman/pkg'
arrow = colored('==>', Colors.green)
dots = colored('::', Colors.cyan)

output = SysCommand(command).split()
pkg_list = []

if len(output) == 1:
    message = f'{arrow} No hay paquetes en cache para eliminar.'
else:
    for pkg in output:
        if "finished" in pkg:
            info = pkg.split(':')
            _pkg = info[1].split()[0]
            disk = info[2].strip()[:-1]
            mesagge = f'{arrow} Eliminados {_pkg} paquetes. Espacio ahorrado {disk}'
        elif '' == pkg:
            continue
        elif 'Candidate packages:' in pkg:
            pkg_list.append(f'{arrow} Paquetes eencontrados:')
        else:
            pkg_list.append(f'{dots}  El paquetes {pkg.removeprefix(cache_path)} ha sido eiminado')
pkg_list.append(mesagge)

print('\n'.join(pkg_list))