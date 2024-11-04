# Let's create definitions that people can change easily
soundInclude = "../pl_sound_data.sbdl"
bgmPrefix = "SEQ_"
pvPrefix = "SEQ_PV"
mePrefix = "SEQ_ME"
sePrefix = "SEQ_SE"

outputDir = "../docs/"

# Variable Inits
bgmNames = []
bgmIds = []

pvNames = []
pvIds = []

meNames = []
meIds = []

seNames = []
seIds = []

si = open(soundInclude) # include SoundFile Database

print("Detecting useful SEQs from SBDL")
while True:
        line = si.readline()
        line = line.split()
        try:
                elif line[1].startswith(pvPrefix) == True:
                    pvNames.append(line[1])
                    pvIds.append(line[2])
                elif line[1].startswith(sePrefix) == True:
                    seNames.append(line[1])
                    seIds.append(line[2])
                elif line[1].startswith(mePrefix) == True:
                    meNames.append(line[1])
                    meIds.append(line[2])
                else:
                    bgmNames.append(line[1])
                    bgmIds.append(line[2])
        except IndexError:
                print("\nFinished detection!")
                break
si.close()

a = 0
out = open(outputDir + "list/bgm_list.html", 'w')

out.write("<html>\n<head><link rel='stylesheet' href='./main.css'></head><body>\n<table>\n<tr><th>ID</th><th>Filename</th></tr>\n")

print(len(bgmIds))

while a != len(bgmIds):
                out.write("<tr><td>" + bgmIds[a] + "</td><td>" + bgmNames[a] + "</td></tr>\n")
                print("Output: " + bgmIds[a] + " - " + bgmNames[a])
                a = a+1

out.write("</table>\n</body>\n</html>")

out.close()

print("Output BGM")

a = 0

out = open(outputDir + "list/pv_list.html", 'w')

out.write("<html>\n<head><link rel='stylesheet' href='./main.css'></head><body>\n<table>\n<tr><th>ID</th><th>Filename</th></tr>\n")

print(len(pvIds))

while a != len(pvIds):
                out.write("<tr><td>" + pvIds[a] + "</td><td>" + pvNames[a] + "</td></tr>\n")
                print("Output: " + pvIds[a] + " - " + pvNames[a])
                a = a+1

out.write("</table>\n</body>\n</html>")

out.close()

print("Output PV")

a = 0

out = open(outputDir + "list/se_list.html", 'w')

out.write("<html>\n<head><link rel='stylesheet' href='./main.css'></head><body>\n<table>\n<tr><th>ID</th><th>Filename</th></tr>\n")

print(len(seIds))

while a != len(seIds):
                out.write("<tr><td>" + seIds[a] + "</td><td>" + seNames[a] + "</td></tr>\n")
                print("Output: " + seIds[a] + " - " + seNames[a])
                a = a+1

out.write("</table>\n</body>\n</html>")

out.close()

print("Output SE")

a = 0


out = open(outputDir + "list/me_list.html", 'w')

out.write("<html>\n<head><link rel='stylesheet' href='./main.css'></head><body>\n<table>\n<tr><th>ID</th><th>Filename</th></tr>\n")

print(len(meIds))

while a != len(meIds):
                out.write("<tr><td>" + meIds[a] + "</td><td>" + meNames[a] + "</td></tr>\n")
                print("Output: " + meIds[a] + " - " + meNames[a])
                a = a+1

out.write("</table>\n</body>\n</html>")

out.close()

print("Output ME")

print("Finished outputting Sound List")
