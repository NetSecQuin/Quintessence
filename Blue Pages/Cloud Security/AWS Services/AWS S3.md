# AWS S3




### Presigned URLs

Presigned URLs can be useful for when a user, who does not have AWS access, needs to upload/download a specific file(s) from S3. Presigned URLs allow an IAM user to pass specific authentication parameters and wrap it in a URL. For example. If an user is accessing a website that stores image files in S3, the website may use a service account (IAM User) to create a presigned URL of the image. This URL would be wrapped in permissions to access the specific file in the S3 bucket, for a limited amount of time, and passed to the user. 

Somet things to think about in regards to presigned URL architecture. 
- When using the URL, the permission match the identity which generated it, therefore:
  - Access denied could mean the generating ID never had access or does not now/on click.
- Dont generate with a role, URL stops working when temporary credentials expire. Therefore it is meant to be used with a IAM user. 
