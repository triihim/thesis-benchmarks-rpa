import pandas as pd
import matplotlib.pyplot as plt

# browsers = ["chrome", "firefox", "edge"]
# frameworks = ["react", "angular", "vue", "blazor_aot", "blazor_noaot"]
# tests = ["Render", "Update", "Remove"]

browsers = ["chrome", "firefox", "edge"]
frameworks = ["blazor_noaot"]
tests = ["Render", "Update", "Remove"]

cols = ["Processor total (J)", "Processor mean (W)", "DRAM total (J)", "DRAM mean (W)", "Total time (s)"]

#csv_folder_path = "../rpa/csv"
#csv_folder_path = "../rpa/csv_ArrayMethods"
csv_folder_path = "../rpa/csv_forloop"

for b in browsers:
  for f in frameworks:
    for t in tests:
      test_id = f"{b}_{f}_{t}"
      totals = pd.DataFrame(columns=cols)
      for i in range(1, 11):
        csv_path = f"{csv_folder_path}/{b}_{f}_{t}_aggregated_{i}.csv"
        data = pd.read_csv(csv_path)
        totals = pd.concat([totals, data])
      summarized = pd.DataFrame(totals.mean()).transpose()
      summarized.to_csv(f"{csv_folder_path}/{test_id}_summary.csv")
