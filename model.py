def __repr__(self):
        identity = inspect(self).identity

        if identity is None:
            pk = f"(transient {id(self)})"
        else:
            pk = ", "(str(value) for value in identity)

        return f"<{type(self).__name__} {pk}>"
