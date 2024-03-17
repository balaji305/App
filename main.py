# Copyright 2015 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
from flask import Flask, jsonify, request

app = Flask(__name__)

def job_matching(context, threshold, noOfMatches, inputFilePath):
    return [{"jobTitle": "Data Scientist", "company": "Google", "location": "Mountain View, CA", "url": "https://www.google.com/careers"}, 0.9], 0.9

def resume_matching(context, threshold, noOfMatches, inputFilePath):
    return [{"name": "John Doe", "location": "San Francisco, CA", "url": "https://www.linkedin.com/in/johndoe"}, 0.9], 0.9

@app.route("/ping",methods=['GET'])
def ping_fun():
    response = {
       "status": "healthy",
       "dependencies": {
         "modelAPIS": {
           "model1": "online",
           "model2": "online"
         },
         "database": {
           "connection": "available",
           "responseTime": "12 ms"
         },
         "memory": {
           "usage": 0.5  # Use the memory value from the YAML file
         },
         "cpu": {
           "usage": 1  # Use the cpu_usage value from the YAML file
         }
       }
    }
    return jsonify(response), 200


@app.route("/search",methods=['POST'])
def search_fun():
    data = request.json
    context = data['context']
    category = data['category']
    threshold = data['threshold']
    noOfMatches = data['noOfMatches']
    inputPath = data['inputPath']

    if(category.lower() == "job"):
        matches, score = job_matching(context, threshold, noOfMatches, inputPath)
        response = {
            "status": "success",
            "count": len(matches),
            "metadata": {
                "confidence score": score,
            },
            "results": matches
        }
        return jsonify(response), 200
    elif(category.lower() == "resume"):
        matches, score = resume_matching(context, threshold, noOfMatches, inputFilePath), 200
        response = {
            "status": "success",
            "count": len(matches),
            "metadata": {
                "confidence score": score,
            },
            "results": matches
        }
        return jsonify(response), 200
    else:
        return jsonify({"status": "Bad Request Please check category should be either resume or job!"}), 400




if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_flex_quickstart]
