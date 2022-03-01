# -------------------------------------------------------------------------
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
# ----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
# --------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "python_quickstart_client.py "
# Please note that storing the batch and storage account keys in Azure Key Vault
# is a better practice for Production usage.

_BATCH_ACCOUNT_NAME = 'keusotebatchaccount'  # Your batch account name
_BATCH_ACCOUNT_KEY = 'v/H5k/d8/mx03RHTIH+qDGpnDzs91iOO6YK6XJSWAkC0zgV+poU/5Tu2JuuE7KCAapuGRAzd/0RczoQ5z5I+DA=='  # Your batch account key
_BATCH_ACCOUNT_URL = 'https://keusotebatchaccount.westeurope.batch.azure.com'  # Your batch account URL
_STORAGE_ACCOUNT_NAME = 'keusotebatchtestdatastor'  # Your storage account name
_STORAGE_ACCOUNT_KEY = 'oK3EJQgRd6GLr4taCElN1fR1CJeEl0fYNMj0UkZUzUvP3pSDWUQl7SNGY30dcYH+FZwse0nYqtwgHSFh+JW9pw=='  # Your storage account key
_POOL_ID = 'PythonQuickstartPool'  # Your Pool ID
_POOL_NODE_COUNT = 1  # Pool node count
_POOL_TARGET_DEDICATED_NODES = 0 # Pool Dedicated node count
_POOL_TARGET_LOW_PRIORITY_NODES = 3 # Pool Low priority node count
_POOL_VM_SIZE = 'Standard_D2_v3'  # VM Type/Size
_JOB_ID = 'PythonQuickstartJob'  # Job ID
_STANDARD_OUT_FILE_NAME = 'stdout.txt'  # Standard Output file
_POOL_START_COMMAND = "/bin/bash -c \"sudo apt update -y \
    && sudo apt install python3.7 -y \
    && sudo apt install python3-pip -y\""
_JOB_PREPARATION_COMMAND = "/bin/bash -c \"sudo cp /mnt/batch/tasks/fsmounts/batch/batch-input/requirements.txt . \
    && sudo -H python3.7 -m pip install -r requirements.txt\""
_MAX_TASK_COUNT_PER_NODE = 1
_TASK_DISTRIBUTION_MODE = 'spread'
