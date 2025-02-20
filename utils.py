import csv
from typing import List, Type
from pydantic import BaseModel
from io import StringIO


def write_pydantic_to_csv(objects: List[BaseModel]) -> StringIO:
    if not objects:
        raise ValueError("The list of objects is empty.")
    model_class: Type[BaseModel] = objects[0].__class__
    try:
        field_names = list(
            model_class.model_json_schema()["properties"].keys()
        )  # Pydantic v2
    except AttributeError:
        field_names = list(model_class.schema()["properties"].keys())  # Pydantic v1

    computed_fields = [
        name
        for name in dir(model_class)
        if isinstance(getattr(model_class, name, None), property)
        and name not in ["__fields_set__", "model_extra", "model_fields_set"] 
    ]
    field_names.extend(computed_fields)
    output = StringIO()

    writer = csv.DictWriter(output, fieldnames=field_names)
    writer.writeheader()

    for obj in objects:
        writer.writerow(
            obj.model_dump() if hasattr(obj, "model_dump") else obj.dict()
        ) 

    output.seek(0)
    return output


if __name__ == "__main__":
    class Person(BaseModel):
        name: str
        age: int

    data = [Person(name="Alice", age=30), Person(name="Bob", age=25)]
    csv_file = write_pydantic_to_csv(data)
    with open("test.csv", "w", newline="") as f:
        f.write(csv_file.getvalue())
