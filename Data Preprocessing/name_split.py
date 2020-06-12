import re

a = "branch-instructions, branch-misses, bus-cycles, cache-misses, cache-references, cpu-cycles, instructions, ref-cycles, alignment-faults, context-switches, cpu-clock, cpu-migrations, dummy, emulation-faults, major-faults, minor-faults, page-faults, task-clock, L1-dcache-load-misses, L1-icache-load-misses, L1-icache-loads, LLC-loads, LLC-stores, branch-load-misses, branch-loads, dTLB-load-misses, iTLB-load-misses, iTLB-loads, cpu/branch-instructions/, cpu/branch-misses/, cpu/cache-misses/, cpu/cache-references/, cpu/cpu-cycles/, cpu/instructions/, msr/aperf/, msr/mperf/, msr/tsc/"

def split(text):
    cleaned_text = re.sub('                   ', ',', text)
    cleaned_text = re.sub('                  ', ',', cleaned_text)
    cleaned_text = re.sub('                 ', ',', cleaned_text)
    cleaned_text = re.sub('                ', ',', cleaned_text)
    cleaned_text = re.sub('               ', ',', cleaned_text)
    cleaned_text = re.sub('              ', ',', cleaned_text)
    cleaned_text = re.sub('             ', ',', cleaned_text)
    cleaned_text = re.sub('            ', ',', cleaned_text)
    cleaned_text = re.sub('           ', ',', cleaned_text)
    cleaned_text = re.sub('          ', ',', cleaned_text)
    cleaned_text = re.sub('         ', ',', cleaned_text)
    cleaned_text = re.sub('        ', ',', cleaned_text)
    cleaned_text = re.sub('       ', ',', cleaned_text)
    cleaned_text = re.sub('      ', ',', cleaned_text)
    cleaned_text = re.sub('     ', ',', cleaned_text)
    cleaned_text = re.sub('    ', ',', cleaned_text)
    cleaned_text = re.sub('   ', ',', cleaned_text)
    cleaned_text = re.sub('  ', ',', cleaned_text)
    cleaned_text = re.sub(' ', ',', cleaned_text)
    return cleaned_text

a = re.sub(',',"\",\"",a)
a = re.sub(' ', '', a)
print(a)