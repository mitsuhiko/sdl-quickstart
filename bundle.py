#!/usr/bin/env python
import os
from urllib import urlopen


FILENAME = 'sdl-quickstart.py'
CODE = r'''\
import re
import os
from subprocess import Popen


template_re = re.compile(r'%([a-zA-Z]+)%')


def get_input(prompt, default=None):
    if default:
        prompt = '%s [%s]' % (prompt, default)
    while 1:
        rv = raw_input('%s: ' % prompt)
        if not rv:
            rv = default
        if rv:
            return rv


def apply_template(string, context):
    def handle_match(match):
        key = match.group(1)
        if key in context:
            return context[key]
        return match.group(0)
    return template_re.sub(handle_match, string)


def main():
    project_name = get_input('Project name')
    namespace = get_input('Namespace', project_name.lower())
    context = {
        'namespace':        namespace,
        'NAMESPACE':        namespace.upper(),
        'projectname':      project_name,
        'PROJECTNAME':      project_name.upper()
    }

    print 'Extracting starter template'
    target_folder = project_name
    for fn, value in PACKAGED_FILES.iteritems():
        value = value.decode('base64').decode('zlib')
        fn = os.path.join(target_folder, apply_template(fn, context))
        dirname = os.path.dirname(fn)
        if dirname and not os.path.isdir(dirname):
            os.makedirs(dirname)
        f = open(fn, 'w')
        f.write(apply_template(value, context))
        f.close()
    print 'Cloning SDL 1.3'
    Popen(['hg', 'clone', 'http://hg.libsdl.org/SDL', 'libs/sdl-1.3']).wait()
    print 'All done'
    print
    print 'Now build SDL 1.3 in the libs folder for your platform'
    print 'On OS X and Linux build it like this:'
    print
    print '  $ cd libs/sdl-1.3'
    print '  $ ./configure --prefix=`pwd`/local'
    print '  $ make && make install'
    print
    print 'On windows open the VisualC folder and build the SDL and SDLmain'
    print 'solutions.'


PACKAGED_FILES = ###FILEDUMP###


if __name__ == '__main__':
    main()
'''


ignored_files = set([FILENAME, __file__.rstrip('c'), 'README'])


def collect_all_files():
    result = {}
    for path, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            if filename in ignored_files:
                continue
            fn = os.path.join(path, filename)
            fn = fn.replace('\\', '/')
            dirnames[:] = [x for x in dirnames if not x == '.git']
            with open(fn, 'r') as f:
                result[fn] = f.read()

    resp = urlopen('https://github.com/mitsuhiko/frameworkify/raw/master/frameworkify.py')
    result['scripts/frameworkify.py'] = resp.read()
    resp.close()

    return result


def main():
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    files = collect_all_files()
    with open(FILENAME, 'w') as f:
        f.write(CODE.replace('###FILEDUMP###', '{\n%s}' % ',\n'.join(
            '%r: """\n%s"""' % (k, v.encode('zlib').encode('base64'))
            for k, v in files.iteritems())))


if __name__ == '__main__':
    main()
