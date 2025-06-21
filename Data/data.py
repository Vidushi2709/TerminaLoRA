import csv
import json
import html
from bs4 import BeautifulSoup 

#remove tagsss
def html_to_text(html_str):
    soup= BeautifulSoup(html_str, "html.parser")

    for code in soup.find_all("code"):
        code.replace_with(f"{code.text.strip()}")
    
    for pre in soup.find_all("pre"):
        pre.replace_with(f"\n'''\n{pre.text.strip()}\n'''\n")
    
    text= soup.get_text(separator="\n")
    return html.unescape(text).strip()

csv_f= "QueryResults.csv"
json_f= "data_for_finetuning.json"
data=[]

with open(csv_f, newline='', encoding='utf-8') as f:
    reader= csv.DictReader(f)
    for r in reader:
        title= r['Title'].strip()
        answer_html= r['Answer']
        cleaned= html_to_text(answer_html)

        data.append({
            "instruction": title,
            "response": cleaned
        })
    
with open(json_f, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent= 2, ensure_ascii=False)

print("done done done")
                         