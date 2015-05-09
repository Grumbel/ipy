ipy - Interactive Python Console
================================

A simple interactive Python console, very similar to:

    python3 -i some-script.py

The difference is that `ipy` will jump directly to the interactive
console after loading the Python file without executing the `if
__name__ == "__main__"` block.

`ipy` can also provide info an what got defined in the script with the
`-v` option:

    $ ipy hello_world.py -v
    loading file 'hello_world.py'

    bar = <function bar at 0x7fba6f30c620>
    main = <function main at 0x7fba6f30c730>
    foo = <function foo at 0x7fba6f30c598>
    >>>

And is able to load multiple scripts into the console:

    $ ipy hello_world.py  hello_world2.py
