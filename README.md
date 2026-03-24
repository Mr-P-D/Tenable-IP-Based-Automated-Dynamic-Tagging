**Objective:**
if you need to create dynamic tagging based on IP Ranges then this script is for you.

**How to use:**
1) Add Secret Key and Access Key in the Python Script
2) Update the sample-tags.csv based on your requirement.
3) Execute the Script to create the Tags.

**Successful Output:**
Processing: CustomerName Subnets -> DMZ
Tag created

**Error Due to Duplicate Entries:**
Processing: CustomerName Subnets -> Corp WiFi
[400: POST] https://cloud.tenable.com/tags/values body=b'{"errors":[{"property":"value","rule":"duplicate","message":"Duplicate tag value \'Corp WiFi\' cannot be created."}],"error":"Duplicate tag value \'Corp WiFi\' cannot be created."}'
Error: [400: POST] https://cloud.tenable.com/tags/values body=b'{"errors":[{"property":"value","rule":"duplicate","message":"Duplicate tag value \'Corp WiFi\' cannot be created."}],"error":"Duplicate tag value \'Corp WiFi\' cannot be created."}'

**Error Due to Incorrect IPs:**
Processing: Wateridge Subnets -> WR_Secured
filter_value has value of 10.2.3/24.  Does not match pattern ^(\s*((?=\d+\.\d+\.\d+\.\d+(?:\/|-|\s*,|$))(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.?){4})(?:(?:\/(?:3[0-2]|[12]+\d|[1-9]))|((?:-(?=\d+\.\d+\.\d+\.\d+)(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.?){4})|(?:\s*,(?:\s*)))?)+)+$
Error: filter_value has value of 10.2.3/24.  Does not match pattern ^(\s*((?=\d+\.\d+\.\d+\.\d+(?:\/|-|\s*,|$))(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.?){4})(?:(?:\/(?:3[0-2]|[12]+\d|[1-9]))|((?:-(?=\d+\.\d+\.\d+\.\d+)(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.?){4})|(?:\s*,(?:\s*)))?)+)+$
