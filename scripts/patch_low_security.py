import glob
import re

html_files = glob.glob('public/*.html')

target_email1 = '<a href="mailto:swerts@seacadets.org" class="hover:text-white">swerts@seacadets.org</a>'
target_email2 = '<a href="mailto:v.chandrasekharan@seacadets.org" class="hover:text-white">v.chandrasekharan@seacadets.org</a>'

# simple JS obfuscation
obf1 = """
<script>
    var part1 = "swerts";
    var part2 = "seacadets.org";
    document.write('<a href="mai' + 'lto:' + part1 + '@' + part2 + '" class="hover:text-white">' + part1 + '@' + part2 + '</a>');
</script>
<noscript>swerts [at] seacadets [dot] org</noscript>
"""

obf2 = """
<script>
    var part1 = "v.chandrasekharan";
    var part2 = "seacadets.org";
    document.write('<a href="mai' + 'lto:' + part1 + '@' + part2 + '" class="hover:text-white">' + part1 + '@' + part2 + '</a>');
</script>
<noscript>v.chandrasekharan [at] seacadets [dot] org</noscript>
"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace(target_email1, obf1).replace(target_email2, obf2)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Obfuscated emails in: {file_path}")

print("Done.")
