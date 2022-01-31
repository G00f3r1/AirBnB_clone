#!/usr/bin/python3
"""Defining Review model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defining Review class"""

    place_id = ""
    user_id = ""
    text = ""
