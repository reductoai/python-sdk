# Parse

Types:

```python
from reducto.types import AsyncParseResponse, ParseResponse, ParseParseResponse
```

Methods:

- <code title="post /parse">client.parse.<a href="./src/reducto/resources/parse.py">parse</a>(\*\*<a href="src/reducto/types/parse_parse_params.py">params</a>) -> <a href="./src/reducto/types/parse_parse_response.py">ParseParseResponse</a></code>
- <code title="post /parse_async">client.parse.<a href="./src/reducto/resources/parse.py">parse_async</a>(\*\*<a href="src/reducto/types/parse_parse_async_params.py">params</a>) -> <a href="./src/reducto/types/async_parse_response.py">AsyncParseResponse</a></code>

# Extract

Types:

```python
from reducto.types import AsyncExtractResponse, ExtractResponse
```

Methods:

- <code title="post /extract">client.extract.<a href="./src/reducto/resources/extract.py">extract</a>(\*\*<a href="src/reducto/types/extract_extract_params.py">params</a>) -> <a href="./src/reducto/types/extract_response.py">ExtractResponse</a></code>
- <code title="post /extract_async">client.extract.<a href="./src/reducto/resources/extract.py">extract_async</a>(\*\*<a href="src/reducto/types/extract_extract_async_params.py">params</a>) -> <a href="./src/reducto/types/async_extract_response.py">AsyncExtractResponse</a></code>

# Jobs

Types:

```python
from reducto.types import AsyncJobResponse, JobCancelResponse
```

Methods:

- <code title="get /job/{job_id}">client.jobs.<a href="./src/reducto/resources/jobs.py">retrieve</a>(job_id) -> <a href="./src/reducto/types/async_job_response.py">AsyncJobResponse</a></code>
- <code title="post /cancel/{job_id}">client.jobs.<a href="./src/reducto/resources/jobs.py">cancel</a>(job_id) -> <a href="./src/reducto/types/job_cancel_response.py">object</a></code>

# Upload

Types:

```python
from reducto.types import UploadResponse
```

Methods:

- <code title="post /upload">client.upload.<a href="./src/reducto/resources/upload.py">upload</a>(\*\*<a href="src/reducto/types/upload_upload_params.py">params</a>) -> <a href="./src/reducto/types/upload_response.py">UploadResponse</a></code>

# Webhooks

Types:

```python
from reducto.types import WebhookConfigureResponse
```

Methods:

- <code title="post /configure_webhook">client.webhooks.<a href="./src/reducto/resources/webhooks.py">configure</a>() -> str</code>

# Version

Types:

```python
from reducto.types import VersionRetrieveResponse
```

Methods:

- <code title="get /version">client.version.<a href="./src/reducto/resources/version.py">retrieve</a>() -> <a href="./src/reducto/types/version_retrieve_response.py">object</a></code>
