class IO:
    supportedList = ["console", "file"]

    def read(src):
        if src not in IO.supportedList:
            print("Not supported")
        else:
            print("Read from", src)


print(IO.supportedList)
IO.read("XXX")