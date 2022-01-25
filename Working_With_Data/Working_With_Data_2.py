from xml.dom.minidom import parse
import xml.dom.minidom


DOMTree = xml.dom.minidom.parse("Chaos.xml")
collection = DOMTree.documentElement
warlords = collection.getElementsByTagName("warlord")

for warlord in warlords:
   print ("----Warlord----")
   name = warlord.getElementsByTagName('name')[0]
   print ("Name: " , name.childNodes[0].data)
   legion = warlord.getElementsByTagName('legion')[0]
   print ("Legion: " , legion.childNodes[0].data)
   allegiance = warlord.getElementsByTagName('allegiance')[0]
   print ("Allegiance: " , allegiance.childNodes[0].data)
