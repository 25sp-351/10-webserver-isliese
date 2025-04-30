# handler_calc.py
# Handle calculation requests under /calc

def handle_calc_request(path: str) -> tuple:
    """
    Handle calculation requests based on path components.

    Returns: (status_code, content_type, body)
    """
    try:
        # /calc/add/5/3 → ['calc', 'add', '5', '3']
        parts = path.strip('/').split('/')

        if len(parts) != 4:
            return (400, "text/plain", b"Bad Request: Invalid path format")

        _, op, x_str, y_str = parts

        # 숫자 변환 시도
        try:
            x = float(x_str)
            y = float(y_str)
        except ValueError:
            return (400, "text/plain", b"Bad Request: Non-numeric operands")

        # 연산 수행
        if op == "add":
            result = x + y
        elif op == "mul":
            result = x * y
        elif op == "div":
            if y == 0:
                return (400, "text/plain", b"Bad Request: Division by zero")
            result = x / y
        else:
            return (400, "text/plain", b"Bad Request: Unknown operation")

        # 결과를 HTML로 포장
        html_body = f"""
        <html>
            <body>
                <h3>Calculation Result</h3>
                <p>{x} {op} {y} = {result}</p>
            </body>
        </html>
        """.strip().encode('utf-8')

        return (200, "text/html", html_body)

    except Exception as e:
        print(f"Error handling calc request: {e}")
        return (500, "text/plain", b"Internal Server Error")