import sys
import os
import argparse
import ast
from . import bundle_prefs_file, read_prefs_file, convert_to_prefs, check_path

def main():
    parser = argparse.ArgumentParser(prog="PREFS", usage="Command Line Tool for PREFS Python library")
    subparsers = parser.add_subparsers(help="commands", dest="command")

    bundle_parser = subparsers.add_parser(
        'bundle', 
        help='Bundle a .prefs to a .py resource file that you can access adding ":/" to the path. Read more at https://patitotective.github.io/PREFS/.', 
        usage="Given the path of a PREFS file, bundle it into a PREFS resource file..",     
    )

    bundle_parser.add_argument("path", type=str, help='The path of the PREFS file to bundle')
    bundle_parser.add_argument("-o", "--output", type=str, help='The path of the output file', default=None)
    bundle_parser.add_argument("-a", "--alias", type=str, help='The alias name to be referenced.', default=None)

    read_prefs_parser = subparsers.add_parser(
        'read_prefs_file', 
        help="Read a PREFS file and print it's value", 
        usage="Given the path of a PREFS file, print it's value."
    )
    
    read_prefs_parser.add_argument("path", type=str, help='The path of the .prefs file to bundle')

    convert_to_prefs_parser = subparsers.add_parser(
        "convert_to_prefs", 
        help="Convert a Python dictionary into a PREFS format.", 
        usage="Given a Python dictionary and some optional arguments converts that dictionary into PREFS format."
        )
    
    convert_to_prefs_parser.add_argument("prefs", type=str, help="The prefs (dictionary) to convert as a string")
    convert_to_prefs_parser.add_argument("-o", "--output", type=str, help='Output path to write the result, if no output path specified, print it.', default=None)

    args = parser.parse_args()

    if args.command is None:
        parser.parse_args(["-h"])

    elif args.command == "bundle":
        path = args.path
        output_path = args.output if args.output is not None else args.output
        alias = args.alias if args.alias is not None else args.alias

        if output_path is None:
            output_path = f"{path.split('.')[0]}_resource.py"
        if alias is None:
            alias = os.path.basename(path)

        bundle_prefs_file(path=path, output=output_path, alias=alias)

    elif args.command == "read_prefs_file":
        print(read_prefs_file(args.path))

    elif args.command == "convert_to_prefs":
        if args.output is None:
            print(convert_to_prefs(prefs=ast.literal_eval(args.prefs)))
            return
            
        convert_to_prefs(prefs=ast.literal_eval(args.prefs), output=args.output)

if __name__ == '__main__':
    main()
