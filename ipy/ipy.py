#!/usr/bin/env python3

# ipy - Interactive Python Console
# Copyright (C) 2015 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import code
import readline
import rlcompleter
import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description='Interactive Python Console')
    parser.add_argument('FILE', action='store', type=str, nargs='*',
                        help='Load FILE into the interactive interpreter')
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help='Be more verbose')
    parser.add_argument('-c', '--command', metavar="COMMAND", type=str, action='append',
                        help='Execute COMMAND')
    parser.add_argument('-q', '--quit', action='store_true', default=False,
                        help='Exit after executing all files and commands')
    parser.add_argument('--main', action='store_true', default=False,
                        help='Execute the \'__name__ == "__main__"\' block')
    return parser.parse_args()


def main():
    args = parse_args()

    global_vars = {}

    if args.main:
        global_vars['__name__'] = "__main__"

    for script_filename in args.FILE:
        if args.verbose:
            print("loading file '{}'".format(script_filename))

        with open(script_filename) as fin:
            func = compile(fin.read(), script_filename, 'exec')
            exec(func, global_vars)
    if args.verbose and args.FILE:
        print()

    if args.command is not None:
        for command in args.command:
            if args.verbose:
                print("executing: '{}'".format(command))
            func = compile(command, "command", 'exec')
            exec(func, global_vars)

    if args.verbose and args.command:
        print()


    readline.set_completer(rlcompleter.Completer(global_vars).complete)
    readline.parse_and_bind("tab: complete")

    if args.verbose:
        for k, v in global_vars.items():
            if k != "__builtins__":
                print("{} = {}".format(k, v))
        print()

    if not args.quit:
        history_file = os.path.expanduser("~/.ipy_history")
        if os.path.exists(history_file):
            readline.read_history_file(history_file)

        code.interact(banner="", local=global_vars)

        readline.write_history_file(history_file)


def main_entrypoint():
    main()


if __name__ == "__main__":
    main()


# EOF #
