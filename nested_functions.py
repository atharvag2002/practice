
def outer(suffix):
    def inner(prefix):
        return prefix + suffix
    return inner

# f = outer("c")
# print(f("hello"))

suffix_list = ["c", "java", "py"]
prefix_list = ["hii","hello","supp"]

for i in suffix_list:
    i = outer(" "+i)
    for j in prefix_list:
        print(i(j))
