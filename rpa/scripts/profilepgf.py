import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

browser = sys.argv[1]
framework = sys.argv[2]
iteration = sys.argv[3]


render_df = pd.read_csv(f"./csv/{browser}_{framework}_render_{iteration}.csv")
update_df = pd.read_csv(f"./csv/{browser}_{framework}_update_{iteration}.csv")
remove_df = pd.read_csv(f"./csv/{browser}_{framework}_remove_{iteration}.csv")
dfs = [render_df, update_df, remove_df]

titles = ["Piirto", "Päivitys", "Poisto"]
columns = ["Elapsed Time (sec)", "Processor Power_0(Watt)", "DRAM Power_0(Watt)"]

plt.style.use("ggplot")
fig = plt.figure()

def clean(df):
  return df.dropna(subset=columns)

index = 1
for df in dfs:
  selected = clean(df[columns])
  time = selected[columns[0]]
  processor = selected[columns[1]]
  dram = selected[columns[2]]
  subplot = fig.add_subplot(3,1, index)
  subplot.plot(time, processor)
  subplot.plot(time, dram)
  subplot.set_ylabel(titles[index - 1])
  index += 1

fig.supxlabel("Aika (s)")
fig.supylabel("Teho (W)")
fig.suptitle(f"{(framework.upper())}-tehoprofiili {browser.upper()}-verkkoselaimessa")
fig.legend(labels=["CPU", "DRAM"], loc="upper right")
fig.set_size_inches(6.5, 4.5)
plt.savefig(f"./figures/pgf/{browser}_{framework}_profiles_{iteration}.pgf")