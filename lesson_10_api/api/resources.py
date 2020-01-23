from flask_restful import Resource
from .schema import DevelopersSchema
from .models import Developer
from flask import request

class DeveloperResource(Resource):

    def get(self, dev_id=None):

        query = Developer.objects if not dev_id else Developer.objects.get(id=dev_id)
        many = not dev_id

        return DevelopersSchema().dump(
            query,
            many=many
        )

    def post(self):
        err = DevelopersSchema().validate(
            request.json
        )

        if err:
            return err

        dev = Developer(**request.get_json()).save()

        dev.reload()
        return DevelopersSchema().dump(dev)

    def put(self):
        return 'put'

    def delete(self):
        return 'delete'