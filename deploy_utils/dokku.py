import os

import sys
from decouple import config


def main(argv):
    """

    :param argv:
    -a --app_dokku  = <app name in dokku>
    -s --server_ip
    -h --allowed_hosts
    -d --disable_collectstatic
    # dokku run reclamaparaguai python manage.py migrate
    # dokku config:set reclamaparaguai
    # ssh root@162.243.252.146
    # DEBUG=False ma collectstatic
    # devdokku run reclamaparaguai python manage.py loaddata src/reclamacoes/fixtures/reclamacoes.json
    # http://reclamaparaguai.66.175.216.177.xip.io - test server
    # ./manage.py loaddata src/core/fixtures/empresas.json
    # ./manage.py loaddata src/reclamacoes/fixtures/reclamacoes.json
    # ./manage.py loaddata src/fixtures/users.json
    # ./manage.py  dumpdata auth.User --indent=2 > user2.json
    # ../../manage.py makemessages -l es
    :return:
    """
    disable_static = False
    app_name_dokku = config('DOKKU_APP_NAME', 'dokku_app_name_not_configured')
    test = False
    server_ip = config('SERVER_IP', 'server_ip_not_configured')
    to_server = ''

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-cs', '--config_set')
    args = parser.parse_args()

    if args.config_set:
        to_server = args.config_set

    if args.test:
        print('ssh dokku@{ip} config:set {app_name} {args}'.format(ip=server_ip, app_name=app_name_dokku, args=to_server))
    else:
        pass
            # os.system('ssh dokku@{ip} config:set {app_name} {args}'.format(ip=server_ip,
            #                                                                app_name=app_name_dokku,
            #                                                                args=to_server))

    print("~ cs: {}".format(args.config_set))
    #
    # try:
    #     opts, args = getopt.getopt(argv, "hasdhoststtcstest:",
    #                                ['cs', 'test'])
    # except getopt.GetoptError:
    #     print('dokku.py -cs <config:set>')
    #     sys.exit(2)
    #
    # print(argv)
    # for opt, arg in opts:
    #     print(opt, arg)
    #     if opt == '-h':
    #         print('dokku.py -cs <config:set>')
    #         sys.exit()
    #     elif opt in ("-cs", "--config_set"):
    #         if len(arg) > 0:
    #             to_server = arg
    #         else:
    #             print('dokku.py -cs <Variavel>:<Valor> <Variavel>:<Valor> ...\nExemplo dokku.py -cs DEBUG:FALSE')
    #             sys.exit()
    #
    #     if opt in ("-t", "--test"):
    #         test = True
    #
    # if test:
    #     print('ssh dokku@{ip} config:set {app_name} {args}'.format(ip=server_ip, app_name=app_name_dokku,args=to_server))
    # else:
    #     pass
    #         # os.system('ssh dokku@{ip} config:set {app_name} {args}'.format(ip=server_ip,
    #         #                                                                app_name=app_name_dokku,
    #         #                                                                args=to_server))


if __name__ == "__main__":
    main(sys.argv[1:])