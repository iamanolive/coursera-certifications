fname = "mbox-short.txt"
fhandle = open(fname)

senders = dict()

for line in fhandle:
    if len(line) > 2 and line.startswith("From "):
        words = line.split()
        sender = words[1]
        senders[sender] = senders.get(sender, 0) + 1

maximum_count = None
maximum_sender = None

for key in senders:
    if maximum_count is None:
        maximum_count = senders[key]
        maximum_sender = key
    elif maximum_count < senders[key]:
        maximum_count = senders[key]
        maximum_sender = key

print(maximum_sender, maximum_count)