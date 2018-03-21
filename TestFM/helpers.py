# helpers required for TestFM
import os


def product():
    sat_version = os.popen(
        'ansible -i TestFM/inventory foreman --user root -m shell '
        '-a "rpm -q satellite --queryformat=%{VERSION}" -o').read()
    project = sat_version.splitlines()[0].split(' ')[-1]
    if project.startswith('6.3'):
        return 'sat63'
    elif project.startswith('6.2'):
        return 'sat62'
    else:
        return 'sat61'
