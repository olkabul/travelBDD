def get_elm_by_text(exp_text, elems):
    selected_elem = ""
    for elem in elems:
        if exp_text in elem.text:
            selected_elem = elem
    return selected_elem

def get_elem_by_name(name, elems):
    selected_elem = ""
    for elem in elems:
        if elem.name == name:
            selected_elem = elem
    return selected_elem