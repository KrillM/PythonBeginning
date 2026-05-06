import pickle

# profile_file = open("profile.pickle", "wb")
# profile = {"Name": "Krille", "Age": 25, "Hobbys": ["Football", "Reading", "Coding"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # 파일에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()