import os

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME=os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL="https://79193314349bc369b2b6a6f7eeadcf63.r2.cloudflarestorage.com/spotlight-bucket"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_LOCATION = f"https://{AWS_STORAGE_BUCKET_NAME}.79193314349bc369b2b6a6f7eeadcf63.r2.cloudflarestorage.com/spotlight-bucket"

DEFAULT_FILE_STORAGE = "core.settings.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "core.settings.cdn.backends.StaticRootS3Boto3Storage"
