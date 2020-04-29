import spell.client
client=spell.client.from_environment()
prompt='the crux of calvinism is the soverignty of God. If god is soverign, then god controls everything. Thus the doctrin of predestination holds'
cmd="python gen_gpt2.py --prompt '"+prompt+"'"
run=client.runs.new(command=cmd,machine_type='k80x2-prempt',\
    github_url="https://github.com/randywreed/gpt2-generate.git", \
    github_ref="master",pip_packages=["gpt-2-simple"], \
    attached_resources={'runs/54/models':'/spell/models'})
print(run.id)
run.wait_status(*client.runs.FINAL)
run.cp("simple_results.csv")
for line in run.logs():
    print(line)
