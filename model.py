from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
        
    #In case we run more than once, empty out existing data
    Game.query.delete()

    #Add sample games
    poker = Game(game_id=1, name ="Poker", description="Try to win money by bluffing your friends out of theirs.")
    backgammon = Game(game_id=3, name="backgommon", description="Bring all your piecies to one side of your board.")

    #Add to db and commit
    db.session.add_all([poker,backgammon])
    db.session.commit()


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
