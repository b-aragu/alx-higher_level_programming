#!/usr/bin/python3
# models.py

"""Defines a base class for all models in our hbnb clone"""
import json
import csv


class Base:
    """Base class for all models in the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_obj to file"""
        filename = cls.__name__+".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns a list of json representation"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__+".json"
        try:
            with open(filename, 'r') as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes list_objs to a csv file """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes csv file to list of instances """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = []
                for row in reader:
                    for k, v in row.items():
                        row[k] = int(v)
                    list_dicts.append(row)
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draws the Rectangles and Squares """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")
        turt.color("#ffffff")
        turt.penup()
        for rect in list_rectangles:
            turt.goto(rect.x, rect.y)
            turt.pendown()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
        turtle.Screen().exitonclick()
