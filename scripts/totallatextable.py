import sys
import pandas as pd
import json

precision = sys.argv[1]
test_avg = bool(sys.argv[2])
property = sys.argv[3]

# If test_avg flag is true, calculate the average instead of total.
divisor = 1
if test_avg > 0:
  divisor = 3 # Test count

browsers = ["chrome", "edge", "firefox"]
browser_names = {"chrome": "Google Chrome", "edge": "Microsoft Edge", "firefox": "Mozilla Firefox"}
frameworks = ["react", "angular", "vue", "blazor_aot", "blazor_noaot"]
framework_names = {"react": "React", "angular": "Angular", "vue": "Vue", "blazor_aot": "Blazor AOT", "blazor_noaot": "Blazor JIT"}
tests = ["Render", "Update", "Remove"]

def get_property_sum(framework, browser):
  property_sum = 0
  for t in tests:
    fp = f"./temp/{t}_{framework}_{browser}.json"
    with open(fp, "r") as json_file:
      json_data = json.load(json_file)
      property_sum += json_data[property]
  return property_sum / divisor


bests = {
  "chrome": 99999999,
  "edge": 99999999,
  "firefox": 99999999
}
for f in frameworks:
  for b in browsers:
    temp = get_property_sum(f, b)
    if temp < bests[b]:
      bests[b] = temp
  
def convert_decimal(value):
  return format(value, f".{precision}f").replace(".", ",")

def get_cell_str(framework, browser):
  value = get_property_sum(framework, browser)
  best = bests[browser]
  percentage = round((value - best) / best * 100)
  diff = f"{percentage}\%"
  if percentage > 0:
     diff = r"\redtext{$\uparrow " + diff + "$}"
  return f"${convert_decimal(value)}$, {diff}"

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
    result += get_cell_str(f, b)
  result += "\\\\ \n"
  result += "\t\t\hline \n"

result += "\t\t\end{tabularx}\n"
result += "\t\caption{TODO}\n"
result += "\t\label{tab:TODO}\n"
result += "\end{table}\n"

with open("total_table.txt", "w") as outfile:
  outfile.write(result)