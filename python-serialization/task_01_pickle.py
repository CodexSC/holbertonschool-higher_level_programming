#!/usr/bin/python3
import pickle


def save_to_json_file(my_obj, filename):
    with open(filename, "wb") as f:
        pickle.dump(my_obj, f)

    return


def load_from_json_file(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

    return

if __name__ == "__main__":
    my_list = [1, 2, 3]
    save_to_json_file(my_list, "my_list.json")
    print(load_from_json_file("my_list.json"))

    my_dict = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    save_to_json_file(my_dict, "my_dict.json")
    print(load_from_json_file("my_dict.json"))

    my_list = [1, 2, 3]
    save_to_json_file(my_list, "my_list.json")
    print(load_from_json_file("my_list.json"))
