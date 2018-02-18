import logging

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

config = Blueprint('config', __name__)

@config.route('/')
def home():
  return 'Hello World!'
