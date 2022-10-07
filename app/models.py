from app import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    role = db.Column(db.String)
    phone = db.Column(db.String)

    def return_data(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    star_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.Integer)

    customer_id = db.Column(db.Integer, db.ForeignKey(f"{User.__tablename__}.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey(f"{User.__tablename__}.id"))

    customer = db.relationship("User", foreign_keys=[customer_id])
    executor = db.relationship("User", foreign_keys=[executor_id])

    def return_data(self):
        return {
            "my_id": self.id,
            "name": self.name,
            "description": self.description,
            "start_sate": self.start_sate,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id,
            "customer": self.customer.return_data(),
            "executor": self.executor.return_data()

        }


class Offer(db.Model):
    __tablename__ = "offer"
    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey(f"{Order.__tablename__}.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey(f"{User.__tablename__}.id"))

    order = db.relationship("Order")
    executor = db.relationship("Order")

    def return_data(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
            "order": self.order.return_data(),
            "executor": self.executor.return_data()

        }
