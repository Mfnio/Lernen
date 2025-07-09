import json
data = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dnZWRJbkFzIjoiYWRtaW4iLCJpYXQiOjE0MjI3Nzk2Mzh9.gzSraSYS8EXBxLN _oWnFSRgCzcmJmMjLiuyu5CSpyHI='
data = data.json(data)
print(data)
# The above code is incorrect because the string 'data' is not a valid JSON string.
# The correct way to decode a JWT token is to split it into its parts and decode the
# payload part, which is the second part of the token.
import base64