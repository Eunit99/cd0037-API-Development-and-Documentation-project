from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


# function to format the category into key pair values e.g "1" : "Science"
def clean_category(all_categories):
    clean_categories = [category.format() for category in all_categories]
    if len(clean_categories) == 0:
        return {}
    else:
        categories = {}
        for category in clean_categories:
            categories[category["id"]] = category["type"]
        return categories


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    @COMPLETED:TODO: Set up CORS. Allow '*' for origins. Delete the sample route
    after completing the TODOs
    """
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    """
    @COMPLETED:TODO: Use the after_request decorator to set Access-Control-Allow
    """

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authentication, true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS"
        )
        return response

    """
    @COMPLETED:TODO:

    Create an endpoint to handle GET requests
    for all available categories.
    """

    @app.route("/categories")
    def get_categories():

        # get all categories and return formatted version
        all_categories = Category.query.all()
        categories = clean_category(all_categories)
        print(categories)

        return jsonify(
            {
                "success": True,
                "categories": categories,
                "total_categories": len(categories),
            }
        )

    """
    @COMPLETED:TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.
    """

    @app.route("/questions", methods=["GET"])
    def get_questions():
        # get page from query parameters
        page = request.args.get("page", 1, type=int)

        # get range index of questions return
        start = (QUESTIONS_PER_PAGE - 1) * page
        end = start + QUESTIONS_PER_PAGE

        all_categories = Category.query.all()
        categories = clean_category(all_categories)

        all_questions = Question.query.all()
        questions = [question.format() for question in all_questions]

        return jsonify(
            {
                "questions": questions[start:end],
                "total_questions": len(questions[start:end]),
                "page": page,
                "success": True,
                "categories": categories,
            }
        )

    """
    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for
    three pages.
    Clicking on the page numbers should update the questions.
    """

    """
    @COMPLETED:TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will
    be removed.
    This removal will persist in the database and when you refresh the page.
    """

    @app.route("/questions/<int:id>", methods=["DELETE"])
    def delete_question(id):
        question = Question.query.get(id)

        if question is None:
            abort(404)
        else:
            question.delete()
            all_questions = Question.query.all()
            questions = [question.format() for question in all_questions]
            return jsonify(
                {
                    "success": True,
                    "deleted_question": id,
                    "questions": questions,
                    "total_questions": len(questions),
                }
            )

    """
    @COMPLETED:TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last
    page of the questions list in the "List" tab.
    """

    @app.route("/questions", methods=["POST"])
    def create_question():
        data = request.get_json()

        if data is None:
            abort(400)

        else:
            if "search_term" in data:
                search_term = data["search_term"]
                # use ilike to get questions similar to search_term by name
                questions = Question.query.filter(
                    Question.question.ilike(f"%{search_term}%")
                ).all()
                return jsonify(
                    {
                        "success": True,
                        "questions": [question.format() for question in questions],
                        "total_questions": len(questions),
                        "search_term": search_term,
                    }
                )

            else:
                try:
                    new_question = Question(
                        question=data["question"],
                        answer=data["answer"],
                        category=data["category"],
                        difficulty=data["difficulty"],
                    )

                    # check if category is valid
                    category = Category.query.get(data["category"])

                    if category is None:
                        abort(406)

                    else:
                        new_question.insert()
                        return jsonify(
                            {"success": True, "question_created": new_question.id}
                        )

                except KeyError as e:
                    abort(406)

    """
    @COMPLETED:TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    """
    @COMPLETED:TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    @app.route("/categories/<int:id>/questions")
    def get_question_by_category(id):
        category = Category.query.get(id)

        all_categories = Category.query.all()
        categories = clean_category(all_categories)
        if category is None:
            abort(404)

        # filter questions by category gotten from url
        all_questions = Question.query.filter(Question.category == id).all()
        questions = [question.format() for question in all_questions]

        return jsonify(
            {
                "success": True,
                "questions": questions,
                "total_questions": len(questions),
                "current_category": category.type,
                "categories": categories,
            }
        )

    """
    @COMPLETED:TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    @app.route("/quizzes", methods=["POST"])
    def get_quiz_question():
        data = request.get_json()

        if data is None:
            abort(400)

        try:
            previous_questions = data["previous_questions"]
            current_category = data["category"]

            # get questions based on category value supplied
            if current_category == "all":
                all_questions = Question.query.all()

            else:
                all_questions = Question.query.filter(
                    Question.category == current_category
                ).all()

            """ create array with questions not among the supplied previous
            questions"""
            questions = []
            for question in all_questions:
                if question.id not in previous_questions:
                    questions.append(question.format())

            # checks if there are no more questions and returns a message
            if len(questions) == 0:
                return jsonify(
                    {
                        "success": True,
                        "message": "no more questions",
                        "question": False,
                        "current_category": current_category,
                    }
                )

            else:
                # checks if only 1 question remains and return it
                if len(questions) == 1:
                    question = questions[0]

                """ create a random index from the number of questions
                using random module"""
                random_index = random.randint(0, (len(questions) - 1))

            question = questions[random_index]

            return jsonify(
                {
                    "success": True,
                    "question": question,
                    "current_category": current_category,
                }
            )

        except KeyError:
            abort(406)

    """
    @COMPLETED:TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "message": "Bad Request", "error": 400}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "message": "Not Found", "error": 404}), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return (
            jsonify(
                {"success": False, "message": "Method Is Not Allowed", "error": 405}
            ),
            405,
        )

    @app.errorhandler(406)
    def method_not_acceptable(error):
        return (
            jsonify({"success": False, "message": "Not Acceptable", "error": 406}),
            406,
        )

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return (
            jsonify({"success": False, "message": "Unprocessable Entity", "error": 422}),
            422,
        )

    @app.errorhandler(500)
    def internal_server_error(error):
        return (
            jsonify({"success": False, "message": "Internal Server Error", "error": 500}),
            500,
        )

    return app
