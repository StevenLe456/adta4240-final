import os

id2roi = {1: "F7", 2: "F3", 3: "F4", 4: "F8", 5: "T3", 6: "C3", 7: "Cz", 8: "C4", 9: "T4", 10: "T5", 11: "P3", 12: "Pz", 13: "P4", 14: "T6", 15: "O1", 16: "O2"}

with open("channels.csv", "w") as csv:
    csv.write("Channel ID,BrainRegion\n")
    for k, v in id2roi.items():
        csv.write(f"{k},{v}\n")

patient = open("patient.csv", "w")
sample = open("samples.csv", "w")

patient.write("PatientID,PatientCode,Diagnosis\n")
sample.write("SampleID,PatientID,ChannelID,Time,Amplitude\n")

pid = 0
sid = 0

for root, dir, files in os.walk("data/"):
    for f in files:
        print(f"Working on patient {pid + 1}")
        patient_code = f[0:f.index(".eea")]
        diagnosis = "nkd" if root.find("norm") != -1 else "scz"
        patient.write(f"{pid},{patient_code},{diagnosis}\n")
        p = os.path.join(root, f)
        with open(p, "r") as eeg:
            raw_str = eeg.read()
            temp_list = [float(num) for num in raw_str.strip().split("\n")]
            for c, n in enumerate(temp_list):
                sample.write(f"{sid},{pid},{(c // 7680) + 1},{(c % 7680) + 1},{n}\n")
                sid += 1
        pid += 1
        print(f"Completed patient {pid}")

patient.close()
sample.close()