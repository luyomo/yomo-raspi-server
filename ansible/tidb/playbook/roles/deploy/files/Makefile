tiVersion = v5.0.0
flashName = tidb-test

flash:
	tiup cluster deploy $(flashName) $(tiVersion) ./tidb.tiflash.yaml

startFlash:
	tiup cluster start $(flashName)

cleanFlash:
	tiup cluster destroy $(flashName) --force

stateFlash:
	tiup cluster display $(flashName)
