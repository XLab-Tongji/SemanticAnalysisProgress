##Python——argparse学习

[TOC]

###入门

argparse是一个完整的参数处理库。参数可以根据add_argument()的action选项触发不同action。支持的action有存储参数（单个，或作为列表的一部分）;存储常量的值（对布尔开关true/false有特殊处理）。默认动作是存储参数值。支持type(指定存储类型)和dest(指定存储变量)等参数。

然后使用函数parse_args()进行参数解析，这个函数的输入默认是sys.argv[1:]，也可以使用其他字符串列表。选项使用GNU/POSIX语法处理，可以混合选项和参数值。parse_args的返回值是一个包含命令参数的Namespace。所有参数以属性的形式存在，比如args.myoption。

````python
parse.add_argument('pkg',help='help')
//这是最基础的参数格式，如果是这样的格式，说明pkg是一个必须的参数，如果不加入这样的参数，则会报错。
````

##### 设置一个解析器

使用argparse的第一步就是创建一个解析器对象，并告诉它将会有些什么参数。那么当你的程序运行时，该解析器就可以用于处理命令行参数。

解析器类是 **ArgumentParser** 。构造方法接收几个参数来设置用于程序帮助文本的描述信息以及其他全局的行为或设置。

````python
import argparse			//导入命令行解析的库文件

parser = argparse.ArgumentParser(description='This is a PyMOTW sample program')												//为了别人执行代码的时候用--help看出来怎么使用这些代码
````

#####定义参数 

argparse是一个全面的参数处理库。参数可以触发不同的动作，动作由 **add_argument()** 方法的 *action* 参数指定。 支持的动作包括保存参数（逐个地，或者作为列表的一部分），当解析到某参数时保存一个常量值（包括对布尔开关真/假值的特殊处理），统计某个参数出现的次数，以及调用一个回调函数。

默认的动作是保存参数值。在这种情况下，如果提供一个类型，那么在存储之前会先把该参数值转换成该类型。如果提供 *dest* 参数，参数值就保存为命令行参数解析时返回的命名空间对象中名为该 *dest* 参数值的一个属性。

#####解析一个命令行

定义了所有参数之后，你就可以给 **parse_args()** 传递一组参数字符串来解析命令行。默认情况下，参数是从 sys.argv[1:] 中获取，但你也可以传递自己的参数列表。选项是使用GNU/POSIX语法来处理的，所以在序列中选项和参数值可以混合。

**parse_args()** 的返回值是一个**命名空间**，包含传递给命令的参数。该对象将参数保存其属性，因此如果你的参数 dest 是 "myoption"，那么你就可以args.myoption 来访问该值。



下面是一个简单的示例：argparse_short.py

以下简单示例带有3个不同的选项：一个布尔选项（-a），一个简单的字符串选项（-b），以及一个整数选项（-c）。

````python
import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print(parser.parse_args(['-a', '-bval', '-c', '3']))
````

执行结果：

````shell
$ python3 argparse_short.py
Namespace(a=True, b='val', c=3)
````

长参数argparse_long.py：

````python
import argparse

parser = argparse.ArgumentParser(
    description='Example with long option names',
)

parser.add_argument('--noarg', action="store_true",
                    default=False)
parser.add_argument('--witharg', action="store",
                    dest="witharg")
parser.add_argument('--witharg2', action="store",
                    dest="witharg2", type=int)

print(
    parser.parse_args(
        ['--noarg', '--witharg', 'val', '--witharg2=3']
    )
)
````

执行结果：

````shell
$ python3 argparse_long.py
Namespace(noarg=True, witharg='val', witharg2=3)
````

混合可选和必选参数：argparse_arguments.py

````python
import argparse

parser = argparse.ArgumentParser(
    description='Example with nonoptional arguments',
)

parser.add_argument('count', action="store", type=int)
parser.add_argument('units', action="store")

print(parser.parse_args())
````

在这个例子中，“count”参数是一个整数，“units”参数存储为一个字符串。其中任意一个参数若没有在命令行中提供，或给定的值不能被转换为正确的类型，就会报告一个错误。

执行结果：

````shell
$ python3 argparse_arguments.py 3 inches
Namespace(count=3, units='inches')

$ python3 argparse_arguments.py some inches
usage: argparse_arguments.py [-h] count units
argparse_arguments.py: error: argument count: invalid int value:
'some'

$ python3 argparse_arguments.py
usage: argparse_arguments.py [-h] count units
argparse_arguments.py: error: the following arguments are
required: count, units
````

#####参数动作

参数 action 有：

``store``：默认action模式，存储值到指定变量。保存参数值，可能会先将参数值转换成另一个数据类型。若没有显式指定动作，则默认为该动作。
``store_const``：存储值在参数的const部分指定。保存一个被定义为参数规格一部分的值，而不是一个来自参数解析而来的值。这通常用于实现非布尔值的命令行标记。
``store_true / store_false``：可以2个参数对应一个变量。保存相应的布尔值。这两个动作被用于实现布尔开关。
``append``：将值保存到一个列表中。若参数重复出现，则保存多个值（该参数可以重复使用）
``append_const``：将一个定义在参数规格中的值保存到一个列表中，存储值在参数的const部分指定。
``version`` 输出版本信息然后退出。

下面是各种action的示例：argparse_action.py

````python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s', action='store',
                    dest='simple_value',
                    help='Store a simple value')

parser.add_argument('-c', action='store_const',
                    dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')

parser.add_argument('-t', action='store_true',
                    default=False,
                    dest='boolean_t',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false',
                    default=True,
                    dest='boolean_f',
                    help='Set a switch to false')

parser.add_argument('-a', action='append',
                    dest='collection',
                    default=[],
                    help='Add repeated values to a list')

parser.add_argument('-A', action='append_const',
                    dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add different values to list')
parser.add_argument('-B', action='append_const',
                    dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')

parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0')

results = parser.parse_args()
print('simple_value     = {!r}'.format(results.simple_value))
print('constant_value   = {!r}'.format(results.constant_value))
print('boolean_t        = {!r}'.format(results.boolean_t))
print('boolean_f        = {!r}'.format(results.boolean_f))
print('collection       = {!r}'.format(results.collection))
print('const_collection = {!r}'.format(results.const_collection))
````

执行结果如下，注意'simple_value'等被自动化转化为大写：

````shell
$ python3 argparse_action.py -h

usage: argparse_action.py [-h] [-s SIMPLE_VALUE] [-c] [-t] [-f]
                          [-a COLLECTION] [-A] [-B] [--version]

optional arguments:
  -h, --help       show this help message and exit
  -s SIMPLE_VALUE  Store a simple value
  -c               Store a constant value
  -t               Set a switch to true
  -f               Set a switch to false
  -a COLLECTION    Add repeated values to a list
  -A               Add different values to list
  -B               Add different values to list
  --version        show program's version number and exit

$ python3 argparse_action.py -s value

simple_value     = 'value'
constant_value   = None
boolean_t        = False
boolean_f        = True
collection       = []
const_collection = []

$ python3 argparse_action.py -c

simple_value     = None
constant_value   = 'value-to-store'
boolean_t        = False
boolean_f        = True
collection       = []
const_collection = []

$ python3 argparse_action.py -t

simple_value     = None
constant_value   = None
boolean_t        = True
boolean_f        = True
collection       = []
const_collection = []

$ python3 argparse_action.py -f

simple_value     = None
constant_value   = None
boolean_t        = False
boolean_f        = False
collection       = []
const_collection = []

$ python3 argparse_action.py -a one -a two -a three

simple_value     = None
constant_value   = None
boolean_t        = False
boolean_f        = True
collection       = ['one', 'two', 'three']
const_collection = []

$ python3 argparse_action.py -B -A

simple_value     = None
constant_value   = None
boolean_t        = False
boolean_f        = True
collection       = []
const_collection = ['value-2-to-append', 'value-1-to-append']

$ python3 argparse_action.py --version

argparse_action.py 1.0
````



###可选前缀

ArgumentParser 函数中的选项 prefix_chars 可以指定前缀。默认使用UNIX风格，命令行使用‘-’作为前缀。可以使用windows的’/’或者其他符号。

argparse_prefix_chars.py：

````python
import argparse

parser = argparse.ArgumentParser(
    description='Change the option prefix characters',
    prefix_chars='-+/',
)

parser.add_argument('-a', action="store_false",
                    default=None,
                    help='Turn A off',
                    )
parser.add_argument('+a', action="store_true",
                    default=None,
                    help='Turn A on',
                    )
parser.add_argument('//noarg', '++noarg',
                    action="store_true",
                    default=False)

print(parser.parse_args())
````

将**ArgumentParser** 方法的*prefix_chars* 参数设置为一个字符串，该字符串包含所有允许用来表示选项的字符。需要理解的是虽然*prefix_chars*包含允许用于开关的字符，但单个参数定义只能使用一种给定的开关语法。这让你可以对使用不同前缀的选项是否是别名（比如独立于平台的命令行语法的情况）或替代选择（例如，使用“+”表明打开一个开发，“-”则为关闭一个开关）进行显式地控制。在上述例子中，+a和-a是不同的参数，//noarg 也可以 ++noarg 提供，但不是 --noarg。

执行结果：

````shell
$ python3 argparse_prefix_chars.py -h
usage: argparse_prefix_chars.py [-h] [-a] [+a] [//noarg]
Change the option prefix characters
optional arguments:
  -h, --help        show this help message and exit
  -a                Turn A off
  +a                Turn A on
  //noarg, ++noarg

$ python3 argparse_prefix_chars.py +a
Namespace(a=True, noarg=False)

$ python3 argparse_prefix_chars.py -a
Namespace(a=False, noarg=False)

$ python3 argparse_prefix_chars.py //noarg
Namespace(a=None, noarg=True)

$ python3 argparse_prefix_chars.py ++noarg
Namespace(a=None, noarg=True)

$ python3 argparse_prefix_chars.py --noarg
usage: argparse_prefix_chars.py [-h] [-a] [+a] [//noarg]
argparse_prefix_chars.py: error: unrecognized arguments: --noarg
````



###处理配置文件中的参数

argparse_with_shlex.py

```python
import argparse
from configparser import ConfigParser
import shlex

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

config = ConfigParser()
config.read('argparse_with_shlex.ini')
config_value = config.get('cli', 'options')
print('Config  :', config_value)

argument_list = shlex.split(config_value)
print('Arg List:', argument_list)

print('Results :', parser.parse_args(argument_list))
```

其中argparse_with_shlex.ini文件的内容如下：

``````ini
[cli]
options = -a -b 2
``````

执行结果：

````shell
$ python3 argparse_with_shlex.py

Config  : -a -b 2
Arg List: ['-a', '-b', '2']
Results : Namespace(a=True, b='2', c=None)
````

上面例子使用了ConfigParser来读取配置，再用shlex来切割参数。也可以通过fromfile_prefix_chars 告知argparse输入参数为文件。

argparse_fromfile_prefix_chars.py：

````python
import argparse
import shlex

parser = argparse.ArgumentParser(description='Short sample app',
                                 fromfile_prefix_chars='@',
                                 )

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print(parser.parse_args(['@argparse_fromfile_prefix_chars.txt']))
````

argparse_fromfile_prefix_chars.txt：

````txt
-a
-b
2
````

执行结果：

````shell
$ python3 argparse_fromfile_prefix_chars.py
Namespace(a=True, b='2', c=None)
````



###帮助

#####自动生成

Argparse会自动生成的帮助和版本信息。ArgumentParser的add_help参数控制帮助的生成，默认是开启。

argparse_with_help.py：

````python
import argparse

parser = argparse.ArgumentParser(add_help=True)

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print(parser.parse_args())
````

下例就关闭帮助：

argparse_without_help.py：

````python
import argparse

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print(parser.parse_args())
````

执行结果：

````shell
$ python argparse_with_help.py -h
usage: argparse_with_help.py [-h] [-a] [-b B] [-c C]
optional arguments:
-h, --help show this help message and exit
-a
-b B
-c C

$ python argparse_without_help.py -h
usage: argparse_without_help.py [-a] [-b B] [-c C]
argparse_without_help.py: error: unrecognized arguments: -h
````



#####自定义帮助

argparse_custom_help.py：

````python
import argparse

parser = argparse.ArgumentParser(add_help=True)

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print('print_usage output:')
parser.print_usage()
print()

print('print_help output:')
parser.print_help()
````

执行结果：

````shell
$ python3 argparse_custom_help.py

print_usage output:
usage: argparse_custom_help.py [-h] [-a] [-b B] [-c C]

print_help output:
usage: argparse_custom_help.py [-h] [-a] [-b B] [-c C]

optional arguments:
  -h, --help  show this help message and exit
  -a
  -b B
  -c C
````

argparse_raw_description_help_formatter.py：

````python
import argparse

parser = argparse.ArgumentParser(
    add_help=True,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="""
    description
        not
           wrapped""",
    epilog="""
    epilog
      not
         wrapped""",
)

parser.add_argument(
    '-a', action="store_true",
    help="""argument
    help is
    wrapped
    """,
)

parser.print_help()
````

执行结果：

````shell
$ python3 argparse_raw_description_help_formatter.py

usage: argparse_raw_description_help_formatter.py [-h] [-a]

    description
        not
           wrapped

optional arguments:
  -h, --help  show this help message and exit
  -a          argument help is wrapped

    epilog
      not
         wrapped
````

argparse_raw_text_help_formatter.py：

````python
import argparse

parser = argparse.ArgumentParser(
    add_help=True,
    formatter_class=argparse.RawTextHelpFormatter,
    description="""
    description
        not
           wrapped""",
    epilog="""
    epilog
      not
         wrapped""",
)

parser.add_argument(
    '-a', action="store_true",
    help="""argument
    help is not
    wrapped
    """,
)

parser.print_help()
````

执行结果：

````shell
$ python3 argparse_raw_text_help_formatter.py

usage: argparse_raw_text_help_formatter.py [-h] [-a]

    description
        not
           wrapped

optional arguments:
  -h, --help  show this help message and exit
  -a          argument
                  help is not
                  wrapped


    epilog
      not
         wrapped
````

argparse_metavar_type_help_formatter.py：

````python
import argparse

parser = argparse.ArgumentParser(
    add_help=True,
    formatter_class=argparse.MetavarTypeHelpFormatter,
)

parser.add_argument('-i', type=int, dest='notshown1')
parser.add_argument('-f', type=float, dest='notshown2')

parser.print_help()
````

执行结果：

````shell
$ python3 argparse_metavar_type_help_formatter.py

usage: argparse_metavar_type_help_formatter.py [-h] [-i int] [-f
 float]

optional arguments:
  -h, --help  show this help message and exit
  -i int
  -f float
````



###组织解析器

公共解析器:通过父子类来实现。

见argparse_parent_base.py：

````python
import argparse

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('--user', action="store")
parser.add_argument('--password', action="store")
````

argparse_uses_parent.py：

````python
import argparse
import argparse_parent_base

parser = argparse.ArgumentParser(
    parents=[argparse_parent_base.parser],
)

parser.add_argument('--local-arg',
                    action="store_true",
                    default=False)

print(parser.parse_args())
````

注意：父类关闭了help。子类却默认开启了help。执行结果：

````shell
$ python3 argparse_uses_parent.py -h

usage: argparse_uses_parent.py [-h] [--user USER]
                               [--password PASSWORD]
                               [--local-arg]

optional arguments:
  -h, --help           show this help message and exit
  --user USER
  --password PASSWORD
  --local-arg
````



###参数冲突

argparse_conflict_handler_resolve.py：

```python
import argparse

parser = argparse.ArgumentParser(conflict_handler='resolve')

parser.add_argument('-a', action="store")
parser.add_argument('-b', action="store", help='Short alone')
parser.add_argument('--long-b', '-b',
                    action="store",
                    help='Long and short together')

print(parser.parse_args(['-h']))

```

执行结果：

````shell
$ python3 argparse_conflict_handler_resolve.py

usage: argparse_conflict_handler_resolve.py [-h] [-a A]
[--long-b LONG_B]

optional arguments:
  -h, --help            show this help message and exit
  -a A
  --long-b LONG_B, -b LONG_B
                        Long and short together
````

argparse_conflict_handler_resolve2.py：

````shell
import argparse

parser = argparse.ArgumentParser(conflict_handler='resolve')

parser.add_argument('-a', action="store")
parser.add_argument('--long-b', '-b',
                    action="store",
                    help='Long and short together')
parser.add_argument('-b', action="store", help='Short alone')

print(parser.parse_args(['-h']))
````

执行结果：

````shell
$ python3 argparse_conflict_handler_resolve2.py

usage: argparse_conflict_handler_resolve2.py [-h] [-a A]
                                             [--long-b LONG_B]
                                             [-b B]

optional arguments:
  -h, --help       show this help message and exit
  -a A
  --long-b LONG_B  Long and short together
  -b B             Short alone
````



###参数分组

默认有可选参数和必选参数组。

argparse_default_grouping.py：

````python
import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('--optional', action="store_true",
                    default=False)
parser.add_argument('positional', action="store")

print(parser.parse_args())
````

执行结果：

````shell
$ python3 argparse_default_grouping.py -h

usage: argparse_default_grouping.py [-h] [--optional] positional

Short sample app

positional arguments:
  positional

optional arguments:
  -h, --help  show this help message and exit
  --optional
````

前面的用户名和密码就可以分组：

argparse_parent_with_group.py：

````python
import argparse

parser = argparse.ArgumentParser(add_help=False)

group = parser.add_argument_group('authentication')

group.add_argument('--user', action="store")
group.add_argument('--password', action="store")
````

argparse_uses_parent_with_group.py：

````python
import argparse
import argparse_parent_with_group

parser = argparse.ArgumentParser(
    parents=[argparse_parent_with_group.parser],
)

parser.add_argument('--local-arg',
                    action="store_true",
                    default=False)

print(parser.parse_args())
````

执行结果：

````shell
$ python3 argparse_uses_parent_with_group.py -h

usage: argparse_uses_parent_with_group.py [-h] [--user USER]
                                          [--password PASSWORD]
                                          [--local-arg]

optional arguments:
  -h, --help           show this help message and exit
  --local-arg

authentication:
  --user USER
  --password PASSWORD
````



###互斥选项

使用add_mutually_exclusive_group()可以添加互斥选项：

argparse_mutually_exclusive.py：

````python
import argparse

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('-a', action='store_true')
group.add_argument('-b', action='store_true')

print(parser.parse_args())
````

执行结果：

````shell
$ python3 argparse_mutually_exclusive.py -h
usage: argparse_mutually_exclusive.py [-h] [-a | -b]
optional arguments:
  -h, --help  show this help message and exit
  -a
  -b

$ python3 argparse_mutually_exclusive.py -a
Namespace(a=True, b=False)

$ python3 argparse_mutually_exclusive.py -b
Namespace(a=False, b=True)

$ python3 argparse_mutually_exclusive.py -a -b
usage: argparse_mutually_exclusive.py [-h] [-a | -b]
argparse_mutually_exclusive.py: error: argument -b: not allowed
with argument -a
````



###嵌套解析

argparse_subparsers.py：

```python
import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='commands')

# A list command
list_parser = subparsers.add_parser(
    'list', help='List contents')
list_parser.add_argument(
    'dirname', action='store',
    help='Directory to list')

# A create command
create_parser = subparsers.add_parser(
    'create', help='Create a directory')
create_parser.add_argument(
    'dirname', action='store',
    help='New directory to create')
create_parser.add_argument(
    '--read-only', default=False, action='store_true',
    help='Set permissions to prevent writing to the directory',
)

# A delete command
delete_parser = subparsers.add_parser(
    'delete', help='Remove a directory')
delete_parser.add_argument(
    'dirname', action='store', help='The directory to remove')
delete_parser.add_argument(
    '--recursive', '-r', default=False, action='store_true',
    help='Remove the contents of the directory, too',
)

print(parser.parse_args())
```

执行结果：

````shell
$ python3 argparse_subparsers.py -h

usage: argparse_subparsers.py [-h] {list,create,delete} ...

positional arguments:
  {list,create,delete}  commands
    list                List contents
    create              Create a directory
    delete              Remove a directory

optional arguments:
  -h, --help            show this help message and exit

$ python3 argparse_subparsers.py create -h

usage: argparse_subparsers.py create [-h] [--read-only] dirname

positional arguments:
  dirname      New directory to create

optional arguments:
  -h, --help   show this help message and exit
  --read-only  Set permissions to prevent writing to the directo
ry

$ python3 argparse_subparsers.py delete -r foo

Namespace(dirname='foo', recursive=True)
````



###高级参数处理

可变参数：数字N代表N的参数，？0或者1个参数。*0或者多个参数。+1或者多个参数。

argparse_nargs.py

````python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--three', nargs=3)
parser.add_argument('--optional', nargs='?')
parser.add_argument('--all', nargs='*', dest='all')
parser.add_argument('--one-or-more', nargs='+')

print(parser.parse_args())
````

执行结果：

````shell
$ python3 argparse_nargs.py -h

usage: argparse_nargs.py [-h] [--three THREE THREE THREE]
                [--optional [OPTIONAL]]
                [--all [ALL [ALL ...]]]
                [--one-or-more ONE_OR_MORE [ONE_OR_MORE ...]]

optional arguments:
  -h, --help            show this help message and exit
  --three THREE THREE THREE
  --optional [OPTIONAL]
  --all [ALL [ALL ...]]
  --one-or-more ONE_OR_MORE [ONE_OR_MORE ...]

$ python3 argparse_nargs.py

Namespace(all=None, one_or_more=None, optional=None, three=None)

$ python3 argparse_nargs.py --three

usage: argparse_nargs.py [-h] [--three THREE THREE THREE]
                [--optional [OPTIONAL]]
                [--all [ALL [ALL ...]]]
                [--one-or-more ONE_OR_MORE [ONE_OR_MORE ...]]
argparse_nargs.py: error: argument --three: expected 3
argument(s)

$ python3 argparse_nargs.py --three a b c

Namespace(all=None, one_or_more=None, optional=None,
three=['a', 'b', 'c'])

$ python3 argparse_nargs.py --optional

Namespace(all=None, one_or_more=None, optional=None, three=None)

$ python3 argparse_nargs.py --optional with_value

Namespace(all=None, one_or_more=None, optional='with_value',
three=None)

$ python3 argparse_nargs.py --all with multiple values

Namespace(all=['with', 'multiple', 'values'], one_or_more=None,
optional=None, three=None)

$ python3 argparse_nargs.py --one-or-more with_value

Namespace(all=None, one_or_more=['with_value'], optional=None,
three=None)

$ python3 argparse_nargs.py --one-or-more with multiple values

Namespace(all=None, one_or_more=['with', 'multiple', 'values'],
optional=None, three=None)

$ python3 argparse_nargs.py --one-or-more

usage: argparse_nargs.py [-h] [--three THREE THREE THREE]
                [--optional [OPTIONAL]]
                [--all [ALL [ALL ...]]]
                [--one-or-more ONE_OR_MORE [ONE_OR_MORE ...]]
argparse_nargs.py: error: argument --one-or-more: expected
at least one argument
````



###参数类型

argparse_type.py：

````python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', type=int)
parser.add_argument('-f', type=float)
parser.add_argument('--file', type=open)

try:
    print(parser.parse_args())

except IOError as msg:
    parser.error(str(msg))
````

执行结果：

````shell
$ python3 argparse_type.py -i 1
Namespace(f=None, file=None, i=1)

$ python3 argparse_type.py -f 3.14
Namespace(f=3.14, file=None, i=None)

$ python3 argparse_type.py --file argparse_type.py
Namespace(f=None, file=<_io.TextIOWrapper
name='argparse_type.py' mode='r' encoding='UTF-8'>, i=None)

$ python3 argparse_type.py -i a
usage: argparse_type.py [-h] [-i I] [-f F] [--file FILE]
argparse_type.py: error: argument -i: invalid int value: 'a'

$ python3 argparse_type.py -f 3.14.15
usage: argparse_type.py [-h] [-i I] [-f F] [--file FILE]
argparse_type.py: error: argument -f: invalid float value:
'3.14.15'

$ python3 argparse_type.py --file does_not_exist.txt
usage: argparse_type.py [-h] [-i I] [-f F] [--file FILE]
argparse_type.py: error: [Errno 2] No such file or directory:
'does_not_exist.txt'
````

Choices可以指定参数的选项：

argparse_choices.py：

````python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '--mode',
    choices=('read-only', 'read-write'),
)

print(parser.parse_args())
````

执行结果：

````shell
$ python3 argparse_choices.py -h

usage: argparse_choices.py [-h] [--mode {read-only,read-write}]

optional arguments:
  -h, --help            show this help message and exit
  --mode {read-only,read-write}

$ python3 argparse_choices.py --mode read-only

Namespace(mode='read-only')

$ python3 argparse_choices.py --mode invalid

usage: argparse_choices.py [-h] [--mode {read-only,read-write}]
argparse_choices.py: error: argument --mode: invalid choice:
'invalid' (choose from 'read-only', 'read-write')
````



###文件参数

argparse_FileType.py：

````python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', metavar='in-file',
                    type=argparse.FileType('rt'))
parser.add_argument('-o', metavar='out-file',
                    type=argparse.FileType('wt'))

try:
    results = parser.parse_args()
    print('Input file:', results.i)
    print('Output file:', results.o)
except IOError as msg:
    parser.error(str(msg))
````

执行结果：

````shell
$ python3 argparse_FileType.py -h

usage: argparse_FileType.py [-h] [-i in-file] [-o out-file]

optional arguments:
  -h, --help   show this help message and exit
  -i in-file
  -o out-file

$ python3 argparse_FileType.py -i argparse_FileType.py -o tmp_\
file.txt

Input file: <_io.TextIOWrapper name='argparse_FileType.py'
mode='rt' encoding='UTF-8'>
Output file: <_io.TextIOWrapper name='tmp_file.txt' mode='wt'
encoding='UTF-8'>

$ python3 argparse_FileType.py -i no_such_file.txt

usage: argparse_FileType.py [-h] [-i in-file] [-o out-file]
argparse_FileType.py: error: argument -i: can't open
'no_such_file.txt': [Errno 2] No such file or directory:
'no_such_file.txt'
````



###自定义action

自定义action是argparse.Action的子类可以处理add_argument中的参数定义相关的参数，并返回一个可调用对象。构造函数会处理参数定义，仅仅需要处理**call**函数。**call**函数中parser代表解释器，namespace用于返回解释结果，value为要处理的参数，option_string用于触发action（对可选参数，永远是None。

argparse_custom_action.py：

````python
import argparse


class CustomAction(argparse.Action):
    def __init__(self,
                 option_strings,
                 dest,
                 nargs=None,
                 const=None,
                 default=None,
                 type=None,
                 choices=None,
                 required=False,
                 help=None,
                 metavar=None):
        argparse.Action.__init__(self,
                                 option_strings=option_strings,
                                 dest=dest,
                                 nargs=nargs,
                                 const=const,
                                 default=default,
                                 type=type,
                                 choices=choices,
                                 required=required,
                                 help=help,
                                 metavar=metavar,
                                 )
        print('Initializing CustomAction')
        for name, value in sorted(locals().items()):
            if name == 'self' or value is None:
                continue
            print('  {} = {!r}'.format(name, value))
        print()
        return

    def __call__(self, parser, namespace, values,
                 option_string=None):
        print('Processing CustomAction for {}'.format(self.dest))
        print('  parser = {}'.format(id(parser)))
        print('  values = {!r}'.format(values))
        print('  option_string = {!r}'.format(option_string))

        # Do some arbitrary processing of the input values
        if isinstance(values, list):
            values = [v.upper() for v in values]
        else:
            values = values.upper()
        # Save the results in the namespace using the destination
        # variable given to our constructor.
        setattr(namespace, self.dest, values)
        print()


parser = argparse.ArgumentParser()

parser.add_argument('-a', action=CustomAction)
parser.add_argument('-m', nargs='*', action=CustomAction)

results = parser.parse_args(['-a', 'value',
                             '-m', 'multivalue',
                             'second'])
print(results)
````

执行结果：

````shell
$ python3 argparse_custom_action.py

Initializing CustomAction
  dest = 'a'
  option_strings = ['-a']
  required = False

Initializing CustomAction
  dest = 'm'
  nargs = '*'
  option_strings = ['-m']
  required = False

Processing CustomAction for a
  parser = 4315836992
  values = 'value'
  option_string = '-a'

Processing CustomAction for m
  parser = 4315836992
  values = ['multivalue', 'second']
  option_string = '-m'

Namespace(a='VALUE', m=['MULTIVALUE', 'SECOND'])
````



