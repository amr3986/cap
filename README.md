<h1>Casting Agency (Capstone Project)</h1>

<h2>Description</h2>

<p>This is the last projectin FSDN it show the skills gained by the student from the beginning of the course </p>
<ol>
    <li>Fyyur project: Database and SQL management.</li>
    <li>Trivia project: API Development and Documentation</li>
    <li>Coffee Shop project: Identity and Access Management</li>
    <li>Deploy Your Flask App to Kubernetes Using EKS project: Server Deployment, Containerization using aws</li>
</ol>

<h2>Dependencies</h2>

<h3>- Python 3.7.9</h3>
<p>
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/windows.html?highlight=installing%20latest%20version%20python)
</p>

<h3>- PIP Dependencies</h3>
<p>

```bash
pip install -r requirements.txt
```
This will install all of the required packages for this project.
</p>

<h3>- Running the server</h3>
<p>
To run the server inside the root directory, open a new terminal session, and run:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

To run the server, execute:

```bash
flask run 
```



<h2>Tasks</h2>
<p> in order to use the app properly follow the fowling steps:
</p><br>
<h3>- Setup Auth0</h3>
<ol>
    <li>Create a new Auth0 Account</li>
    <li>Select a unique tenant domain</li>
    <li>Create a new, single page web application</li>
    <li>Create a new API
        - in API Settings:
            <ul>
                <li>Enable RBAC</li>
                <li>Enable Add Permissions in the Access Token</li>
            </ul>
    </li>
    <li>Create new API permissions:
        <ul>
            <li>get:actors</li>
            <li>get:movies</li>
            <li>post:actor</li>
            <li>post:movie</li>
            <li>patch:actor</li>
            <li>patch:movie</li>
            <li>delete:actor</li>
            <li>delete:movie</li>
        </ul>
    </li>
    <li>Create new roles for:
        <ul>
            <li> Assistant<br/>
                - can get:actors and get: movies
            </li>
            <li> Director<br/>
                - can get:actors and get: movies<br/>
                - can post:actor and delete:actor<br/>
                - can patch:actor and patch:movie<br/>
            </li>
            <li> Producer<br/>
                - can perform all actions<br/>
            </li>
        </ul>
    </li>
    <li>Register 3 users
        <ul>
            <li>Assign the  Assistant role to one</li>
            <li>Assign the  Director role to another</li>
            <li>Assign the  Producer role to the last one </li>
        </ul>
    </li>
    <li>Sign into each account and make note of the JWT.</li>
    <li>Test the endpoints with the latest version of [Postman](https://getpostman.com). 
        <ul>
            <li>Import the postman collection "./CastingAgency_FSND.postman_collection.json"</li>
            <li>Right-clicking the collection folder for Assistant, Director and Producer, navigate to the authorization tab, and include the JWT in the token field (you should have noted these JWTs).</li>
            <li>Run the collection.</li>
            <li>The collection points to heroku app hosted on : https://appv22.herokuapp.com/</li>
        </ul>
    </li>
</ol>

<h3>- Testing</h3>
To run the unit tests, execute:

```bash
python3 test_app.py
```
Note - make sure the 3 header variables(assistant_header , director_header , producer_header) are updated for each role JWT collected.
