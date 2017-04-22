
import csv, json

csvfile = open('test.csv', 'r')
csvfile2 = open('labresults-codes.csv', 'r')

reader = csv.reader(csvfile)
reader2 = csv.reader(csvfile2)

data = list(reader)
data2 = list(reader2)

my_dict = {"patients":[]}

for i in range(1,len(data)):
        for l in range(len(data2)):
            if data[i][30] in data2[l]:
                code = data2[l][1]
                label = data2[l][2]
        d1 = [{"code":code,"label":label,"value":''.join([s for s in data[i] if (data[i][30]+"~") in s]),"unit":data[i][31],"lower":data[i][32],
        "upper":data[i][33]}]
        for j in range(i+1,len(data)):
            if data[i][1] == data[j][1]:
                for l in range(len(data2)):
                    if data[j][30] in data2[l]:
                        code = data2[l][1]
                        label = data2[l][2]
                d1.append({"code":code,"label":label,"value":''.join([s for s in data[j] if (data[j][30] + "~") in s]),"unit":data[j][31],"lower":data[j][32],
                "upper":data[j][33]})
        d2 = {"name":data[i][3],"code":data[i][1]}
        d3 = [{"timestamp":data[i][2],"profile":d2,"panel":d1}]
        for j in range(i+1,len(data)):
            if data[i][0] == data[j][0]:
                for l in range(len(data2)):
                    if data[j][30] in data2[l]:
                        code = data2[l][1]
                        label = data2[l][2]
                d1_1 = [{"code":code,"label":label,"value":''.join([s for s in data[j] if (data[j][30] + "~") in s]),"unit":data[j][31],"lower":data[j][32],
                "upper":data[j][33]}]
                for k in range(j+1,len(data)):
                    if data[j][1] == data[k][1]:
                        for l in range(len(data2)):
                            if data[k][30] in data2[l]:
                                code = data2[l][1]
                                label = data2[l][2]
                        d1_1.append({"code":code,"label":label,"value":''.join([s for s in data[k] if (data[k][30] + "~") in s]),"unit":data[k][31],"lower":data[k][32],
                        "upper":data[k][33]})
                d2_1 = {"name":data[j][3],"code":data[j][1]}
                d3_1 = [{"timestamp":data[j][2],"profile":d2_1,"panel":d1_1}]
                d3.append(d3_1)
        d4 = {"id":data[i][0],"firstName":"","lastName":"","dob":"","lab_results":d3}
        my_dict["patients"].append(d4)

my_dict_dumped = json.dumps(my_dict)
my_dict_loaded = json.loads(my_dict_dumped)

print(json.dumps(my_dict_loaded, indent = 2))
