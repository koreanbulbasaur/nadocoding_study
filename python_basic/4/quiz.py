url = "http://naver.com"
rule_1 = url.replace("http://", "")
rule_2 = rule_1[:rule_1.index(".")]

password = rule_2[:3] + str(len(rule_2)) + str(rule_2.count("e")) + "!"
print(f"생성된 비밀번호 : {password}")
