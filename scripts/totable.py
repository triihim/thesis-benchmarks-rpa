import pandas as pd
import math
import json

browsers = ["chrome", "edge", "firefox"]
frameworks = ["react", "angular", "vue", "blazor_aot", "blazor_noaot"]
tests = ["Render", "Update", "Remove"]

columns = ["Processor total (J)", "Processor mean (W)", "DRAM total (J)", "DRAM mean (W)", "Total time (s)"]
round_to_digits = 3

for t in tests:
  for b in browsers:
    for f in frameworks:
      table = f"{t}_{f}_{b}"
      total_df = pd.DataFrame(columns=columns)
      for i in range(1,11):
        path = f"../rpa/backup_csv/{b}_{f}_{t}_aggregated_{i}.csv"
        df = pd.read_csv(path)
        total_df = pd.concat([total_df, df])
      summary = {
        "Testi": table,
        "CPU energiankulutuksen keskiarvo (J)": round(total_df[columns[0]].mean(), round_to_digits),
        "CPU energiankulutuksen keskihajonta (J)": round(total_df[columns[0]].std(), round_to_digits),
        "DRAM energiankulutuksen keskiarvo (J)": round(total_df[columns[round_to_digits]].mean(), round_to_digits),
        "DRAM energiankulutuksen keskihajonta (J)": round(total_df[columns[round_to_digits]].std(), round_to_digits),
        "CPU tehon keskiarvo (W)": round(total_df[columns[1]].mean(), round_to_digits),
        "CPU tehon keskihajonta (W)": round(total_df[columns[1]].std(), round_to_digits),
        "DRAM tehon keskiarvo (W)": round(total_df[columns[round_to_digits]].mean(), round_to_digits),
        "DRAM tehon keskihajonta (W)": round(total_df[columns[round_to_digits]].std(), round_to_digits),
        "Suoritusajan keskiarvo (S)": round(total_df[columns[4]].mean(), round_to_digits),
        "Suoritusajan keskihajonta (S)": round(total_df[columns[4]].std(), round_to_digits),
      }
      summary["Kokonaisenergiankulutus CPU+DRAM (J)"] = round(summary["CPU energiankulutuksen keskiarvo (J)"] + summary["DRAM energiankulutuksen keskiarvo (J)"], round_to_digits)
      summary["Kokonaisenergiankulutuksen keskihajonta CPU+DRAM (J)"] = round(math.sqrt(summary["CPU energiankulutuksen keskihajonta (J)"]**2 + summary["DRAM energiankulutuksen keskihajonta (J)"]**2), round_to_digits)
      json_summary = json.dumps(summary, indent=4)
      with open(f"./temp/{table}.json", "w") as outfile:
        outfile.write(json_summary)