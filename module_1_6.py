my_dict = {"Name": 'Maikl',"Age": 24,"Weight": 81, "Men": True}
print(my_dict)
print(my_dict.get("Age"), '\n', my_dict.get("Height"))
my_dict.update({"Height": 190,
                "Job_Title": 'programist'})
a = my_dict.pop("Name")
print(a)
print(my_dict)

my_set = {True,1,4,7,"65",5,1,23.0,5,4,8,5,2,6,5,4,1.0,2,3,4}
print(my_set)
my_set.update({1000,"prosto"})
my_set.remove(5)
print(my_set)
