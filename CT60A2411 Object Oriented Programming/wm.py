import os
import argparse
import zipfile
import subprocess

def create_week_structure(args):
    week_dir = f"week{args.week}"

    if os.path.exists(week_dir) and (not args.force and not args.purge):
        overwrite = input(f"The directory '{week_dir}' already exists. Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Operation cancelled.")
            return
    
    if os.path.exists(week_dir) and args.purge:
        print(f"Removing existing directory '{week_dir}'")
        os.removedirs(week_dir)

    main_dir = os.path.join(week_dir, "src", "main", "java", "main")
    os.makedirs(main_dir, exist_ok=True)

    if args.app:
        app_path = os.path.join(main_dir, "App.java")
        if not os.path.exists(app_path) or args.force:
            with open(app_path, "w") as f:
                f.write("""package main;

public class App {
    public static void main(String[] args) {
        // Code here
    }
}
""")

    for other_class in args.classes:
        class_path = os.path.join(main_dir, f"{other_class}.java")
        if not os.path.exists(class_path) or args.force:
            with open(class_path, "w") as f:
                f.write(f"""package main;

public class {other_class} {{
    // Code here
}}
""")

def zip_week(args):
    output_file = f"week{args.week}.zip"

    if os.path.exists(output_file) and not args.force:
        overwrite = input(f"The file '{output_file}' already exists. Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Operation cancelled.")
            return

    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(f"week{args.week}"):
            for file in files:
                file_path = os.path.join(root, file)
                z.write(file_path, os.path.relpath(file_path, f"week{args.week}"))

def compile_java(args):
    week_dir = f"week{args.week}"
    src_dir = os.path.join(week_dir, "src", "main", "java")
    bin_dir = os.path.join("run", week_dir)

    os.makedirs(bin_dir, exist_ok=True)

    java_files = []
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                java_files.append(file_path)

    if java_files:
        try:
            subprocess.run(["javac", "-d", bin_dir] + java_files, check=True)
            print(f"Compiled Java files to {bin_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Error during compilation: {e}")
            return

    if args.execute:
        try:
            subprocess.run(["java", "-cp", bin_dir, args.main_class], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing main class: {e}")

parser = argparse.ArgumentParser(description="Utility script for week-based operations.")
subparsers = parser.add_subparsers(dest="command", required=True)

parser_create = subparsers.add_parser('create', help='Create week structure')
parser_create.add_argument('week', type=int, help='Week number')
parser_create.add_argument('-f', '--force', action='store_true', help='Force overwrite existing files')
parser_create.add_argument('-a', '--app', action='store_true', help='Create App.java')
parser_create.add_argument('-c', '--classes', nargs='*', default=[], help='List of additional classes to create')
parser_create.add_argument('-p', '--purge', action='store_true', help='Purge existing week directory')
parser_create.set_defaults(func=create_week_structure)

parser_zip = subparsers.add_parser('zip', help='Zip week directory')
parser_zip.add_argument('week', type=int, help='Week number')
parser_zip.add_argument('-f', '--force', action='store_true', help='Force overwrite existing zip file')
parser_zip.set_defaults(func=zip_week)

parser_compile = subparsers.add_parser('compile', help='Compile Java code')
parser_compile.add_argument('week', type=int, help='Week number')
parser_compile.add_argument('-e', '--execute', action='store_true', help='Execute the main class after compilation')
parser_compile.add_argument('-m', '--main-class', type=str, default="main.App", help='Main class to execute')
parser_compile.set_defaults(func=compile_java)

args = parser.parse_args()
args.func(args)
