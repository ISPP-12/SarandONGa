def get_person_str(name, surname, else_field):
    if surname != None and name != None:
        if surname.strip() != "" and name.strip() != "":
            return f"{surname}, {name}"
        elif surname.strip() != "" and name.strip() == "":
            return f"{surname}"
        elif surname.strip() == "" and name.strip() != "":
            return f"{name}"
        else:
            return else_field
    elif surname != None and name == None:
        if surname.strip() != "":
            return f"{surname}"
        else:
            return else_field
    elif surname == None and name != None:
            if name.strip() != "":
                return f"{name}"
            else:
                return else_field
    else:
        return else_field