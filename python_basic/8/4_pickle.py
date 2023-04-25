import pickle
profile_file = open(
    r"C:\Private_Projects\nadocoding\python_basic\8\profile.pickle", "wb")
profile = {"이름": "하도영", "나이": 63, "취미": ["오토바이", "당구", "골프"]}

# profile 에 있는 정보를 file 에 저장
pickle.dump(profile, profile_file)
profile_file.close()

profile_file = open(
    r"C:\Private_Projects\nadocoding\python_basic\8\profile.pickle", "rb")
# file 에 있는 정보를 profile 에 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
