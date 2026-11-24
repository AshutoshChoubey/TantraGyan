from pages_part1 import get_pages_part1
from pages_part2 import get_pages_part2
from pages_part3 import get_pages_part3
from pages_part4 import get_pages_part4
import re

p1 = get_pages_part1()
p2 = get_pages_part2()
p3 = get_pages_part3()
p4 = get_pages_part4()
all_pages = p1 + p2 + p3 + p4

print(f"Total pages: {len(all_pages)}")

for i, page in enumerate(all_pages, 1):
    # Check for python code
    py_matches = re.findall(r'def\s+[a-zA-Z0-9_]+\s*\(|import\s+[a-zA-Z0-9_]+|class\s+[a-zA-Z0-9_]+|```python|elif |return ', page)
    # Check for raw math commands / backslashes
    math_matches = re.findall(r'\\(?:tan|sin|cos|lfloor|rfloor|pmod|implies|alpha|beta|lambda|Delta|theta|deg|frac|text|left|right)', page)
    # Check for dollar signs
    dollars = page.count('$')
    # Check for raw markdown hashes
    hashes = re.findall(r'#{2,}', page)
    
    issues = []
    if py_matches:
        issues.append(f"Python: {py_matches}")
    if math_matches:
        issues.append(f"Math: {math_matches}")
    if dollars > 0:
        issues.append(f"Dollars: {dollars}")
    if hashes:
        issues.append(f"Hashes: {hashes}")
        
    if issues:
        print(f"Page {i:03d} issues: {', '.join(issues)}")
