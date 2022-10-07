import json


from flask import request

from app.create_app import db, app
from app.models import User, Order, Offer


@app.route("/users", methods=['GET', 'POST'])
def work_users():

    if request.method == 'GET':
        result = []
        for user in db.session.query(User).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result),
            minetype="application/json",
            status=200
        )

    if request.method == 'POST':
        data = request.json

        db.session.add(
            User(
                **data
            )
        )

        return app.response_class(
            json.dumps("OK"),
            minetype="application/json",
            status=200
        )



@app.route("/users/<int:bid>", methods=['GET', 'PUT', 'DELETE'])
def work_user(bid):

    if request.method == 'GET':
        result = []
        for user in db.session.query(User).filter(User.id == bid).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result),
            minetype="application/json",
            status=200
        )

    if request.method == 'PUT':
        data = request.json
        try:
            user = db.session.query(User).get(bid)
            user.id = data.get("id")
            user.first_name = data.get("first_name")
            user.last_name = data.get("last_name")
            user.age = data.get("age")
            user.email = data.get("email")
            user.role = data.get("role")
            user.phone = data.get("phone")

            db.session.commit()
        except Exception as e:
            print(e)
            ...

        return app.response_class(
            json.dumps("OK"),
            minetype="application/json",
            status=200
        )

    if request.method == 'DELETE':
        try:
            db.session.query(User).filter(User.id == bid).delete()
            db.session.commit()
        except Exception as e:
            print(e)
            ...

        return app.response_class(
            json.dumps("OK"),
            minetype="application/json",
            status=200
        )

@app.route("/orders", methods=['GET', 'POST'])
def work_orders():

    if request.method == 'GET':
        result = []
        for user in db.session.query(Order).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result),
            minetype="application/json",
            status=200
        )

    if request.method == 'POST':
        data = request.json

        db.session.add(
            Order(
                **data
            )
        )

        return app.response_class(
            json.dumps("OK"),
            minetype="application/json",
            status=200
        )


@app.route("/orders/<int:bid>", methods=['GET', 'POST'])
def work_order(bid):

    if request.method == 'GET':
        result = []
        for user in db.session.query(Order).filter(Order.id == bid).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result, ensure_ascii=False),
            minetype="application/json",
            status=200
        )

    if request.method == 'POST':
        data = request.json

        db.session.add(
            Order(
                **data
            )
        )

        return app.response_class(
            json.dumps("OK"),
            minetype="application/json",
            status=200
        )

    if request.method == 'PUT':
        data = request.json
        try:
            user = db.session.query(Order).get(bid)
            user.id = data.get("id")
            user.name = data.get("name")
            user.description = data.get("description")
            user.start_date = data.get("start_date")
            user.end_date = data.get("end_date")
            user.address = data.get("address")
            user.price = data.get("price")
            user.customer_id = data.get("customer_id")
            user.executor_id = data.get("executor_id")
            db.session.commit()
        except Exception as e:
            print(e)
            ...

        return app.response_class(
            json.dumps("OK"),
            minetype="application/json",
            status=200
        )

    if request.method == 'DELETE':
        try:
            db.session.query(Order).filter(User.id == bid).delete()
            db.session.commit()
        except Exception as e:
            print(e)
            ...

        return app.response_class(
            json.dumps("OK"),
            minetype="application/json",
            status=200
        )



@app.route("/offers", methods=['GET', 'POST'])
def work_offers():

    if request.method == 'GET':
        result = []
        for user in db.session.query(Offer).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result),
            minetype="application/json",
            status=200
        )

    if request.method == 'POST':
        data = request.json

        db.session.add(
            Offer(
                **data
            )
        )

        return app.response_class(
            json.dumps("OK"),
            minetype="application/json",
            status=200
        )


@app.route("/offers/<int:bid>", methods=['GET', 'POST'])
def work_offer(bid):

    if request.method == 'GET':
        result = []
        for user in db.session.query(Offer).filter(Offer.id == bid).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result, ensure_ascii=False),
            minetype="application/json",
            status=200
        )

    if request.method == 'POST':
        data = request.json

        db.session.add(
            Offer(
                **data
            )
        )

        return app.response_class(
            json.dumps("OK"),
            minetype="application/json",
            status=200
        )

    if request.method == 'PUT':
        data = request.json
        try:
            user = db.session.query(Offer).get(bid)
            user.id = data.get("id")
            user.order_id = data.get("order_id")
            user.executor_id = data.get("executor_id")


            db.session.commit()
        except Exception as e:
            print(e)
            ...

        return app.response_class(
            json.dumps("OK"),
            minetype="application/json",
            status=200
        )

    if request.method == 'DELETE':
        try:
            db.session.query(Offer).filter(Offer.id == bid).delete()
            db.session.commit()
        except Exception as e:
            print(e)
            ...

        return app.response_class(
            json.dumps("OK"),
            minetype="application/json",
            status=200
        )

if __name__ == '__main__':
    app.run("localhost", port=8080, debug=True)