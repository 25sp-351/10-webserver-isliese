### File Structure
10-WEBSERVER-ISLIESE/ <br>
├── main.py               # Main server execution file <br>
├── request_parser.py      # HTTP request parsing <br>
├── response_builder.py    # HTTP response generation <br>
├── handler_static.py      # Handles /static route (serves static files) <br>
├── handler_calc.py        # Handles /calc route (calculation functions) <br>
├── utils.py               # Utilities: Content-Type handling <br>
├── static/                # Static files directory (e.g., test.txt, rex.png) <br>
  	  └── test.txt           # Example static file <br>


 <br>
 
### About files
1. `main.py`
: Main entry point for the HTTP server. Handles client connections and requests using multithreading to serve multiple clients simultaneously.

2. `request_parser.py`
: Parses incoming HTTP requests, extracting the method, path, headers, and body.

3. `response_builder.py`
: Builds HTTP responses, including setting the status code, headers, and body content.

4. `handler_static.py`
: Handles requests to the /static route, serving static files from the static/ directory.

5. `handler_calc.py`
: Handles requests to the /calc route, processing mathematical operations (add, multiply, divide).

6. `utils.py`
: Provides utility functions, such as handling Content-Type and other helper methods.

 <br>

### How to Run the Server
`python3 main.py` or `python3 main.py -p 80`

 <br>

### Test with broswer
1. To test static, access "http://localhost/static/test.txt" <br> You can see 'hello rex' which is the content of static/test.txt.

2. To test calc, access "http://localhost:8080/calc/mul/8/2", http://localhost:8080/calc/add/6/8, http://localhost:8080/calc/div/9/3 <br> You can see the calculation result.

<br>

### Test with telnet
1. In the terminal, run: `telnet localhost 80`

2. To test static, enter the request:
```bash
GET /static/test.txt HTTP/1.1
Host: localhost
```

3. To test calc, enter the request:
```bash
GET /calc/add/5/3 HTTP/1.1
Host: localhost
```
