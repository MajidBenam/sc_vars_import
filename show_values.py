show_values_general ={
    "peak_years": """
    
    """,

}

def show_values_general(is_range_or_choice, list_of_vars):
    if is_range_or_choice == "IS_RANGE" and len(list_of_vars) == 2:
        _from = list_of_vars[0]
        _to = list_of_vars[1]
        return f"""
        if self.{_from} and self.{_to} and self.{_to} == self.{_from}:
            return self.{_from}
        elif self.{_from} and self.{_to}:
            return f"[{{self.{_from}:,}} to {{self.{_to}:,}}]"
        elif self.{_from}:
            return f"[{{self.{_from}:,}}"
        elif self.{_to}:
            return f"[{{self.{_to}:,}}"
        else:
            return " - "
        """
    elif is_range_or_choice == "IS_NOT_RANGE" and len(list_of_vars) == 1:
        value = list_of_vars[0]
        return f"""
        if self.{value}:
            return self.{value}
        else:
            return " - "
        """
    elif is_range_or_choice == "IS_CHOICE" and len(list_of_vars) == 1:
        value = list_of_vars[0]
        return f"""
        if self.{value}:
            return self.get_{value}_display()
        else:
            return " - "
        """