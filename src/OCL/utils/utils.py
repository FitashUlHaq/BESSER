def readAndPopulateCD(environment,cd):
    pass
def populateOD(environment,od):
    OD_file_parts = od.split("\n")

    for i in range(len(OD_file_parts)):
        if "@" in OD_file_parts[i]:
            continue;
        if "Object " in OD_file_parts[i]:
            objName = OD_file_parts[i].split(" ")[1]
            environment.add_element(objName)
            # print(objName)
            for j in range (i+1,len(OD_file_parts)):
                if "}" in OD_file_parts[j]: #ending one object
                    break
                if ":" not in OD_file_parts[j]: # empty line
                    continue
                attributeAndVal = OD_file_parts[j]
                attributeAndVal = attributeAndVal.replace("{","")
                attributeAndValParts = attributeAndVal.split(":")
                # print(attributeAndValParts)
                attribute = attributeAndValParts[0]
                value = attributeAndValParts [1]
                # print(attribute)
                environment.update_element(objName,attribute,value)
            i = j
