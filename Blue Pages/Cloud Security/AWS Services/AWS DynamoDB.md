# AWS DynamoDB 


# DynamoDB Encryption
- All DynamoDB tables are encrypted at rest by default. There is not an option otherwise.
- You cannot use a customer managed key with DAX
- LSI/GSI use the same key as teh table
- Backups use the same key, resotures require that key.A restored table can use differnet encrpytion settings
- Customer managed keys work with transactions but a temporary compay uses AWS owned key
- Data in streams have a 24 hours lifetime even when a key is disabled
- If CMK is disabled or inaccessible for 7 days, an assoicated table is backed up and archived. In order to restore an archvied table, you will need the key. 
