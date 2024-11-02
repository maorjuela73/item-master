import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import app
from app import Base, Evaluador, Item

class TestEvaluador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session = self.Session()
        app.session = self.session
        self.evaluador = Evaluador(nombre='Test Evaluador', email='test@example.com')
        self.session.add(self.evaluador)
        self.session.commit()

    def tearDown(self):
        # Clear all tables after each test
        self.session.query(Evaluador).delete()
        self.session.query(Item).delete()
        self.session.commit()
        self.session.close()

    def test_crear_item(self):
        item = self.evaluador.crear_item(
            contenido='Test item',
            dificultad=0.5,
            discriminacion=0.5,
            adivinacion=0.1
        )
        self.assertIsNotNone(item.id)
        self.assertEqual(item.contenido, 'Test item')
        item_in_db = self.session.query(Item).filter_by(id=item.id).first()
        self.assertIsNotNone(item_in_db)

    def test_editar_item(self):
        item = self.evaluador.crear_item(
            contenido='Original content',
            dificultad=0.5,
            discriminacion=0.5,
            adivinacion=0.1
        )
        updated_item = self.evaluador.editar_item(
            item_id=item.id,
            contenido='Updated content'
        )
        self.assertEqual(updated_item.contenido, 'Updated content')
        item_in_db = self.session.query(Item).filter_by(id=item.id).first()
        self.assertEqual(item_in_db.contenido, 'Updated content')

    def test_eliminar_item(self):
        item = self.evaluador.crear_item(
            contenido='Item to delete',
            dificultad=0.5,
            discriminacion=0.5,
            adivinacion=0.1
        )
        result = self.evaluador.eliminar_item(item_id=item.id)
        self.assertTrue(result)
        item_in_db = self.session.query(Item).filter_by(id=item.id).first()
        self.assertIsNone(item_in_db)

    def test_eliminar_item_nonexistent(self):
        result = self.evaluador.eliminar_item(item_id=999)
        self.assertFalse(result)

    def test_editar_item_nonexistent(self):
        updated_item = self.evaluador.editar_item(
            item_id=999,
            contenido='Should not work'
        )
        self.assertIsNone(updated_item)

if __name__ == '__main__':
    unittest.main()