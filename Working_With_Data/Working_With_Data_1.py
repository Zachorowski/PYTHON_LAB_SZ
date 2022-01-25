import xml.sax

class ChaosHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ""
        self.name = ""
        self.legion = ""
        self.allegiance = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "name":
            print("----Warlord----")


    def endElement(self,tag):
        if self.CurrentData == "name":
            print("Name: ", self.name)
        elif self.CurrentData == "legion":
            print("Legion: ", self.legion)
        elif self.CurrentData == "allegiance":
            print("Allegiance: ", self.allegiance)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "legion":
            self.legion = content
        elif self.CurrentData == "allegiance":
            self.allegiance = content


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = ChaosHandler()
parser.setContentHandler(Handler)
parser.parse("Chaos.xml")
