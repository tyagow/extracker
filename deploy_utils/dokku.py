import os

import sys
from decouple import config


def main(argv):
    """
    :param argv:
    """
    disable_static = False
    app_name_dokku = config('DOKKU_APP_NAME', default='dokku_app_name_not_configured')
    test = False
    server_ip = config('SERVER_IP', default='server_ip_not_configured')
    to_server = ''

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-cs', '--config_set')
    parser.add_argument('-m', '--migrate')
    parser.add_argument('-t', '--test', action="store_true")
    args = parser.parse_args()

    if args.config_set:
        to_server = ' config:set {app_name} {args}'.format(app_name=app_name_dokku, args=args.config_set)
    elif args.migrate:
        to_server = ' run {app_name} python manage.py migrate '.format(app_name=app_name_dokku)

    if args.test:
        print('ssh dokku@{ip} {args}'.format(ip=server_ip, args=to_server))
    else:
        print('[SERVER]: ssh dokku@{ip} {args}'.format(ip=server_ip, args=to_server))

            # os.system('ssh dokku@{ip} config:set {app_name} {args}'.format(ip=server_ip,
            #                                                                app_name=app_name_dokku,
            #                                                                args=to_server))

    # print("~ cs: {}".format(args.config_set))
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