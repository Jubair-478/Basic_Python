# info={
#     "name":"sajid",
#     "subject":{
#         "phy":97,
#         "chem":98,
#         "math":95
#     }
# }

# info["name"]=["rahat"]
# print(info)
# print(list(info.items()))
# print(list(info.keys()))
# print(info.values())

# print(info["name2"])    ---- error
# print(info.get("name2")) ------- None

# info.update({"bio":98,"math":98,"bangla":500})
# new_info={"bio":98,"math":98,"bangla":500}
# info.update(new_info)

# print(info)

        #   SET

# collection={1,1,1,1,1,222,2,2,23,3,3,"hello","hello","hi","hi"}
# print(collection)
# print(len(collection))


# Store following word meaning in python dictionary.

# Dictionary={
#         "table":["a piece of furniture,list of facts & figures"],
#         "cat":"a small animal"
#         }

# print(Dictionary)


# You are given a list of subjects for students.Assume one classroom is required for 1 subject.How many classrooms are needed by all students.

# subjects={"python","java","c++","python","javascript","java","python","java","c++","c"}

# Classroom=len(subjects)

# print("Classroom need :",Classroom)


# WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary & add one by one.USe subject name as key & marks value.

math=90
bangla=80
english=90

marks={}

new_dic = {"math":90,"bangla":80,"english":90}

marks.update(new_dic)

print(marks)







