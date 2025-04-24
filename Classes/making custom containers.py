class TagCloud:
    # a dictionary called tags
    def __init__(self):
        self.tags = {}

    # the add function, default value 0, lower case
    def add(self, tag):
        #
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
