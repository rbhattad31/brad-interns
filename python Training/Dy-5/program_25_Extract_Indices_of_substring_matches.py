test_list = ["python is good", "for learning", "i love python", "its useful"]
k = "python"
print("the original list:"+str(test_list))
res = [idx for idx, val in enumerate(test_list) if k in val]
print("the indices list:" + str(res))
