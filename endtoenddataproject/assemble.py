HEADERS = {
	"creditcard" : [
	'V1',
	'V2',
	'V3',
	'V4',
	'V5',
	'V6',
	'V7',
	'V8',
	'V9',
	'V10',
	'V11',
	'V12',
	'V13',
	'V14',
	'V15',
	'V16',
	'V17',
	'V18',
	'V19',
	'V20',
	'V21',
	'V22',
	'V23',
	'V24',
	'V25',
	'V26',
	'V27',
	'V28',
	'Amount',
	"Class"]
}

SELECT = {
	"creditcard": HEADERS['creditcard']
}

import os
import settings
import pandas as pd

def concatenate(prefix = "creditcard"):
	files = os.listdir(settings.DATA_DIR)
	full = []
	for f in files:
		if not f.startswith(prefix):
			continue

		data = pd.read_csv(os.path.join(settings.DATA_DIR, f))
		data = data[SELECT[prefix]]
		full.append(data)

	full = pd.concat(full,axis=0)
	full.to_csv(os.path.join(settings.PROCESSED_DIR, "{}.txt".format(prefix)), sep=",", header=SELECT[prefix], index=False)

if __name__ == "__main__":
	concatenate("creditcard")