class Meta:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.attr = 100
        return obj


