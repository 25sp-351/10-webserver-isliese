# request_parser.py
# HTTP 요청을 파싱합니다. / Parse HTTP request

# request_parser.py
def parse_http_request(request_data: bytes) -> dict:
    try:
        request_text = request_data.decode('utf-8')
        lines = request_text.split('\r\n')

        # Request Line: GET /path HTTP/1.1
        request_line = lines[0]
        method, path, _ = request_line.split()

        headers = {}
        for line in lines[1:]:
            if line == '':
                break  # Header 끝
            if ':' in line:
                key, value = line.split(':', 1)
                headers[key.strip()] = value.strip()

        return {
            'method': method,
            'path': path,
            'headers': headers
        }
    except Exception as e:
        print(f"Error parsing HTTP request: {e}")
        raise