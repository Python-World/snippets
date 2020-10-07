# Print type object in dict
*tags:* **type, dict forloop keys, object**


**Snippet**
```python




def validate_type_object_in_dict(data_dict):
    """
    First get the key values
    Second use isinstace(value, type) to detect if is str, bool,int,float
    Note that bool is a subclass of int then validate this always first
    """
    for key in data_dict.keys():
        if isinstance(data_dict[key],str):
            print(f"The data {data_dict[key]}  is a string value")
        elif isinstance(data_dict[key], bool):
            print(f"The data {data_dict[key]}  is a boolean value")
        elif isinstance(data_dict[key], int):
            print(f"The data {data_dict[key]}  is  a integer value")
        elif isinstance(data_dict[key], float):
            print(f"The data {data_dict[key]}  is  a float value")
    
data = {

    "name":"jairo",
    "age":20,
    "enable":True,
    "distance":5.5

}

validate_type_object_in_dict(data)

```