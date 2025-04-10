#! /usr/bin/env python3

from argparse import ArgumentParser
from file_io import FileInputOutput
from zoo import Zoo
from animal import Animal, Bird, Cat, Dog, Reptile

def list_animals(args):
    file = FileInputOutput(args.file)
    zoo = Zoo()
    file.load_data(zoo)
    zoo.list_animals()

def add_animal(args):
    file = FileInputOutput(args.file)
    name = args.name
    type = args.type
    zoo = Zoo()
    animal = None
    file.load_data(zoo)
    match type:
        case 'bird':
            animal = Bird(name)
        case 'cat':
            animal = Cat(name)
        case 'dog':
            animal = Dog(name)
        case 'reptile':
            animal = Reptile(name)
        case _:
            animal = Animal(name, type)
    zoo.add_animal(animal)
    file.save_data(zoo)

def remove_animal(args):
    file = FileInputOutput(args.file)
    name = args.name
    zoo = Zoo()
    file.load_data(zoo)
    if name:
        zoo.remove_animal(name)
    file.save_data(zoo)

if __name__ == "__main__":
    parser = ArgumentParser(
        prog='Zoo Manager Command-Line Utility',
        description='Manages zoo files containing animal data'
    )
    parser.add_argument('-f', '--file', help='Name of the zoo file to modify.', default='zoo_data.txt')
    subparsers = parser.add_subparsers(help='SUBCOMMANDS')

    list_parser = subparsers.add_parser('list', help='Lists all animals in the zoo file.')
    list_parser.set_defaults(func=list_animals)

    add_parser = subparsers.add_parser('add', help='Adds a new animal to the zoo file.')
    add_parser.add_argument('name', help='Name of the individual animal to add.')
    add_parser.add_argument('type', help='Type of animal to add.', choices=['bird','cat','dog','reptile'])
    add_parser.set_defaults(func=add_animal)

    remove_parser = subparsers.add_parser('remove', help='Remove an animal by name.')
    remove_parser.add_argument('name', help='Name of the individual animal to remove.')
    remove_parser.set_defaults(func=remove_animal)

    arguments = parser.parse_args()

    arguments.func(arguments)
else:
    print("It looks like you've imported the executable script from elsewhere in the codebase!  Please ensure you only call this script from the command line.")