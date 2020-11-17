import datetime, math

directory = "Course_files\\"
present_date = datetime.datetime.now()
date_string = present_date.strftime("%b") + "_" + str(int(present_date.strftime("%d")))
filename = directory + date_string + "_Courses.txt"

course_file = open(filename, "r", encoding="utf-8")
filedata = course_file.read().split("\n")

posts = math.ceil((len(filedata))/60)
#type_of_post = input("Choose the post platform from below:\n1 for Whatsapp.\n2 for Telegram.\nEnter your choice?")

whatsapp_post_start = "*FREE KNOWLEDGE SOCIETY*\n\n*_Courses for today:_*\n\n\n"
telegram_post_start = "Courses for today:\n\n\n"
whatsapp_post_end = "*Thank you for your Support!*\n*_Join our TELEGRAM channel for more courses:_*\n*https://t.me/freeknowledgesociety/*"
telegram_post_end = "Thank you for your Support!\nJoin our TELEGRAM channel for more courses:\nhttps://t.me/freeknowledgesociety/"

whatsapp_filename = directory + "whatsapp_" + date_string + "_post_file.txt"
telegram_filename = directory + "telegram_" + date_string + "_post_file.txt"
whatsapp_file = open(whatsapp_filename, "w", encoding="utf-8")
telegram_file = open(telegram_filename, "w", encoding="utf-8")

for i in range(1, posts+1):
    print("Round " + str(i))
    whatsapp_file.write(whatsapp_post_start)
    telegram_file.write(telegram_post_start)
    print("Starting added!")
    for j in range(60*(i-1), 60*i):
        whatsapp_file.write(filedata[j]+"\n")
        telegram_file.write(filedata[j]+"\n")
    print("Middle Part added!")
    whatsapp_file.write(whatsapp_post_end+"\n\n\n\n\n\n\n\n\n\n")
    telegram_file.write(telegram_post_end+"\n\n\n\n\n\n\n\n\n\n")
    print("Ending added!")
    print("Round " + str(i) + "done!!!\n\n")

whatsapp_file.close()
telegram_file.close()