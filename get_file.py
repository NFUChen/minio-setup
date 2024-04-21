
from datetime import timedelta
from minio import Minio


client = Minio("localhost:9000",
        access_key="WXDj1Y5cW8JZ1gyWgYvD",
        secret_key="iHLtuRRHFaIMDeqfDuUoOR5AYVDkMgiEk42bXEmh",
        secure= False
    )
bucket_name = "python-test-bucket"
destination_file = "test-jpg-in-bucket.txt"
object = client.get_object(bucket_name, destination_file)
print(object.data)
url = client.get_presigned_url(
    "GET",
    bucket_name,
    destination_file,
    expires=timedelta(hours=2),
)

print(url)