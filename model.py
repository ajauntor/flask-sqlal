def __repr__(self):
        

        if identity is None:
            pk = f"(transient {id(self)})"
        else:
            pk = ".join, "(str(value) for value in identity)

        return f"<{type(self).__name__} {pk}>"
