# Least Recently USed Cache problem, exposed as a REST API using Flask (Python's micro web framework)

This code was written on a Windows 8 (64-bit) machine in Python 3.7.3. Instructions to run are given below.

Install Python 3.7.3 and add to Path:
- Download Python 3.7.3 from https://www.python.org/downloads/ and install it
- If installed at C:\Users\YourName\Desktop\Python 3.7.3, the python.exe file will be located at C:\Users\YourName\Desktop\Python 3.7.3\python.exe. Make sure to add C:\Users\YourName\Desktop\Python 3.7.3 to Path variable
- "Path" variable can be edited at: Environment Variables --> User Variables

Install flask (Python's micro web framework to write a REST api):
- Also add C:\Users\YourName\Desktop\Python 3.7.3\Scripts to Path, so that pip can be used to install new python packages. Note that pip does not come packaged with all Python versions (but some of the latest Python versions like 3.7.3 have it for sure)
- Open Windows Command Prompt (search for cmd)
- run the following command (from any directory, since pip's location can be recognized from Path variable): pip install flask

Install curl:
- Download latest curl version compatible with your machine
- Make sure it has curl.exe executable file
- If curl.exe is located at C:\Users\YourName\Desktop\curl-7.64.0-win64-mingw\bin\curl.exe, add the parent folder i.e. C:\Users\YourName\Desktop\curl-7.64.0-win64-mingw\bin to Path

Start the web app:
- From Windows Command Prompt, cd to the folder where you have the python file lruCacheFlask.py
- run: python lruCacheFlask.py 2
(2 is the cache's capacity. It could be set to any other integer. Plz make sure to pass only an integer)
- On the Command Prompt, you will see where the server is listening for requests. Say, http://127.0.0.1:5000/ which is the same as http://localhost:5000/

Make REST calls to test it:
- Open Windows Command Prompt in a new window
- Make the following calls (in order) to test the example given in the question.
Note: Please make sure to include -H "Content-Type: text" in the PUT calls, else there are parsing errors
curl -H "Content-Type: text" -X PUT http://localhost:5000/api/v1/put/1 -d "value=400"
curl -H "Content-Type: text" -X PUT http://localhost:5000/api/v1/put/2 -d "value=800"
curl -X GET http://localhost:5000/api/v1/get/1
curl -H "Content-Type: text" -X PUT http://localhost:5000/api/v1/put/3 -d "value=1200" // key 2 gets evicted and is printed as output
... and so on
