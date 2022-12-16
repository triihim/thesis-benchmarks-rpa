import sys
import pandas as pd
import json

test = sys.argv[1].capitalize()
precision = sys.argv[2]
property = sys.argv[3]
std = sys.argv[4]

output = "./table.txt"

browsers = ["chrome", "edge", "firefox"]
browser_names = {"chrome": "Google Chrome", "edge": "Microsoft Edge", "firefox": "Mozilla Firefox"}
frameworks = ["react", "angular", "vue", "blazor_aot", "blazor_noaot"]
framework_names = {"react": "React", "angular": "Angular", "vue": "Vue", "blazor_aot": "Blazor AOT", "blazor_noaot": "Blazor JIT"}

def get_best(browser):
  best_value = 999999
  for f in frameworks:
    path = f"./temp/{test}_{f}_{browser}.json"
    with open(path, "r") as json_file:
      json_data = json.load(json_file)
      if json_data[property] < best_value:
        best_value = json_data[property]
  return best_value

def convert_decimal(value):
  return format(value, f".{precision}f").replace(".", ",")

def get_cell_str(test, framework, browser):
  json_data = {}
  json_path = f"./temp/{test}_{framework}_{browser}.json"
  with open(json_path, "r") as json_file:
    json_data = json.load(json_file)
  value = json_data[property]
  best = get_best(browser)
  percentage = round((value - best) / best * 100)
  diff = f"{percentage}\%"
  if percentage > 0:
    diff = r"\redtext{$\uparrow " + diff + "$}"
  return f"${convert_decimal(value)} \pm {convert_decimal(json_data[std])}$, {diff}"

result = str()
result += "\\begin{table}[htb!]\n"
result += "\t\centering\n"
result += "\t\\begin{tabularx}{\\textwidth}{|l|X|X|X|}\n"
result += "\t\t\hline \n"
result += "\t\t\multicolumn{4}{|c|}{\\textbf{TODO}} \\\\ \n"
result += "\t\t\hline \n"
result += "\t\t\hline \n"
for b in browsers:
  result += f"\t\t& {browser_names[b]}"
result += "\\\\ \n"
result += "\t\t\hline \n"

for f in frameworks:
  result += "\t\t"
  result += framework_names[f]
  for b in browsers:
    result += " & "
    result += get_cell_str(test, f, b)
  result += "\\\\ \n"
  result += "\t\t\hline \n"

result += "\t\t\end{tabularx}\n"
result += "\t\caption{TODO}\n"
result += "\t\label{tab:TODO}\n"
result += "\end{table}\n"

with open(output, "w") as outfile:
  outfile.write(result)

