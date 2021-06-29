class BlueprintMeta(type):
    def __new__(mcs, class_name, bases, class_dict):
        return type.__new__(mcs, class_name, bases, class_dict)
