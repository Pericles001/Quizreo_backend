from unittest import TestCase


class Test(TestCase):
    def test_root(self):
        from app.main import app
        from starlette.testclient import TestClient
        client = TestClient(app)
        response = client.get("/")
        self.assertEqual(200, response.status_code)

    def test_db(self):
        from app.main import get_db
        self.assertIsNotNone(get_db())

    def test_db_engine(self):
        from app.main import engine
        self.assertIsNotNone(engine)

    def test_db_models(self):
        from app.main import user, quiz, survey, trial, party, answer
        self.assertIsNotNone(user)
        self.assertIsNotNone(quiz)
        self.assertIsNotNone(survey)
        self.assertIsNotNone(trial)
        self.assertIsNotNone(party)
        self.assertIsNotNone(answer)

    def test_db_metadata(self):
        from app.main import user, quiz, survey, trial, party, answer
        self.assertIsNotNone(user.Base.metadata)
        self.assertIsNotNone(quiz.Base.metadata)
        self.assertIsNotNone(survey.Base.metadata)
        self.assertIsNotNone(trial.Base.metadata)
        self.assertIsNotNone(party.Base.metadata)
        self.assertIsNotNone(answer.Base.metadata)

    def test_db_create_all(self):
        from app.main import engine, user, quiz, survey, trial, party, answer
        user.Base.metadata.create_all(bind=engine)
        quiz.Base.metadata.create_all(bind=engine)
        survey.Base.metadata.create_all(bind=engine)
        trial.Base.metadata.create_all(bind=engine)
        party.Base.metadata.create_all(bind=engine)
        answer.Base.metadata.create_all(bind=engine)
        self.assertTrue(True)

    def test_db_tables(self):
        from app.main import engine
        self.assertTrue(engine.has_table('users'))
        self.assertTrue(engine.has_table('quizzes'))
        self.assertTrue(engine.has_table('surveys'))
        self.assertTrue(engine.has_table('trials'))
        self.assertTrue(engine.has_table('parties'))
        self.assertTrue(engine.has_table('answers'))

    def test_db_tables_columns(self):
        from app.main import engine
        users = engine.execute('SELECT * FROM users')
        self.assertEqual(['id', 'email', 'hashed_password', 'is_active', 'is_superuser'], users.keys())
        quizzes = engine.execute('SELECT * FROM quizzes')
        self.assertEqual(['id', 'title', 'description', 'created_at', 'updated_at'], quizzes.keys())
        surveys = engine.execute('SELECT * FROM surveys')
        self.assertEqual(['id', 'title', 'description', 'created_at', 'updated_at'], surveys.keys())
        trials = engine.execute('SELECT * FROM trials')
        self.assertEqual(['id', 'title', 'description', 'created_at', 'updated_at'], trials.keys())