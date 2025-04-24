class TagCloud:

    # a dictionary called tags
    def __init__(self):
        # prefixing with two __ serves as a warning not to touch
        self.__tags = {}

    # the add function, default value 0, lower case
    def add(self, tag):
        #
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
print(cloud.__dict__)
print(cloud._TagCloud__tags)
