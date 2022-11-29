import sys
import pandas as pd

framework = sys.argv[1]

tests = ["Render", "Update", "Remove"]

for t in tests:
  total_processor_joules_mean = 0
  total_dram_joules_mean = 0
  for i in range(1, 11):
    df = pd.read_csv(f"./csv/{framework}_{t}_aggregated_{i}.csv")
    total_processor_joules_mean += df["Processor total (J)"]
  print(f"{t} : {total_processor_joules_mean / 10}")


