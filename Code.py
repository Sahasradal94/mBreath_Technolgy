import csv
import xml.etree.cElementTree as ET

#code for data/apnea file :

tree=ET.parse('apnea.xml')
root=tree.getroot()
xml_data_to_csv =open('mesa-sleep-0001-profusion.xml.csv','w')
list_head=[]
Csv_writer=csv.writer(xml_data_to_csv)
count=0
for element in root.findall('ScoredEvents'):
    for child in element.findall('ScoredEvent'):
        List_nodes=[]
        #get head by tag
        if count==0:
           name=child.find('Name').tag
           list_head.append(name)
           start = child.find('Start').tag
           list_head.append(start)
           duration = child.find('Duration').tag
           list_head.append(duration)
           input = child.find('Input').tag
           list_head.append(input)
           Csv_writer.writerow(list_head)
           count = +1

        #get child node of ScoredEvent
        name = child.find('Name').text
        if name=='Hypopnea':
           List_nodes.append(name)
           start = child.find('Start').text
           List_nodes.append(start)
           duration = child.find('Duration').text
           List_nodes.append(duration)
           input = child.find('Input').text
           List_nodes.append(input)
           # write List_node to csv
           Csv_writer.writerow(List_nodes)

xml_data_to_csv.close()





#Code for sleep stage file:

tree2=ET.parse('mesa-sleep-0001-nsrr.xml')
root2=tree2.getroot()
xml_data_to_csv=open('mesa-sleep.xml.csv','w')

list_head2=[]
Csv_writer=csv.writer(xml_data_to_csv)
count2=0

for  element2 in root2.findall('ScoredEvents'):
     for child2 in element2.findall('ScoredEvent'):
         List_nodes2=[]
         #get head by tag
         if count2==0:
            duration = child2.find('Duration').tag
            list_head2.append(duration)
            stages=child2.find('EventConcept').tag
            list_head2.append(stages)
            start=child2.find('Start').tag
            list_head2.append(start)
            Type = child2.find('EventType').tag
            list_head2.append(Type)
            Csv_writer.writerow(list_head2)
            count2=+1

         #get child node of ScoredEvent
         Type = child2.find('EventType').text
         if Type=='Stages|Stages':
            duration = child2.find('Duration').text
            List_nodes2.append(duration)
            stages = child2.find('EventConcept').text
            List_nodes2.append(stages)
            start = child2.find('Start').text
            List_nodes2.append(start)
            List_nodes2.append(Type)
            Csv_writer.writerow(List_nodes2)

xml_data_to_csv.close()
