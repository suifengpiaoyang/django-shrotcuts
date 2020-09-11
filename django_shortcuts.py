import os
import sys
import shutil
import argparse

# 切换到 manage.py 路径下，运行此脚本。

add_flag = ["all", "forms", "urls", "templates", "static"]


def check_exists(path):
    if os.path.exists(path):
        print('{} existed.'.format(path))
        return True
    else:
        return False


def generate_file(path):
    if not check_exists(path):
        with open(path, 'w', encoding='utf-8')as fl:
            pass
        print('Generate {} successfully.'.format(path))


def generate_file_from_template(app_path, templates_path, flag, app_name):
    generate_file_name = '{}.py'.format(flag)
    templates_file_path = os.path.join(templates_path, generate_file_name)
    generate_file_path = os.path.join(app_path, generate_file_name)
    if not check_exists(generate_file_path):
        if flag == 'forms':
            shutil.copy(templates_file_path, generate_file_path)
        elif flag == 'urls':
            with open(templates_file_path)as fl:
                data = fl.read().replace('{{ app_name }}', app_name)
            with open(generate_file_path, 'w', encoding='utf-8')as fl:
                fl.write(data)
        print('Generate {} successfully.'.format(generate_file_path))


def add_files(flag, file=None):
    current_path = os.path.abspath('.')
    execute_file = sys.executable
    execute_path = os.path.dirname(execute_file)
    app_path = os.path.join(current_path, args.app)
    if execute_file.endswith('python.exe'):
        templates_path = os.path.join(current_path, 'files')
    else:
        templates_path = os.path.join(execute_path, 'files')
    if flag in ('forms', 'urls'):
        generate_file_from_template(app_path, templates_path, flag, args.app)
    elif flag in ('templates', 'static'):
        target_path = os.path.join(app_path, flag, args.app)
        if not os.path.exists(target_path):
            os.makedirs(target_path)
            print('Generate {} successfully.'.format(target_path))
        if file is None:
            if flag == 'templates':
                file = 'index.html'
            elif flag == 'static':
                file = 'style.css'
        file_path = os.path.join(target_path, file)
        generate_file(file_path)

parser = argparse.ArgumentParser()
parser.add_argument('--app', help='type the app name', required=True)
parser.add_argument('-a',
                    '--add',
                    help='add file automatically, the value must be one of {}'.format(
                        add_flag),
                    )
parser.add_argument('-t', '--templates', help='add templates html file')
parser.add_argument('-s', '--static', help='add static css file')

args = parser.parse_args()

if args.app not in os.listdir():
    print('The app [{}] not in the current path, please check again and run later.'.format(
        args.app))
    sys.exit()

if args.add:
    if args.add in add_flag:
        if args.add == 'all':
            for each in add_flag:
                add_files(each)
        elif args.add in ('forms', 'urls'):
            add_files(args.add)
        elif args.add == 'templates':
            add_files(args.add,)
        elif args.add == 'static':
            add_files(args.add)
    else:
        print(
            'The add values must be one of {}'.format(add_flag))
        sys.exit()

if args.templates:
    add_files(flag='templates', file=args.templates)

if args.static:
    add_files(flag='static', file=args.static)
