import sys
import pandas as pd

framework = sys.argv[1]
iteration = sys.argv[2]

render_df = pd.read_csv(f"./csv/{framework}_render_{iteration}.csv")
update_df = pd.read_csv(f"./csv/{framework}_update_{iteration}.csv")
remove_df = pd.read_csv(f"./csv/{framework}_remove_{iteration}.csv")
dfs = [render_df, update_df, remove_df]

tests = ["Render", "Update", "Remove"]
columns = ["Elapsed Time (sec)", "Processor Power_0(Watt)", "Cumulative Processor Energy_0(Joules)", "DRAM Power_0(Watt)", "Cumulative DRAM Energy_0(Joules)"]

def clean(df):
  return df.dropna(subset=columns)

def aggregate(df):
  processor_total_joules = df[columns[2]].iloc[-1]
  processor_avg_watt = df[columns[1]].mean()
  dram_total_joules = df[columns[4]].iloc[-1]
  dram_avg_power = df[columns[3]].mean()
  total_time_s = df[columns[0]].iloc[-1]
  return (processor_total_joules, processor_avg_watt, dram_total_joules, dram_avg_power, total_time_s)

index = 0
for df in dfs:
  cleaned_df = clean(render_df)
  data = aggregate(cleaned_df)
  titles = ["Processor total (J)", "Processor mean (W)", "DRAM total (J)", "DRAM mean (W)", "Total time (s)"]
  data_dict = { titles[0]: [data[0]], titles[1]: [data[1]], titles[2]: [data[2]], titles[3]: [data[3]], titles[4]: [data[4]] }
  aggregated = pd.DataFrame(data_dict)
  aggregated.to_csv(f"./csv/{framework}_{tests[index]}_aggregated_{iteration}.csv", index=False, header=titles)
  index += 1


