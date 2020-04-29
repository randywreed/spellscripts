import spell.client
id=79
client=spell.client.from_environment()
run=client.runs.get(id)
print(run.run.status)
logs=run.logs()
for l in logs:
    print(l)
if run.run.status=="complete":
    run.cp('simple_results.csv','simple_results'+str(id)+'.csv')