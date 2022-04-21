import os

# Author: c0nvict
# Github: https://github.com/c0nvict/BetterDesign

os.system("")

def center(text: str) -> str:
    if len(text.splitlines()) >= 2:
        return centertypes.multiple_line_center(text)
    else:
        return centertypes.single_line_center(text)

def table(values: dict, **kwargs) -> str:
    if "limit" in kwargs:
        if isinstance(kwargs["limit"], int):
            return tablefunctions.limited_table(values, kwargs["limit"])
        else:
            return tablefunctions.table(values)
    else:
        return tablefunctions.table(values)

def section(**kwargs) -> str:
    if "length" in kwargs:
        if isinstance(kwargs["length"], int):
            return design_methods.limited_section(kwargs["limit"])
        else:
            return design_methods.unlimited_section()
    else:
        return design_methods.unlimited_section()

class centertypes:

    @staticmethod
    def single_line_center(text: str) -> str:
        total_width = os.get_terminal_size().columns
        text_width = len(text)
        side = round((total_width - text_width) / 2)
        centerspace = " " * side
        return f"{centerspace}{text}"

    @staticmethod
    def multiple_line_center(text: str) -> str:
        completed_string = ""
        total_width = os.get_terminal_size().columns
        for key, line in enumerate(text.splitlines()):
            text_width = len(line)
            side = round((total_width - text_width) / 2)
            centerspace = " " * side
            if (key + 1) == len(text.splitlines()):
                new_line = f"{centerspace}{line}"
            else:
                new_line = f"{centerspace}{line}\n"
            completed_string += new_line
        return completed_string

class tablefunctions:

    @staticmethod
    def limited_table(values: dict, limit) -> str:
        mrgl = limit + 2
        mrg = "═" * mrgl
        table = f"╔{mrg}╦{mrg}╗\n"
        for key, value in values.items():
            if len(value) > limit:
                fixed_value = value[:limit]
            else:
                left = (limit - len(value))
                fixed_value = value + " " * left
            if len(key) > limit:
                fixed_key = key[:limit]
            else:
                left = (limit - len(key))
                fixed_key = key + " " * left
            table += f"║ {fixed_key} ║ {fixed_value} ║\n"
        table += f"╚{mrg}╩{mrg}╝"
        return table

    @staticmethod
    def table(values: dict):
        largest_key = max(len(d) for d in values)
        largest_value = max(len(d) for x,d in values.items())
        max_ = largest_value if largest_value > largest_key else largest_key
        brdl = max_ + 2
        mrg = "═" * brdl
        table = f"╔{mrg}╦{mrg}╗\n"
        for key, value in values.items():
            if len(value) > max_:
                fixed_value = value[:max_]
            else:
                left = (max_ - len(value))
                fixed_value = value + " " * left
            if len(key) > max_:
                fixed_key = key[:max_]
            else:
                left = (max_ - len(key))
                fixed_key = key + " " * left
            table += f"║ {fixed_key} ║ {fixed_value} ║\n"
        table += f"╚{mrg}╩{mrg}╝"
        return table

class design_methods:

    @staticmethod
    def limited_section(limit: int) -> str:
        line = "-" * limit
        return line
    
    @staticmethod
    def unlimited_section() -> str:
        line = "-" * os.get_terminal_size().columns
        return line
