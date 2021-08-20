# -*- coding: utf-8 -*-
"""
recommendation api

"""
import jsonschema
from flask import jsonify, request as current_request
from ..util.blueprint import AppBlueprint
from ..util.helper import predict, json_validation


recommend_api = AppBlueprint('recommend', __name__)
api = recommend_api


@api.POST('/product_reco')
def get_recommend_product():
    user = current_request.get_json()
    try:
        json_validation(user)
    except jsonschema.exceptions.SchemaError as e:
        return jsonify({"message": f"invalid parameters check {str(e.message)}"}), 400
    except jsonschema.exceptions.ValidationError as e:
        return jsonify({"message": f"invalid parameters check {str(e.message)}"}), 400
    try:
        output = predict(user)
    except Exception as e:
        print(str(e))
        return "error occured while retriving recommended product", 200
    return jsonify({"recommendations": output})
