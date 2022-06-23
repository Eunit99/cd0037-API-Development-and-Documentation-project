# Trivia API

## Introduction

Trivia API was created as a backend for the Trivia project based on Udacity course, it has endpoints to handle creation of questions and also returning random question for quizzes. Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out, hence the creation of this trivia API.

All backend code follows the [PEP8 guidelines](https://peps.python.org/pep-0008/).

## Getting Started

- **BASE URL**: the base url is still at localhost since its still in local development

  ```curl
  localhost:5000/
  ```

- API KEYS / AUTHENTICATION: Authentication, authorization and API keys are not needed to access the API.

## Error

This project handles errors and success by using the traditional http response codes

1. ``2xx`` This code indicates successful responses
2. ``4xx`` This code indicates errors from client
3. ``5xx`` This code indicates errors from the server

Below are the list of the codes returned and their meaning

- ``200``: This code indicates that the request was successful sample.
- ``400``: This error occurs when the server will not process the request due to missing headers or data
- ``404``: This error is returned when the question, category or route requested was not found
- ``405``: This code indicates an error with this code occurs when the method used in the request was not accepted.
- ``406``: This error happens when a request is rejected due to missing or incorrect parameters.
- ``500``: This error indicates that the server could not handle the request

Sample responses for success and errors

- Sample success response

  ```json
  {
      "current_category": "all",
      "question": {
          "answer": "206",
          "category": 2,
          "difficulty": 3,
          "id": 17,
          "question": "How many bones are there in the human body?"
      },
      "success": true
  }

  ```

- Sample error response

  ```json
  {
      "error": 404,
      "success": false,
      "message": "Not Found",
  }
  ```

## Resource Endpoint Library

- ### Questions

  this endpoint handles all processes for creating, retrieving and searching of questions,


  - **Retrieve Questions**: perform a ``GET`` requests on this endpoint

    ```javascript
    GET /questions
    ```

    This endpoint also accepts a ``page`` parameter that indicates the ``page`` number, the total questions per ``page`` is 10, it also returns all available categories.

    ```javascript
    GET /questions?page=3
    ```

    Sample response:

    ```json
        {

            "page": 2,
            "questions": [
                {
                "answer": "Alexander Fleming",
                "category": 1,
                "difficulty": 3,
                "id": 21,
                "question": "Who discovered penicillin?"
                },
                {
                "answer": "yes",
                "category": 5,
                "difficulty": 5,
                "id": 25,
                "question": "well done"
                }
            ],
            "success": true,
            "total_questions": 2
            "categories": {
                "1" : "Science",
                "2" : "Art",
                "3" : "Geography",
                "4" : "History",
                "5" : "Entertainment",
                "6" : "Sports"
              }
        }
    ```

  - **Create Questions**: To create questions, perform a post request with the following attributes, it will create a question in the database and returns a response that contains id of the created question.

    **attributes**

    1. ``question``: this is a ``string`` that represents the question to be asked
    2. ``answer``: a ``string`` parameter that specifies the answer for the question
    3. ``category``: an ``integer`` to specify the category the question belongs to
    4. ``difficulty``: an ``integer`` which specifies the difficulty of the question

    **sample request**

    ```curl
    curl -X POST -d '{"question":"How many continents are there in the world?", "answer":"7", "category":1, "difficulty":1}' localhost:5000/questions -H "Content-Type: application/json"
    ```

    **response**

    ```json
    {
        "success":true,
        "question_created": 1
    }
    ```

  - **Search For Questions**: You also, have the ability to search for questions. To do this, make a `POST` request using a ``search_term`` parameter in the ``POST`` request body.

    **sample request**

    ```curl
    curl -X POST -d '{"search_term":"name"}' localhost:5000/questions -H "Content-Type: application/json"
    ```

    **response**

    ```json
    {
        "questions": [
            {
                "answer": "Muhammad Ali",
                "category": 4,
                "difficulty": 1,
                "id": 9,
                "question": "What boxer's original name is Cassius Clay?"
            },
            {
                "answer": "Brazil",
                "category": 6,
                "difficulty": 3,
                "id": 10,
                "question": "Which is the only team to play in every soccer World Cup tournament?"
            }
        ],
        "search_term": "name",
        "success": true,
        "total_questions": 2
    }
    ```

  - **Delete Question**: this deletes the selected question using its ``id`` in the url, the reponse includes the id of the deleted question and a list of available questions.

    ```javascript
        DELETE /questions/{id}
    ```

    **sample request**

    ``curl -X DELETE localhost:5000/questions/2``

    **response**

    ```json
    {
        "deleted_question": 14,
        "questions": [
            {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            },
            {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
            },
            {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            },
            {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
            },
            {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
            },
            {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
            },
            {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
            },
            {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
            },
            {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
            },
            {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
            },
            {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
            },
            {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
            },
            {
            "answer": "Jackson Pollock",
            "category": 2,
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
            },
            {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
            },
            {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
            },
            {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
            },
            {
            "answer": "Scarab",
            "category": 4,
            "difficulty": 4,
            "id": 23,
            "question": "Which dung beetle was worshipped by the ancient Egyptians?"
            },
            {
            "answer": "yes",
            "category": 5,
            "difficulty": 5,
            "id": 25,
            "question": "weldone"
            }
        ],
        "success": true,
        "total_questions": 18
    }

    ```
- ### Categories

  this endpoint handles all processes for categories this includes retrieving categories and linked questions


  - **Retrieve Categories**: perform a ``GET`` request to this endpoint to retrieve all categories available

    ```javascript
    GET /categories
    ```

    **sample request**

    ``curl -X GET localhost:5000/categories``

    **response**

    ```json
    {
        "categories": {
            "1" : "Science",
            "2" : "Art",
            "3" : "Geography",
            "4" : "History",
            "5" : "Entertainment",
            "6" : "Sports"
         },
        "success": true,
        "total_categories": 6
    }
    ```

  - **Retrieve Questions By Category**: perform a ``GET`` request to get questions that are under category specified in the ``url`` using category ``id``

  ```javascript
      GET /categories/{id}/questions
  ```

  **sample request**

  ``curl -X GET localhost:5000/categories/6/questions``

  **response**

  ```json
  {
      "categories": {
          "1" : "Science",
          "2" : "Art",
          "3" : "Geography",
          "4" : "History",
          "5" : "Entertainment",
          "6" : "Sports"
       },
      "current_category": "Sports",
      "questions": [
          {
          "answer": "Brazil",
          "category": 6,
          "difficulty": 3,
          "id": 10,
          "question": "Which is the only team to play in every soccer World Cup tournament?"
          },
          {
          "answer": "Uruguay",
          "category": 6,
          "difficulty": 4,
          "id": 11,
          "question": "Which country won the first ever soccer World Cup in 1930?"
          }
      ],
      "success": true,
      "total_questions": 2
  }
  ```

- ### Quizzes

  This endpoint returns a random question to be used in a quiz by accepting an ``array`` of previous questions ``id`` and ``category`` which could be a ``string`` "all" or the ``id`` of the category.

  ```javascript
  POST /quizzes
  ```

  **sample request**

  ```curl
  curl -X POST -d '{"previous_questions":[5, 1],"category":"all" }'
  ```

  **response**

  ```json
    {
        "current_category": "all",
        "question": {
            "answer": "206",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "How many bones are there in the human body?"
        },
        "success": true
    }
  ```

  When the questions in the database have already been given and no more question to return the response is usually different and the ``question`` parameter becomes a ``boolean`` -> ``false``

  **response**

  ```json
  {
      "current_category":"all",
      "question": false,
      "success":true
  }
  ```
