import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

cols = ["Processor total (J)", "Processor mean (W)", "DRAM total (J)", "DRAM mean (W)", "Total time (s)"]

def get_test_results(browser, framework):

  def get_summary_csv(test_id):
    csv_path = f"../rpa/csv/{test_id}_summary.csv"
    return pd.read_csv(csv_path)[cols]

  render = get_summary_csv(f"{browser}_{framework}_Render")
  update = get_summary_csv(f"{browser}_{framework}_Update")
  remove = get_summary_csv(f"{browser}_{framework}_Remove")

  def get_column_summary(col_index):
    return np.array([render[cols[col_index]].iloc[0], 
            update[cols[col_index]].iloc[0], 
            remove[cols[col_index]].iloc[0], 
            render[cols[col_index]].iloc[0] + update[cols[col_index]].iloc[0] + remove[cols[col_index]].iloc[0]])

  cpu_energy_total = get_column_summary(0)
  cpu_watt_mean = get_column_summary(1)
  dram_energy_total = get_column_summary(2)
  dram_watt_mean = get_column_summary(3)
  total_time = get_column_summary(4)

  return {
    "total_energy": cpu_energy_total + dram_energy_total,
    "total_watts": cpu_watt_mean + dram_watt_mean,
    "cpu_energy_total": cpu_energy_total,
    "cpu_watt_mean": cpu_watt_mean,
    "dram_energy_total": dram_energy_total,
    "dram_watt_mean": dram_watt_mean,
    "total_time": total_time
  }
  
def get_plot(browser, property):
  xlabel = "DOM-testi"
  ylabel = ""
  title = ""

  if property == "total_energy":
    ylabel = "Kokonaisenergiankulutus (J)"
    title = f"Kokonaisenergiankulutus {browser.capitalize()}-verkkoselaimessa"
  elif property == "total_watts":
    ylabel = "Kokonaisteho (W)"
    title = f"Kokonaisteho {browser.capitalize()}-verkkoselaimessa"
  elif property == "cpu_energy_total":
    ylabel = "CPU:n energiankulutus (J)"
    title = f"CPU:n energiankulutus {browser.capitalize()}-verkkoselaimessa"
  elif property == "cpu_watt_mean":
    ylabel = "CPU:n tehon keskiarvo (W)"
    title = f"CPU:n tehonkäyttö {browser.capitalize()}-verkkoselaimessa"
  elif property == "dram_energy_total":
    ylabel = "DRAM:in energiankulutus (J)"
    title = f"DRAM:in energiankulutus {browser.capitalize()}-verkkoselaimessa"
  elif property == "dram_watt_mean":
    ylabel = "DRAM:in tehon keskiarvo (W)"
    title = f"DRAM:in tehonkäyttö {browser.capitalize()}-verkkoselaimessa"
  elif property == "total_time":
    ylabel = "Suoritusaika (s)"
    title = f"Suoritusaika {browser.capitalize()}-verkkoselaimessa"

  x_labels = ["Piirto", "Päivitys", "Poisto", "Piirto+Päivitys+Poisto"]
  x_indexes = np.arange(len(x_labels))
  bar_width = 0.15
  react = get_test_results(browser, "react")
  angular = get_test_results(browser, "angular")
  vue = get_test_results(browser, "vue")
  blazor_aot = get_test_results(browser, "blazor_aot")
  blazor_noaot = get_test_results(browser, "blazor_noaot")
  ax = plt.subplot()
  ax.set_title(title)
  ax.bar(x_indexes - 2*bar_width, react[property], width=bar_width, label="React", color="#61DBFB")
  ax.bar(x_indexes - bar_width, angular[property], width=bar_width, label="Angular", color="#DD0031")
  ax.bar(x_indexes, vue[property], width=bar_width, label="Vue", color="#42b883")
  ax.bar(x_indexes + bar_width, blazor_aot[property], width=bar_width, label="Blazor AOT", color="#562B88")
  ax.bar(x_indexes + 2*bar_width, blazor_noaot[property], width=bar_width, label="Blazor NOAOT", color="#CE3EE5")
  ax.set_xticks(x_indexes, x_labels)
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  ax.legend(facecolor='white', framealpha=1)
  return ax


browsers = ["chrome", "firefox", "edge"]
plots = ["total_energy", "total_watts", "cpu_energy_total", "cpu_watt_mean", "dram_energy_total", "dram_watt_mean", "total_time"]

for b in browsers:
  for p in plots:
    fig = plt.figure()
    plot = get_plot(b, p)
    fig.add_subplot(plot)
    fig.set_size_inches(8, 5)
    fig.savefig(f"../rpa/figures/{b}_{p}.png")
    plt.close()
      
      

