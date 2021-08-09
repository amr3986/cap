import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import APP
from models import setup_db, Movie, Actor, db


class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = APP
        self.client = self.app.test_client
        self.database_name = "agency2"
        self.database_path = "postgresql://postgres:3986@localhost:5432/agency2"
        setup_db(self.app, self.database_path)

        self.assistant_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlQ3Y05rQ21xb19KQzZzNV8tMDJMcSJ9.eyJpc3MiOiJodHRwczovL2Rldi1rb3RicjE5MC51cy5hdXRoMC5jb20vIiwic3ViIjoiRHJDdkNFekxHbXBSYnV6dkJobVdRTlFNQmVCMlJmUllAY2xpZW50cyIsImF1ZCI6ImNhcCIsImlhdCI6MTYyODUxMzk5MywiZXhwIjoxNjI4NzczMTkzLCJhenAiOiJEckN2Q0V6TEdtcFJidXp2QmhtV1FOUU1CZUIyUmZSWSIsInNjb3BlIjoiZ2V0OmFjdG9ycyBnZXQ6bW92aWVzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.CD9YoTH8jMKnOFoD5DRPz5_aN0xXeFrJLSOs5PTxr3ifDWYM_0po2LCwgUOitrsjBSPD_cQ4TRgYL7C8Q3S_66MgF50lDKuCh5zdFFR6pkf-d5Rv1881rSEf1PY6pvbTOvhHYzT6rmdt_NMcMoe8aEtGSFoIkyV75se8OMia-g8siVS8OMq_bYNfdimDcb7zuQPF-P1uTghAUPfET4pt7oIDg_-ukBc3tVrtA_aQfMtdFpa9zHIDKAvCS-4DsfpVWigUPAcQvJ2a1bY8ASIh61AC3BIhehvjP9Eu0lq6r-gBA-sH6tb7ziAZNLXEwII2ZTt-0ONh69snG8Mptge7FA'
        }

        self.director_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlQ3Y05rQ21xb19KQzZzNV8tMDJMcSJ9.eyJpc3MiOiJodHRwczovL2Rldi1rb3RicjE5MC51cy5hdXRoMC5jb20vIiwic3ViIjoiRHJDdkNFekxHbXBSYnV6dkJobVdRTlFNQmVCMlJmUllAY2xpZW50cyIsImF1ZCI6ImNhcCIsImlhdCI6MTYyODUxNDA5OCwiZXhwIjoxNjI4NzczMjk4LCJhenAiOiJEckN2Q0V6TEdtcFJidXp2QmhtV1FOUU1CZUIyUmZSWSIsInNjb3BlIjoiZ2V0OmFjdG9ycyBnZXQ6bW92aWVzIHBvc3Q6YWN0b3IgcGF0Y2g6YWN0b3IgcGF0Y2g6bW92aWUgZGVsZXRlOmFjdG9yIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9yIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsImRlbGV0ZTphY3RvciJdfQ.cj4ODjkWgze38pmgRcqT-QF9jhAT0KWrlqkqPuvOv7x8c40JCYTsIYrPrqGC3HTlcaZ6nusX0iTU-OeICFnh1LJFOSDmJtidQsPGNWkBJY08OswO6yfE8tNd2UxywGFm9GxQh2i25l2QF3o4ovRYjuDapVyYchAtmUwqIQJ9zZ6MlQyfS2qBnIkvmDXEYmJvXhU9ekGG1qyQ-mFbsiPdC9M3GYBzyabD7wUL9wVYmeoCsFY2hO7uUNmcDoHCw0YTlM3p1-l1xq106TjAqqBMG8gosc9lqWCtB-tScxcQNmbVzzQz4mPzavfdPN6htDDHasKdEc6Yb_brl8PM16nw9w'
        }

        self.producer_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlQ3Y05rQ21xb19KQzZzNV8tMDJMcSJ9.eyJpc3MiOiJodHRwczovL2Rldi1rb3RicjE5MC51cy5hdXRoMC5jb20vIiwic3ViIjoiRHJDdkNFekxHbXBSYnV6dkJobVdRTlFNQmVCMlJmUllAY2xpZW50cyIsImF1ZCI6ImNhcCIsImlhdCI6MTYyODUxMzkzNCwiZXhwIjoxNjI4NzczMTM0LCJhenAiOiJEckN2Q0V6TEdtcFJidXp2QmhtV1FOUU1CZUIyUmZSWSIsInNjb3BlIjoiZ2V0OmFjdG9ycyBnZXQ6bW92aWVzIHBvc3Q6YWN0b3IgcG9zdDptb3ZpZSBwYXRjaDphY3RvciBwYXRjaDptb3ZpZSBkZWxldGU6YWN0b3IgZGVsZXRlOm1vdmllIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiXX0.lVCtO-oq-qHjrV_H-8oWtf1bnEm4RTvGCU5jEj3XizC550pYbn2hccqOs6gWAnys2YG_rQsRaNeXuXjNZX7_dSBlx3CsgemchR5GSdY5MksFaIGvR_Qd8RALQ2XwrmEAr7lTXB_SRWbpsyD8QGWw9oNYZtObY8L9vcyoCMldIJ8t1ff9WP9KnMdUGXlL14tAxMSkX28Xq1TFs6XeKKhqdWlNaKp12xRJl5X8DwBef-pLr6dZqzGJuIBQmUXGB1jsJbQ4cVTAu2FdWg3TqDvDDseTpCWMBaKfu53eRD8VskeNreH2zyQc-1P4WHvcuw2QVEOgL2gN9rubht8LDSu4Fg'
        }

        self.movie = {
            'title': 'Knives Out ',
            'release_date': '2019'
        }

        self.new_movie = {
            'title': 'Space',
            'release_date': '2020'
        }

        self.actor = {
            'name': 'Daniel Craig',
            'age': '52',
            'gender': 'Male'
        }

        self.new_actor = {
            'name': 'Chris Evans',
            'age': '38',
            'gender': 'Male'
        }

        with self.app.app_context():
            self.db = db
            self.db.init_app(self.app)
            self.db.create_all()

        self.client().post('/movies', json=self.movie, headers=self.producer_header)
        self.client().post('/actors', json=self.actor, headers=self.producer_header)

    def tearDown(self):
        self.db.drop_all()
        pass

    def test_get_actors_public(self):
        res = self.client().get('/actors')

        self.assertEqual(res.status_code, 401)

    def test_get_actors_assistant(self):
        res = self.client().get('/actors', headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['actors']))

    def test_get_actors_director(self):
        res = self.client().get('/actors', headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['actors']))

    def test_get_actors_producer(self):
        res = self.client().get('/actors', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['actors']))

    def test_get_movies_public(self):
        res = self.client().get('/movies')

        self.assertEqual(res.status_code, 401)

    def test_get_movies_assistant(self):
        res = self.client().get('/movies', headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['movies']))

    def test_get_movies_director(self):
        res = self.client().get('/movies', headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['movies']))

    def test_get_movies_producer(self):
        res = self.client().get('/movies', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['movies']))

    def test_post_actors_public(self):
        res = self.client().post('/actors', json=self.new_actor)

        self.assertEqual(res.status_code, 401)

    def test_post_actors_assistant(self):
        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers=self.assistant_header)

        self.assertEqual(res.status_code, 401)

    def test_post_actors_director(self):
        original_count = len(Actor.query.all())

        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertGreater(data['id'], 0)

    def test_post_actors_producer(self):
        original_count = len(Actor.query.all())

        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertGreater(data['id'], 0)

    def test_post_movies_public(self):
        res = self.client().post('/movies', json=self.new_movie)

        self.assertEqual(res.status_code, 401)

    def test_post_movies_assistant(self):
        res = self.client().post(
            '/movies',
            json=self.new_movie,
            headers=self.assistant_header)

        self.assertEqual(res.status_code, 401)

    def test_post_movies_producer(self):
        original_count = len(Movie.query.all())

        res = self.client().post(
            '/movies',
            json=self.new_movie,
            headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertGreater(data['id'], 0)

    def test_patch_actors_public(self):
        res = self.client().patch('/actors/1', json={'age': "33"})

        self.assertEqual(res.status_code, 401)

    def test_patch_actors_assistant(self):
        res = self.client().patch(
            '/actors/1',
            json={
                'age': "33"},
            headers=self.assistant_header)

        self.assertEqual(res.status_code, 401)

    def test_patch_actors_director(self):
        res = self.client().patch(
            '/actors/1',
            json={
                'age': "33"},
            headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actors_producer(self):
        res = self.client().patch(
            '/actors/1',
            json={
                'age': "33"},
            headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actors_does_not_exist(self):
        res = self.client().patch(
            '/actors/1000',
            json={
                'age': "33"},
            headers=self.producer_header)

        self.assertEqual(res.status_code, 404)

    def test_patch_actors_no_data(self):
        res = self.client().patch('/actors/1', headers=self.producer_header)

        self.assertEqual(res.status_code, 404)

    def test_patch_movies_public(self):
        res = self.client().patch('/movies/1', json={'title': "New Title"})

        self.assertEqual(res.status_code, 401)

    def test_patch_movies_assistant(self):
        res = self.client().patch(
            '/movies/1',
            json={
                'title': " New Title"},
            headers=self.assistant_header)

        self.assertEqual(res.status_code, 401)

    def test_patch_movies_director(self):
        res = self.client().patch(
            '/movies/1',
            json={
                'title': "New Title"},
            headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movies_producer(self):
        res = self.client().patch(
            '/movies/1',
            json={
                'title': "New Title"},
            headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movies_does_not_exist(self):
        res = self.client().patch(
            '/movies/1000',
            json={
                'title': "New Title"},
            headers=self.producer_header)

        self.assertEqual(res.status_code, 404)

    def test_patch_movies_no_data(self):
        res = self.client().patch('/movies/1', headers=self.producer_header)

        self.assertEqual(res.status_code, 404)

    def test_delete_actors_public(self):
        res = self.client().delete('/actors/1')

        self.assertEqual(res.status_code, 401)

    def test_delete_actors_assistant(self):
        res = self.client().delete('/actors/1', headers=self.assistant_header)

        self.assertEqual(res.status_code, 401)

    def test_delete_actors_producer(self):
        res = self.client().delete('/actors/1', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actors_does_not_exist(self):
        res = self.client().delete('/actors/1000', headers=self.producer_header)

        self.assertEqual(res.status_code, 404)

    def test_delete_movies_public(self):
        res = self.client().delete('/movies/1')

        self.assertEqual(res.status_code, 401)

    def test_delete_movies_assistant(self):
        res = self.client().delete('/movies/1', headers=self.assistant_header)

        self.assertEqual(res.status_code, 401)

    def test_delete_movies_director(self):
        res = self.client().delete('/movies/1', headers=self.director_header)

        self.assertEqual(res.status_code, 401)

    def test_delete_movies_producer(self):
        res = self.client().delete('/movies/1', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movies_does_not_exist(self):
        res = self.client().delete('/movies/1000', headers=self.producer_header)

        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()