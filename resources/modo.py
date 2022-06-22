from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, jwt_required

import mysql.connector
from ref.mysql_connection import get_connection

from ref.utils import check_password, hash_password
from email_validator import validate_email, EmailNotValidError

class MemoListResource(Resource) :
    @jwt_required()
    def post(self) :

        # 1. 클라이언트로부터 데이터를 받아온다.
        # {
        #    "title": "커피",
        #   "date": "2022-07-01 11:00",
        #    "content": "커피마시면서 개발"
        # }

        data = request.get_json()
        user_id = get_jwt_identity()
        return