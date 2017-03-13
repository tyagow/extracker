import os

import sys, getopt
from decouple import config


def main(argv):
    """

    :param argv:
    -a --app_dokku  = <app name in dokku>
    -s --server_ip
    -h --allowed_hosts
    -d --disable_collectstatic

    :return:
    """
    disable_static = False
    app_name_dokku = 'tety'
    test = False
    server_ip = config('SERVER_IP', '104.236.104.21')
    allowed_hosts_target = 'tety.104.236.104.21.xip.io'
    # os.system('ssh dokku@104.236.104.21  config facebot')
    to_server = ''
    try:
        opts, args = getopt.getopt(argv, "hasdhoststt:",
                                   ["app_dokku=", "server_ip=", "allowed_hosts=",
                                    "disable_collectstatic", "hosts", "test"])
    except getopt.GetoptError:
        print('cconfig_dokku.py -a <app name dokku> -s <server ip>'
              ' -hosts <allowed hosts> -d --disable_collectstatic -t --test')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('config_dokku.py -a <app name dokku> -s <server ip>'
                  ' -hosts <allowed hosts> -d --disable_collectstatic -t --test')
            sys.exit()
        elif opt in ("-a", "--app_dokku"):
            if len(arg) > 0:
                app_name_dokku = arg
            else:
                print('config_dokku.py -a <app name dokku>')
                sys.exit()

        elif opt in ("-s", "--server_ip"):
            if len(arg) > 0:
                server_ip = arg
            else:
                print('config_dokku.py -s|--server_ip <server ip>')
                sys.exit()

        elif opt in ("-hosts", "--allowed_hosts"):
            if len(arg) > 0:
                allowed_hosts_target = arg
            else:
                print('config_dokku.py -hosts <allowed host>')
                sys.exit()
        elif opt in ("-d", "--disable_collectstatic"):
            disable_static = True
        elif opt in ("-t", "--test"):
            test = True

    with open('.env') as file:
        for line in file:

            if not line[:1] == '#':
                line = line[:-1].split('=')
                if line[0] == 'ALLOWED_HOSTS':
                    line = '{}={}'.format('ALLOWED_HOSTS', str(allowed_hosts_target))
                    to_server = '{} {}'.format(to_server, str(line))
                elif line[0] == 'SECRET_KEY':
                    line = "{}='{}'".format('SECRET_KEY', str(line[1]))
                    to_server = "{} {}".format(to_server, str(line))
                else:
                    if len(line[1]) > 1:
                        line = '{}={}'.format(line[0], line[1])
                        to_server = '{} {}'.format(to_server, str(line))
                    else:
                        # to_server = '{} error{}error'.format(to_server, str(line))
                        print('Error line: %s' % line)
        if disable_static:
            to_server = '{} {}'.format(to_server, ' DISABLE_COLLECTSTATIC=1')
        if test:
            print('ssh dokku@{ip} config:set {app_name} {args}'.format(ip=server_ip, app_name=app_name_dokku,args=to_server))
        else:
            os.system('ssh dokku@{ip} config:set {app_name} {args}'.format(ip=server_ip,
                                                                           app_name=app_name_dokku,
                                                                           args=to_server))

if __name__ == "__main__":
    main(sys.argv[1:])