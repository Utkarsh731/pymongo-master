import re
text="as"
i={"email":"af","firstName":"adgd","lastName":"As"}
if re.search(text,i["email"],re.IGNORECASE) or re.search(text,i["firstName"],re.IGNORECASE) or re.search(text,i["lastName"],re.IGNORECASE):
              print("true")