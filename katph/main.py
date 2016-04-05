from scrapy import cmdline
import os

class Utils:
    ## get input ##
    filename = "items.json"

    def prepare(self):
        ## delete only if file exists ##
        if os.path.exists(self.filename):
            os.remove(self.filename)
        else:
            print("Sorry, I can not remove %s file." % self.filename)

    def execute(self,module):
        command = ("scrapy crawl %s -o items.json" % module)
        # command = ("scrapy crawl selenium  -a category=dublin -o items.json -t json")
        cmdline.execute(command.split())

# scrapy crawl apple -o items.json
def main():
    utils = Utils()

    utils.prepare()
    # utils.execute("katph")
    # utils.execute("dmoz")
    # utils.execute("stackoverflow")

    utils.execute("itunes")
    # utils.execute("stack")
    # utils.execute("apple")
    # utils.execute("selenium")
    # utils.execute("dribbble");


if __name__ == '__main__':
    main()



