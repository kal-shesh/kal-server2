import json
import os

pdfsPath = "C:\\Users\\lavi\\Desktop\\Hackaton\\server\\kal-server2\\PDF\\Templates\\"

file = open('data.json','w')
json.dump({"Soldiers Details": {
                "Personal Info": {
                    "ID": 4408783,
                    "Rank": "Lieutenant",
                    "Family Name": "occaec",
                    "First Name": "sunt ut elit oc",
                    "Corps": "minim laborum i",
                    "Unit": "cupidatat nul",
                    "Citizenship": "sunt eiusmod ea Duis",
                    "Family Status": "incididunt ullamco sed ut",
                    "education": "quis anim tem",
                    "Medical Profile": 53521427,
                    "Is Permanent": True,
                    "Medical Profile set date": "2454-12-21T08:06:40.054Z",
                    "Job": "commo",
                    "Main Profession": "vel",
                    "Main Profession Num": 25628665,
                    "Main Profession Type": "ea dese",
                    "Permanent Service Start": "4281-02-22T14:36:28.908Z",
                    "Start Of Next Permanent Service": "1988-10-22T02:15:51.298Z",
                    "Rank Before Position": "Corporal",
                    "End of Current Commitment": "4890-03-13T00:41:00.890Z",
                    "Date Of Birth": "2881-07-20T03:08:29.840Z"
}}},file)
file.close()
pdfFromPath = pdfsPath + 'form.pdf'
pdfOutPath = pdfsPath + 'out.pdf'
cmd = pdfsPath+'PdfFiller.exe '+pdfFromPath +' ' +pdfOutPath + ' ' + 'data.json'
os.system(cmd)


