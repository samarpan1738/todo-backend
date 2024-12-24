from unittest import TestCase
from bson import ObjectId
from pydantic import BaseModel, ValidationError

from todo.models.common.pyobjectid import PyObjectId


class PyObjectIdTests(TestCase):
    def test_validate_valid_objectid(self):
        valid_id = str(ObjectId())
        validated = PyObjectId.validate(valid_id)
        self.assertEqual(validated, ObjectId(valid_id))

    def test_validate_invalid_objectid(self):
        invalid_id = "invalid_objectid"
        with self.assertRaises(ValueError) as context:
            PyObjectId.validate(invalid_id)
        self.assertIn(f"Invalid ObjectId: {invalid_id}", str(context.exception))

    def test_validate_none(self):
        self.assertIsNone(PyObjectId.validate(None))

    def test_pydantic_json_schema(self):
        field_schema = {}
        PyObjectId.__get_pydantic_json_schema__(field_schema)
        self.assertEqual(field_schema["type"], "string")

    def test_integration_with_pydantic_model(self):
        class TestModel(BaseModel):
            id: PyObjectId

        valid_id = str(ObjectId())
        instance = TestModel(id=valid_id)
        self.assertEqual(instance.id, ObjectId(valid_id))

        invalid_id = "invalid_objectid"
        with self.assertRaises(ValidationError) as context:
            TestModel(id=invalid_id)
        self.assertIn(f"Invalid ObjectId: {invalid_id}", str(context.exception))

        try:
            TestModel(id=None)
        except ValidationError:
            self.fail("ValidationError raised for None id")
